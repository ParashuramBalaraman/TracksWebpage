import csv
from pathlib import Path

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository
from music.domainmodel.user import User
from music.domainmodel.artist import Artist
from music.domainmodel.album import Album
from music.adapters.csvdatareader import TrackCSVReader



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


def load_users(data_path: Path, repo: AbstractRepository):
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

#if u see this u are on the latest one!
def load_tracks(data_path: Path, repo: AbstractRepository):
    tracks_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_excerpt.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_excerpt.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    tracks = data.dataset_of_tracks #list
    for track in tracks:
        repo.add_track(track)
        tracks_dict[track.track_id] = track
    return tracks_dict


def load_albums(data_path: Path, repo: AbstractRepository):
    albums_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_excerpt.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_excerpt.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    albums = data.dataset_of_albums
    for album in albums:
        repo.add_album(album)
        albums_dict[album.album_id] = album
    return albums_dict


def load_artists(data_path: Path, repo: AbstractRepository):
    artists_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_excerpt.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_excerpt.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    artists = data.dataset_of_artists
    for artist in artists:
        repo.add_artist(artist)
        artists_dict[artist.artist_id] = artist
    return artists_dict


def load_genres(data_path: Path, repo: AbstractRepository):
    genres_dict = dict()
    test_album_file_name = str(Path(data_path) / "raw_albums_excerpt.csv")
    test_track_file_name = str(Path(data_path) / "raw_tracks_excerpt.csv")
    data = TrackCSVReader(test_album_file_name, test_track_file_name)
    data.read_csv_files()
    genres = data.dataset_of_genres
    for genre in genres:
        repo.add_genre(genre)
        genres_dict[genre.genre_id] = genre
    return genres_dict

