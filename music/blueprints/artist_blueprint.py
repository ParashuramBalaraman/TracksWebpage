from flask import Blueprint, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

from music.adapters.memoryrepository import tracks_repo
from music.adapters.memoryrepository import artists_repo


artist_blueprint = Blueprint('artist_blueprint', __name__)


@artist_blueprint.route('/artists')
def list_of_artists():
    artists_per_page = 30
    cursor = request.args.get('cursor')
    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if cursor + 29 >= len(artists_repo):
        artists = artists_repo[cursor:]
    elif cursor == 0:
        artists = artists_repo[0: 30]
    else:
        artists = artists_repo[cursor: cursor + 30]

    first_page = None
    prev_page = None
    last_page = None
    next_page = None

    if cursor > 0:
        prev_page = url_for('artist_blueprint.list_of_artists', cursor=cursor - artists_per_page)
        first_page = url_for('artist_blueprint.list_of_artists', cursor=0)

    if cursor + 30:
        if cursor == 0:
            next_page = url_for('artist_blueprint.list_of_artists', cursor=artists_per_page)
        else:
            next_page = url_for('artist_blueprint.list_of_artists', cursor=cursor + artists_per_page)
        last_cursor = artists_per_page * int(len(artists_repo) / artists_per_page)
        if len(artists_repo) % artists_per_page == 0:
            last_cursor -= artists_per_page
        if last_cursor == cursor:
            last_page = None
            next_page = None
        else:
            last_page = url_for('artist_blueprint.list_of_artists', cursor=last_cursor)
    return render_template(
        'artists_list.html',
        artists=artists,
        first_page=first_page,
        last_page=last_page,
        prev_page=prev_page,
        next_page=next_page
    )

@artist_blueprint.route('/find_artist', methods=['GET', 'POST'])
def find_artist():
    form = SearchForm_artist()
    if form.validate_on_submit():
        return redirect(
            url_for('artist_blueprint.artist_view', artist=form.artist.data)
        )
    else:
        return render_template(
            'artist_search.html',
            form=form,
            handler_url=url_for('artist_blueprint.find_artist')
        )


@artist_blueprint.route('/artists/<string:artist>')
def artist_view(artist):
    artists = []
    for track in tracks_repo:
        if track.artist.full_name == artist:
            artists.append(track)
    if len(artists) == 0:
        return render_template('not_found.html')
    return render_template('artist_view.html', artists=artists)

class SearchForm_artist(FlaskForm):
    artist = StringField("Enter the name of the artist", [DataRequired()])
    submit = SubmitField("Search")