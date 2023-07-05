from music.domainmodel.user import User
from music.domainmodel.track import Track
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from typing import List
from typing import List

#user
#pass
def test_repository_can_add_a_user(in_memory_repo):
    user = User('dave', '123456789')
    in_memory_repo.add_user(user)
    assert in_memory_repo.search_user('dave') is user

#pass
def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.search_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')

#pass
def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.search_user('prince')
    assert user is None

#track
#pass
def test_repository_can_add_a_track(in_memory_repo):
    track = Track(504, "testing, track")
    in_memory_repo.add_track(track)
    assert in_memory_repo.search_track(504) is track

#pass
def test_repository_can_retrieve_a_track(in_memory_repo):
    track = in_memory_repo.search_track(2)
    assert track == Track(2, "Food")

#pass
def test_repository_does_not_retreive_a_non_existent_track(in_memory_repo):
    track = in_memory_repo.search_track(500)
    assert track is None

#pass
def test_repository_can_get_correct_amounts_of_tracks(in_memory_repo):
    numbers_of_tracks = in_memory_repo.get_tracks()
    assert len(numbers_of_tracks) == 10


#album
#pass
def test_repository_can_add_a_album(in_memory_repo):
    album = Album(599, "Hello Worls")
    in_memory_repo.add_album(album)
    assert in_memory_repo.search_album(599) is album

def test_repository_can_retrieve_a_album(in_memory_repo):
    album = in_memory_repo.search_album(1)
    assert album == Album(1, "AWOL - A Way Of Life")

def test_repository_does_not_retreive_a_non_existent_album(in_memory_repo):
    album = in_memory_repo.search_album(70)
    assert album is None

def test_repository_can_get_correct_amounts_of_albums(in_memory_repo):
    numbers_of_albums = in_memory_repo.get_albums()
    assert len(numbers_of_albums) == 5

#artist
#pass
def test_repository_can_add_a_artist(in_memory_repo):
    artist = Artist(599, "NLE Choppa")
    in_memory_repo.add_artist(artist)
    assert in_memory_repo.search_artist(599) is artist

#pass
def test_repository_can_retrieve_a_artist(in_memory_repo):
    artist = in_memory_repo.search_artist(1)
    assert artist == Artist(1, "AWOL")

#pass
def test_repository_does_not_retreive_a_non_existent_artist(in_memory_repo):
    artist = in_memory_repo.search_artist(70)
    assert artist is None

def test_repository_can_get_correct_amounts_of_artist(in_memory_repo):
    numbers_of_artists = in_memory_repo.get_artists()
    assert len(numbers_of_artists) == 5

#genres
#pass
def test_repository_can_add_a_genre(in_memory_repo):
    genre = Genre(560, "Heavy-Metal")
    in_memory_repo.add_genre(genre)
    assert in_memory_repo.search_genre(560) is genre

#pass
def test_repository_can_retrieve_a_genre(in_memory_repo):
    genre = in_memory_repo.search_genre(21)
    assert genre == Genre(21, "Hip-Hop")

#pass
def test_repository_does_not_retreive_a_non_existent_genre(in_memory_repo):
    genre = in_memory_repo.search_genre(500)
    assert genre is None

def test_repository_can_get_correct_amounts_of_genres(in_memory_repo):
    numbers_of_genres = in_memory_repo.get_genres()
    assert len(numbers_of_genres) == 7