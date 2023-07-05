import pytest
from flask import Flask, session, request, url_for

#pass
def test_register(client):
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    response = client.post(
        '/authentication/register',
        data={'user_name': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers.get('Location') == '/authentication/login'

#pass
@pytest.mark.parametrize(('user_name', 'password', 'message'), (
        ('', '', b'Your user name is required'),
        ('cj', '', b'Your user name is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test', b'Your password must be at least 8 characters, and contain an upper case letter,\
            a lower case letter and a digit'),
        ('fmercury', 'Test#6^0', b'Your user name is already taken - please supply another'),
))
def test_register_with_invalid_input(client, user_name, password, message):
    # Check that attempting to register with invalid combinations of user name and password generate appropriate error
    # messages.

    response1 = client.post('/authentication/register', data={'user_name':'fmercury', 'password':'Test#6^0'})

    response = client.post(
        '/authentication/register',
        data={'user_name': user_name, 'password': password}
    )
    assert message in response.data

#pass
def test_login(client):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200
    response1 = client.post('/authentication/register', data={'user_name': 'fmercury', 'password': 'Test#6^0'})
    response2 = client.post('/authentication/login', data={'user_name': 'fmercury', 'password': 'Test#6^0'})
    assert response2.headers.get('Location') == '/'

#pass
def test_logout(client):
    response1 = client.post('/authentication/register', data={'user_name': 'fmercury', 'password': 'Test#6^0'})
    response2 = client.post('/authentication/login', data={'user_name': 'fmercury', 'password': 'Test#6^0'})
    response3 = client.get('/authentication/logout')
    assert response3.headers.get('Location') == '/'

#albums
#pass
def test_search_albums(client):
    respone1 = client.post('/find_album', data={'album':'Niris'}).status_code
    respone2 = client.post('/find_album', data={'album': 'Niris'})
    assert respone1 == 302
    assert respone2.headers.get('Location') == '/albums/Niris'

#pass
def test_search_no_album(client):
    respone1 = client.get('/find_album', data={'album': 'chicken_little'})
    assert b'chicken_little.' not in respone1.data

#pass
def test_list_of_albums(client):
    response1 = client.get('/albums')
    assert b'AWOL - A Way Of Life' in response1.data
    assert b'Niris' in response1.data
    assert b'Constant Hitmaker' in response1.data


#artist
#pass
def test_search_artist(client):
    respone1 = client.post('/find_artist', data={'artist':'AWOL'}).status_code
    respone2 = client.post('/find_artist', data={'artist': 'AWOL'})
    assert respone1 == 302
    assert respone2.headers.get('Location') == '/artists/AWOL'

#pass
def test_search_no_artist(client):
    respone1 = client.get('/find_artist', data={'artist':'Overwatch'})
    assert b'Overwatch' not in respone1.data

#pass
def test_list_of_artists(client):
    response1 = client.get('/artists')
    assert b'AWOL' in response1.data
    assert b'Nicky Cook' in response1.data
    assert b'Kurt Vile' in response1.data

#track
#pass
def test_search_track(client):
    respone1 = client.post('/find_track', data={'track':'Food'}).status_code
    respone2 = client.post('/find_track', data={'track': 'Food'})
    assert respone1 == 302
    assert respone2.headers.get('Location') == '/tracks/Food'

#pass
def test_search_no_track(client):
    respone1 = client.get('/find_track', data={'track':'Nba2k23'})
    assert b'Nba2k23' not in respone1.data

#pass
def test_list_of_track(client):
    response1 = client.get('/tracks')
    assert b'Food' in response1.data
    assert b'Electric Ave' in response1.data
    assert b'This World' in response1.data

#genre
def test_search_genre(client):
    respone1 = client.post('/find_genre', data={'genre':'Avant-Garde'}).status_code
    respone2 = client.post('/find_genre', data={'genre': 'Avant-Garde'})
    assert respone1 == 302
    assert respone2.headers.get('Location') == '/genres/Avant-Garde'

#pass
def test_search_no_genre(client):
    respone1 = client.get('/find_genre', data={'genre':'Mickey Mouse'})
    assert b'Mickey Mouse' not in respone1.data

def test_list_of_genre(client):
    response1 = client.get('/genres')
    assert b'Avant-Garde' in response1.data
    assert b'International' in response1.data
    assert b'Blues' in response1.data



















