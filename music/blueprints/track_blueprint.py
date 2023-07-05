from flask import Blueprint, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

from music.adapters.memoryrepository import tracks_repo

track_blueprint = Blueprint('track_blueprint', __name__)

@track_blueprint.route('/')
def home():
    return render_template('home.html')

@track_blueprint.route('/tracks', methods=['GET'])
def list_of_tracks():
    tracks_per_page = 30
    cursor = request.args.get('cursor')
    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if cursor + 29 >= len(tracks_repo):
        tracks = tracks_repo[cursor : ]
    elif cursor == 0:
        tracks = tracks_repo[0 : 30]
    else:
        tracks = tracks_repo[cursor : cursor + 30]

    first_page = None
    prev_page = None
    last_page = None
    next_page = None

    if cursor > 0:
        prev_page = url_for('track_blueprint.list_of_tracks', cursor=cursor - tracks_per_page)
        first_page = url_for('track_blueprint.list_of_tracks', cursor = 0)

    if cursor + 30:
        if cursor == 0:
            next_page = url_for('track_blueprint.list_of_tracks', cursor=tracks_per_page)
        else:
            next_page = url_for('track_blueprint.list_of_tracks', cursor=cursor + tracks_per_page)
        last_cursor = tracks_per_page * int(len(tracks_repo) / tracks_per_page)
        if len(tracks_repo) % tracks_per_page == 0:
            last_cursor -= tracks_per_page
        if last_cursor == cursor:
            last_page = None
            next_page = None
        else:
            last_page = url_for('track_blueprint.list_of_tracks', cursor=last_cursor)
    return render_template(
        'track_list.html',
        tracks = tracks,
        first_page = first_page,
        last_page = last_page,
        prev_page = prev_page,
        next_page = next_page
    )

@track_blueprint.route('/find_track', methods=['GET', 'POST'])
def find_track():
    form = SearchForm_track()
    if form.validate_on_submit():
        return redirect(
            url_for('track_blueprint.track_view', track_name=form.track.data)
        )
    else:
        return render_template(
            'track_search.html',
            form=form,
            handler_url=url_for('track_blueprint.find_track')
        )

@track_blueprint.route('/tracks/<string:track_name>')
def track_view(track_name):
    for track in tracks_repo:
        if track.title == track_name:
            return render_template(
                'track_view.html',
                title=track.title,
                title_url = track.track_url,
                artist=track.artist.full_name,
                album =track.album.title,
            )
    return render_template('not_found.html')

class SearchForm_track(FlaskForm):
    track = StringField("Enter the name of the track", [DataRequired()])
    submit = SubmitField("Search")



