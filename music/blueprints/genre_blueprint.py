from flask import Blueprint, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

from music.adapters.memoryrepository import tracks_repo
from music.adapters.memoryrepository import genres_repo

genre_blueprint = Blueprint('genre_blueprint', __name__)

@genre_blueprint.route('/genres')
def list_of_genres():
    genres_per_page = 30
    cursor = request.args.get('cursor')
    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if cursor + 29 >= len(genres_repo):
        genres = genres_repo[cursor:]
    elif cursor == 0:
        genres = genres_repo[0: 30]
    else:
        genres = genres_repo[cursor: cursor + 30]

    first_page = None
    prev_page = None
    last_page = None
    next_page = None

    if cursor > 0:
        prev_page = url_for('genre_blueprint.list_of_genres', cursor=cursor - genres_per_page)
        first_page = url_for('genre_blueprint.list_of_genres', cursor=0)

    if cursor + 30:
        if cursor == 0:
            next_page = url_for('genre_blueprint.list_of_genres', cursor=genres_per_page)
        else:
            next_page = url_for('genre_blueprint.list_of_genres', cursor=cursor + genres_per_page)
        last_cursor = genres_per_page * int(len(genres_repo) / genres_per_page)
        if len(genres_repo) % genres_per_page == 0:
            last_cursor -= genres_per_page
        if last_cursor == cursor:
            last_page = None
            next_page = None
        else:
            last_page = url_for('genre_blueprint.list_of_genres', cursor=last_cursor)
    return render_template(
        'genre_list.html',
        genres=genres,
        first_page=first_page,
        last_page=last_page,
        prev_page=prev_page,
        next_page=next_page
    )

@genre_blueprint.route('/find_genre', methods=['GET', 'POST'])
def find_genre():
    form = SearchForm_genre()
    if form.validate_on_submit():
        return redirect(
            url_for('genre_blueprint.genre_view', genre_name=form.genre.data)
        )
    else:
        return render_template(
            'genre_search.html',
            form=form,
            handler_url=url_for('genre_blueprint.find_genre')
        )

@genre_blueprint.route('/genres/<string:genre_name>')
def genre_view(genre_name):
    genres = []
    for track in tracks_repo:
        for genre in track.genres:
            if genre.name == genre_name:
                genres.append(track)
    if len(genres) == 0:
        return render_template('not_found.html')
    return render_template('genre_view.html', genres=genres)

class SearchForm_genre(FlaskForm):
    genre = StringField("Enter the genre", [DataRequired()])
    submit = SubmitField("Search")