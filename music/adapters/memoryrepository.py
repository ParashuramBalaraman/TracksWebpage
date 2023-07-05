
import csv
from pathlib import Path
from werkzeug.security import generate_password_hash
from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.track import Track
from music.domainmodel.track import Album
from music.domainmodel.track import Artist
from music.domainmodel.track import Genre
from music.domainmodel.user import User
from music.adapters.csvdatareader import TrackCSVReader


tracks_repo = None
albums_repo = None
artists_repo = None
genres_repo = None


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__tracks = list()
        self.__albums = list()
        self.__users = list()
        self.__artists = list()
        self.__genres = list()

    def add_track(self, track: Track):
        self.__tracks.append(track)

    def search_track(self, track_id):
        return next((track for track in self.__tracks if track.track_id == track_id), None)

    def add_user(self, user: User):
        self.__users.append(user)

    def search_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_album(self, album: Album):
        self.__albums.append(album)

    def search_album(self, album_id):
        return next((album for album in self.__albums if album.album_id == album_id), None)

    def add_artist(self, artist: Artist):
        self.__artists.append(artist)

    def search_artist(self, artist_id):
        return next((artist for artist in self.__artists if artist.artist_id == artist_id), None)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def search_genre(self, genre_id):
        return next((genre for genre in self.__genres if genre.genre_id == genre_id), None)

    def get_tracks(self):
        return self.__tracks

    def get_albums(self):
        return self.__albums

    def get_artists(self):
        return self.__artists

    def get_genres(self):
        return self.__genres

def track_list(tracks, repo : MemoryRepository):
    for track in tracks:
        repo.add_track(track)

def album_list(albums, repo : MemoryRepository):
    for album in albums:
        repo.add_album(album)

def artist_list(artists, repo : MemoryRepository):
    for artist in artists:
        repo.add_artist(artist)

def genre_list(genres, repo : MemoryRepository):
    for genre in genres:
        repo.add_genre(genre)

def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        # Read first line of the the CSV file.
        headers = next(reader)
        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row
def load_users_for_testing(data_path: Path, repo: MemoryRepository):
    users = dict()
    users_filename = str(Path(data_path) / "users.csv")
    for data_row in read_csv_file(users_filename):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users

def load_tracks_for_testing(data_path: Path, repo: MemoryRepository):
    tracks_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_test.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_test.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    tracks = data.dataset_of_tracks
    for track in tracks:
        repo.add_track(track)
        tracks_dict[track.track_id] = track
    return tracks_dict

def load_albums_for_testing(data_path: Path, repo: MemoryRepository):
    albums_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_test.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_test.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    albums = data.dataset_of_albums
    for album in albums:
        repo.add_album(album)
        albums_dict[album.album_id] = album
    return albums_dict

def load_artists_for_testing(data_path: Path, repo: MemoryRepository):
    artists_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_test.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_test.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    artists = data.dataset_of_artists
    for artist in artists:
        repo.add_artist(artist)
        artists_dict[artist.artist_id] = artist
    return artists_dict

def load_genres_for_testing(data_path: Path, repo: MemoryRepository):
    genres_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_test.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_test.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    genres = data.dataset_of_genres
    for genre in genres:
        repo.add_genre(genre)
        genres_dict[genre.genre_id] = genre
    return genres_dict


def populate(data_path: Path, repo: MemoryRepository):
    users = load_users_for_testing(data_path, repo)
    tracks = load_tracks_for_testing(data_path, repo)
    albums = load_albums_for_testing(data_path, repo)
    artists = load_artists_for_testing(data_path, repo)
    genres = load_genres_for_testing(data_path, repo)



