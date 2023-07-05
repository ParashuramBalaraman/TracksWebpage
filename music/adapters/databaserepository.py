from sqlalchemy import desc, asc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session

from music.domainmodel.track import Album
from music.domainmodel.track import Artist
from music.domainmodel.track import Genre
from music.domainmodel.user import User
from music.domainmodel.track import Track
from music.adapters.repository import AbstractRepository



class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_track(self, track: Track):
        with self._session_cm as scm:
            scm.session.merge(track)
            scm.commit()

    def search_track(self, track_id):
        track = None
        try:
            track = self._session_cm.session.query(Track).filter(Track._Track__track_id == track_id).one()
        except NoResultFound:
            pass
        return track

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.merge(user)
            scm.commit()

    def search_user(self, user_name):
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._User__user_name == user_name).one()
        except NoResultFound:
            pass
        return user

    def add_album(self, album: Album):
        with self._session_cm as scm:
            scm.session.merge(album)
            scm.commit()

    def search_album(self, album_id):
        album = None
        try:
            album = self._session_cm.session.query(Album).filter(Album._Album__album_id == album_id).one()
        except NoResultFound:
            pass
        return album

    def add_artist(self, artist: Artist):
        with self._session_cm as scm:
            scm.session.merge(artist)
            scm.commit()

    def search_artist(self, artist_id):
        artist = None
        try:
            artist = self._session_cm.session.query(Artist).filter(Artist._Artist__artist_id == artist_id).one()
        except NoResultFound:
            pass
        return artist

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.merge(genre)
            scm.commit()

    def search_genre(self, genre_id):
        genre = None
        try:
            genre = self._session_cm.session.query(Genre).filter(Genre._Genre__genre_id == genre_id).one()
        except NoResultFound:
            pass
        return genre

    def get_tracks(self):
        tracks = self._session_cm.session.query(Track).all()
        return tracks

    def get_albums(self):
        albums = self._session_cm.session.query(Album).all()
        return albums

    def get_artists(self):
        artists = self._session_cm.session.query(Artist).all()
        return artists

    def get_genres(self):
        genres = self._session_cm.session.query(Genre).all()
        return genres

def tracks_list(tracks, repo : SqlAlchemyRepository):
    for track in tracks:
        repo.add_track(track)

def albums_list(albums, repo : SqlAlchemyRepository):
    for album in albums:
        repo.add_album(album)

def artists_list(artists, repo : SqlAlchemyRepository):
    for artist in artists:
        repo.add_artist(artist)

def genres_list(genres, repo : SqlAlchemyRepository):
    for genre in genres:
        repo.add_genre(genre)