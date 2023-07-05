from datetime import date, datetime

import pytest

import music.adapters.repository as repo
from music.adapters.databaserepository import SqlAlchemyRepository
from music.domainmodel.user import User
from music.domainmodel.track import Track
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.adapters.repository import RepositoryException

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#user
def test_repository_can_add_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = User('Dave', '123456789')
    repo.add_user(user)
    repo.add_user(User('Martin', '123456789'))
    user2 = repo.search_user('Dave')

    assert user2 == user

def test_repository_can_retrieve_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = repo.search_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')

def test_repository_does_not_retrieve_a_non_existent_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = repo.search_user('prince')
    assert user is None

#track
def test_repository_can_add_a_track(session_factory):
    repo= SqlAlchemyRepository(session_factory)
    track = Track(566, 'Haha')
    repo.add_track(track)
    testing_track = repo.search_track(566)
    assert testing_track == track

def test_repository_can_retrieve_a_track(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    track = repo.search_track(2)
    assert track == Track(2, 'Food')

def test_repository_does_not_retrieve_a_non_existent_track(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    track = repo.search_track(1)
    assert track is None

#album
def test_repository_can_add_a_album(session_factory):
    repo= SqlAlchemyRepository(session_factory)
    album = Album(2, 'mickey mouse')
    repo.add_album(album)
    testing_album = repo.search_album(2)
    assert testing_album == album

def test_repository_can_retrieve_a_album(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    album = repo.search_album(1)
    assert album == Album(1, 'AWOL - A Way Of Life')

def test_repository_does_not_retrieve_a_non_existent_album(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    album = repo.search_album(2)
    assert album is None

#artist
def test_repository_can_add_a_artist(session_factory):
    repo= SqlAlchemyRepository(session_factory)
    artist = Artist(2, 'winston')
    repo.add_artist(artist)
    testing_artist = repo.search_artist(2)
    assert testing_artist == artist

def test_repository_can_retrieve_a_artist(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    artist = repo.search_artist(1)
    assert artist == Artist(1, 'AWOL')

def test_repository_does_not_retrieve_a_non_existent_artist(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    album = repo.search_album(2)
    assert album is None

#genre
def test_repository_can_add_a_genre(session_factory):
    repo= SqlAlchemyRepository(session_factory)
    genre = Genre(6, 'r and b')
    repo.add_genre(genre)
    testing_genre = repo.search_genre(6)
    assert testing_genre == genre

def test_repository_can_retrieve_a_genre(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    genre = repo.search_genre(1)
    assert genre == Genre(1, 'Avant-Garde')

def test_repository_does_not_retrieve_a_non_existent_genre(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    genre = repo.search_genre(500)
    assert genre is None

