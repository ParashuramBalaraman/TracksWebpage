import pytest

from music import create_app
from music.adapters import memoryrepository, repository_populate


from utils import get_project_root

# the csv files in the test folder are different from the csv files in the covid/adapters/data folder!
# tests are written against the csv files in tests, this data path is used to override default path for testing
TEST_DATA_PATH = get_project_root() / "tests" / "data"


@pytest.fixture
def in_memory_repo():
    repo = memoryrepository.MemoryRepository()
    database_mode = False
    repository_populate.populate_for_database(TEST_DATA_PATH, repo, database_mode)
    return repo





# @pytest.fxture
# def client():
#     my_app = create_app({
#         'TESTING': True,                                # Set to True during testing.
#         'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
#         'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
#     })
#
#     return my_app.test_client()


@pytest.fixture()
def app():
    app = create_app({
        'TESTING': True,  # Set to True during testing.
        'REPOSITORY': 'memory',
        'TEST_DATA_PATH': TEST_DATA_PATH,  # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False  # test_client will not send a CSRF token, so disable validation.
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()




