"""Initialize Flask app."""
import os
import csv
from pathlib import Path

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool
from music.adapters.orm import metadata, map_model_to_tables
from music.adapters import databaserepository, repository_populate


from music.adapters.csvdatareader import TrackCSVReader
import music.adapters.repository as repo
import music.adapters.memoryrepository as memoryrepository
from music.adapters.memoryrepository import MemoryRepository, track_list, album_list, artist_list, genre_list, populate
from music.adapters.databaserepository import tracks_list, albums_list, artists_list, genres_list


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    if app.config['REPOSITORY'] == 'memory':
        dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        albums_file_name = os.path.join(dirname, 'music/adapters/data/raw_albums_excerpt.csv')
        tracks_file_name = os.path.join(dirname, 'music/adapters/data/raw_tracks_excerpt.csv')
        data = TrackCSVReader(albums_file_name, tracks_file_name)
        data.read_csv_files()
        tracks = data.dataset_of_tracks
        albums = data.dataset_of_albums
        artists = data.dataset_of_artists
        genres = data.dataset_of_genres

        repo.repo_instance = MemoryRepository()
        track_list(tracks, repo.repo_instance)
        album_list(albums, repo.repo_instance)
        artist_list(artists, repo.repo_instance)
        genre_list(genres, repo.repo_instance)

        memoryrepository.tracks_repo = repo.repo_instance.get_tracks()
        memoryrepository.albums_repo = repo.repo_instance.get_albums()
        memoryrepository.artists_repo = repo.repo_instance.get_artists()
        memoryrepository.genres_repo = repo.repo_instance.get_genres()

    elif app.config['REPOSITORY'] == "database":
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        database_echo = app.config['SQLALCHEMY_ECHO']
        database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                        echo=database_echo)
        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
        repo.repo_instance = databaserepository.SqlAlchemyRepository(session_factory)

        if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
            print("REPOPULATING DATABASE...")
            clear_mappers()
            metadata.create_all(database_engine)
            for table in reversed(metadata.sorted_tables):
                database_engine.execute(table.delete())
            map_model_to_tables()
            database_mode = True
            repository_populate.populate_for_database(data_path, repo.repo_instance)
            print("REPOPULATING DATABASE... FINISHED")
        else:
            map_model_to_tables()

            memoryrepository.tracks_repo = repo.repo_instance.get_tracks()
            memoryrepository.albums_repo = repo.repo_instance.get_albums()
            memoryrepository.artists_repo = repo.repo_instance.get_artists()
            memoryrepository.genres_repo = repo.repo_instance.get_genres()

    with app.app_context():
        from music.blueprints.track_blueprint import track_blueprint
        app.register_blueprint(track_blueprint)

        from music.blueprints.album_blueprint import album_blueprint
        app.register_blueprint(album_blueprint)

        from music.blueprints.artist_blueprint import artist_blueprint
        app.register_blueprint(artist_blueprint)

        from music.blueprints.genre_blueprint import genre_blueprint
        app.register_blueprint(genre_blueprint)

        from music.authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from music.home import home
        app.register_blueprint(home.home_blueprint)

        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, databaserepository.SqlAlchemyRepository):
                repo.repo_instance.reset_session()

        

    return app
