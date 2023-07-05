from sqlalchemy import (
    Table, MetaData, Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.domainmodel.track import Track
from music.domainmodel.user import User

metadata = MetaData()

tracks_table = Table(
    'tracks', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('artist_id', ForeignKey('artists.id')),
    Column('album_id', ForeignKey('albums.id')),
    Column('url', String(255)),
    Column('duration', Integer)
)

albums_table = Table(
    'albums', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('url', String(255)),
    Column('type', String(255)),
    Column('release_year', Integer)
)

artists_table = Table(
    'artists', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255))
)

genres_table = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255))
)

track_genres_table = Table(
    'track_genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('track_id', ForeignKey('tracks.id')),
    Column('genre_id', ForeignKey('genres.id'))
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255)),
    Column('password', String(255))
)

def map_model_to_tables():
    mapper(Track, tracks_table, properties={
        '_Track__track_id': tracks_table.c.id,
        '_Track__title': tracks_table.c.title,
        '_Track__track_url': tracks_table.c.url,
        '_Track__artist': relationship(Artist),
        '_Track__album': relationship(Album),
        '_Track__track_duration': tracks_table.c.duration,
        '_Track__genres': relationship(Genre, secondary=track_genres_table, back_populates='_Genre__users')

    })
    mapper(Album, albums_table, properties={
        '_Album__album_id': albums_table.c.id,
        '_Album__title': albums_table.c.title,
        '_Album__album_url': albums_table.c.url,
        '_Album__album_type': albums_table.c.type,
        '_Album__release_year': albums_table.c.release_year,
    })
    mapper(Artist, artists_table, properties={
        '_Artist__artist_id': artists_table.c.id,
        '_Artist__full_name': artists_table.c.name
    })
    mapper(Genre, genres_table, properties={
        '_Genre__genre_id': genres_table.c.id,
        '_Genre__name': genres_table.c.name,
        '_Genre__users': relationship(Track, secondary=track_genres_table, back_populates='_Track__genres')
    })
    mapper(User, users_table, properties={
        '_User__user_name': users_table.c.user_name,
        '_User__password': users_table.c.password,
    })


#new


# tracks_table = Table(
#     'tracks', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('title', String(255), nullable=False),
#     Column('artist', ForeignKey('artists.name')),
#     Column('album', ForeignKey('albums.title')),
#     Column('track_url', String(255), nullable=False),
# )
#
# albums_table = Table(
#     'albums', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('title', String(255), nullable=False),
#     Column('url', String(255), nullable=False),
#     Column('type', String(255), nullable=False),
# )
#
#
# artists_table = Table(
#     'artists', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('name', String(255), nullable=False)
# )
#
# genres_table = Table(
#     'genres', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('name', String(255), nullable=False)
# )
#
#
# users_table = Table(
#     'users', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('user_name', String(255), unique=True, nullable=False),
#     Column('password', String(255), nullable=False)
# )
#
#
# def map_model_to_tables():
#     mapper(Track, tracks_table, properties={
#         '_Track__track_id': tracks_table.c.id,
#         '_Track__title': tracks_table.c.title,
#         '_Track__track_url': tracks_table.c.url,
#         '_Track__artist': tracks_table.c.artists,
#         '_Track__album': tracks_table.c.album,
#         '_Track__track_duration': tracks_table.c.duration,
#
#     })
#     mapper(Album, albums_table, properties={
#         '_Album__album_id': albums_table.c.id,
#         '_Album__title': albums_table.c.title,
#         '_Album__album_url': albums_table.c.url,
#         '_Album__album_type': albums_table.c.type
#     })
#     mapper(Artist, artists_table, properties={
#         '_Artist__artist_id': artists_table.c.id,
#         '_Artist__full_name': artists_table.c.name
#     })
#     mapper(Genre, genres_table, properties={
#         '_Genre__genre_id': genres_table.c.id,
#         '_Genre__name': genres_table.c.name
#     })
#     mapper(User, users_table, properties={
#         '_User__user_name': users_table.c.user_name,
#         '_User__password': users_table.c.password,
#     })

#
#
#
#
#
