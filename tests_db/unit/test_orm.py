import pytest

from sqlalchemy.exc import IntegrityError

from music.domainmodel.user import User
from music.domainmodel.track import Track
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre


def insert_users(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO users (user_name, password) VALUES (:user_name, :password)',
                              {'user_name': value[0], 'password': value[1]})
    rows = list(empty_session.execute('SELECT id from users'))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_tracks(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO tracks (id, title) VALUES (:id, :title)',
                              {'id': value[0], 'title': value[1]})
    rows = list(empty_session.execute('SELECT id from tracks'))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_albums(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO albums (id, title) VALUES (:id, :title)',
                              {'id': value[0], 'title': value[1]})
    rows = list(empty_session.execute('SELECT id from albums'))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_artists(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO artists (id, name) VALUES (:id, :name)',
                              {'id': value[0], 'name': value[1]})
    rows = list(empty_session.execute('SELECT id from artists'))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_genres(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO genres (id, name) VALUES (:id, :name)',
                              {'id': value[0], 'name': value[1]})
    rows = list(empty_session.execute('SELECT id from genres'))
    keys = tuple(row[0] for row in rows)
    return keys

def make_user():
    user = User("Andrew", "111")
    return user

def  make_track():
    track = Track(1, "mickey mouse")
    return track

def make_album():
    album = Album(2, 'overwatch')
    return album

def make_artist():
    artist = Artist(2, 'drake')
    return artist

def make_genre():
    genre = Genre(6, 'hip-hop')
    return genre

#user
def test_loading_of_users(empty_session):
    users = list()
    users.append(("Andrew", "1234"))
    users.append(("Cindy", "1111"))
    insert_users(empty_session, users)

    expected = [
        User("Andrew", "1234"),
        User("Cindy", "999")
    ]
    assert empty_session.query(User).all() == expected

def test_saving_of_users(empty_session):
    user = make_user()
    empty_session.add(user)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT user_name, password FROM users'))
    assert rows == [("Andrew", "111")]

#track
def test_loading_of_tracks(empty_session):
    tracks = list()
    tracks.append((13, 'hello kitty', 'http/hi', 34))
    tracks.append((15, 'mickey_mouse', 'http/bye', 100))
    insert_tracks(empty_session, tracks)

    expected = [
        Track(13, 'hello kitty'),
        Track(15, 'mickey mouse')
    ]
    assert empty_session.query(Track).all() == expected

def test_saving_of_tracks(empty_session):
    track = make_track()
    empty_session.add(track)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT id, title FROM tracks'))
    assert rows == [(1, "mickey mouse")]

#album
def test_loading_of_albums(empty_session):
    albums = list()
    albums.append((13, 'hello kitty'))
    albums.append((15, 'mickey_mouse'))
    insert_albums(empty_session, albums)

    expected = [
        Album(13, 'hello kitty'),
        Album(15, 'mickey mouse')
    ]
    assert empty_session.query(Album).all() == expected

def test_saving_of_albums(empty_session):
    album = make_album()
    empty_session.add(album)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT id, title FROM albums'))
    assert rows == [(2, "overwatch")]

#artist
def test_loading_of_artists(empty_session):
    artists = list()
    artists.append((13, 'hello kitty'))
    artists.append((15, 'mickey_mouse'))
    insert_artists(empty_session, artists)

    expected = [
        Artist(13, 'hello kitty'),
        Artist(15, 'mickey mouse')
    ]
    assert empty_session.query(Artist).all() == expected

def test_saving_of_artists(empty_session):
    artist = make_artist()
    empty_session.add(artist)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT id, name FROM artists'))
    assert rows == [(2, "drake")]

#genre
def test_loading_of_genres(empty_session):
    genres = list()
    genres.append((13, 'hello kitty'))
    genres.append((15, 'mickey_mouse'))
    insert_genres(empty_session, genres)

    expected = [
        Genre(13, 'hello kitty'),
        Genre(15, 'mickey mouse')
    ]
    assert empty_session.query(Genre).all() == expected

def test_saving_of_genres(empty_session):
    genre = make_genre()
    empty_session.add(genre)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT id, name FROM genres'))
    assert rows == [(6, "hip-hop")]
