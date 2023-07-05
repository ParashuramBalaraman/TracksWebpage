import csv, abc
from pathlib import Path
from datetime import date, datetime
from typing import List
from bisect import bisect, bisect_left, insort_left
from music.domainmodel.track import Album
from music.domainmodel.track import Artist
from music.domainmodel.track import Genre
from music.domainmodel.user import User
from music.domainmodel.track import Track


repo_instance = None

class RepositoryException(Exception):
    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_track(self, track: Track):
        raise NotImplementedError


    @abc.abstractmethod
    def search_track(self, track_id):
        raise NotImplementedError


    @abc.abstractmethod
    def add_album(self, album: Album):
        raise NotImplementedError

    @abc.abstractmethod
    def search_album(self, album_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_artist(self, artist: Artist):
        raise NotImplementedError

    @abc.abstractmethod
    def search_artist(self, artist_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def search_user(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def search_genre(self, genre_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_albums(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artists(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self):
        raise NotImplementedError









