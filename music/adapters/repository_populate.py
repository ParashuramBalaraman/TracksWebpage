from pathlib import Path
from music.adapters.repository import AbstractRepository
from music.adapters.csv_data_importer import load_users, load_genres, load_tracks, load_artists, load_albums



def populate_for_database(data_path: Path, repo: AbstractRepository):
    users = load_users(data_path, repo)
    tracks = load_tracks(data_path, repo)
    albums = load_albums(data_path, repo)
    artists = load_artists(data_path, repo)
    genres = load_genres(data_path, repo)
