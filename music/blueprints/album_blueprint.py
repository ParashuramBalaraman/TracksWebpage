from flask import Blueprint, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

from music.adapters.memoryrepository import tracks_repo
from music.adapters.memoryrepository import albums_repo

album_blueprint = Blueprint('album_blueprint', __name__)

@album_blueprint.route('/albums', methods=['GET'])
def list_of_albums():
    albums_per_page = 30
    cursor = request.args.get('cursor')
    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if cursor + 29 >= len(albums_repo):
        albums = albums_repo[cursor:]
    elif cursor == 0:
        albums = albums_repo[0: 30]
    else:
        albums = albums_repo[cursor: cursor + 30]

    first_page = None
    prev_page = None
    last_page = None
    next_page = None

    if cursor > 0:
        prev_page = url_for('album_blueprint.list_of_albums', cursor=cursor - albums_per_page)
        first_page = url_for('album_blueprint.list_of_albums', cursor=0)

    if cursor + 30:
        if cursor == 0:
            next_page = url_for('album_blueprint.list_of_albums', cursor=albums_per_page)
        else:
            next_page = url_for('album_blueprint.list_of_albums', cursor=cursor + albums_per_page)
        last_cursor = albums_per_page * int(len(albums_repo) / albums_per_page)
        if len(albums_repo) % albums_per_page == 0:
            last_cursor -= albums_per_page
        if last_cursor == cursor:
            last_page = None
            next_page = None
        else:
            last_page = url_for('album_blueprint.list_of_albums', cursor=last_cursor)
    return render_template(
        'album_list.html',
        albums=albums,
        first_page=first_page,
        last_page=last_page,
        prev_page=prev_page,
        next_page=next_page
    )

@album_blueprint.route('/find_album', methods=['GET', 'POST'])
def find_album():
    form = SearchForm_album()
    if form.validate_on_submit():
        return redirect(
            url_for('album_blueprint.album_view', album_name=form.album.data)
        )
    else:
        return render_template(
            'album_search.html',
            form=form,
            handler_url=url_for('album_blueprint.find_album')
        )

@album_blueprint.route('/albums/<string:album_name>')
def album_view(album_name):
    track_list = []
    for track in tracks_repo:
        if track.album != None:
            if track.album.title == album_name:
                track_list.append(track)
    if len(track_list) == 0:
        return render_template('not_found.html')
    return render_template('album_view.html', tracks=track_list)


class SearchForm_album(FlaskForm):
    album = StringField("Enter the name of the album", [DataRequired()])
    submit = SubmitField("Search")