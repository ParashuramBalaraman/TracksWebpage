from sqlalchemy import select, inspect

from music.adapters.orm import metadata

def test_database_populate_inspect_table_names(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['albums', 'artists', 'genres', 'track_genres', 'tracks', 'users']

def test_database_populate_select_all_users(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_users_table = inspector.get_table_names()[5]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_users_table]])
        result = connection.execute(select_statement)

        all_users = []
        for row in result:
            all_users.append(row['user_name'])

        assert all_users == ['thorke', 'fmercury']

def test_database_populate_select_all_tracks(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_tracks_table = inspector.get_table_names()[4]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_tracks_table]])
        result = connection.execute(select_statement)

        all_tracks = []
        for row in result:
            all_tracks.append((row['id'], row['title']))

        assert len(all_tracks) == 2000

def test_database_populate_select_all_albums(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_albums_table = inspector.get_table_names()[0]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_albums_table]])
        result = connection.execute(select_statement)

        all_albums = []
        for row in result:
            all_albums.append((row['id'], row['title']))

        assert len(all_albums) == 427

def test_database_populate_select_all_artist(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_artist_table = inspector.get_table_names()[1]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_artist_table]])
        result = connection.execute(select_statement)

        all_artist = []
        for row in result:
            all_artist.append((row['id'], row['name']))

        assert len(all_artist) == 263



def test_database_populate_select_all_genre(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_genre_table = inspector.get_table_names()[2]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_genre_table]])
        result = connection.execute(select_statement)

        all_genre = []
        for row in result:
            all_genre.append((row['id'], row['name']))

        assert len(all_genre) == 60