import requests

base_url = 'https://reqres.in/api'


def test_list_users():
    page = 2

    response = requests.get(f'{base_url}/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page


def test_single_users():
    first_name = "Janet"
    last_name = "Weaver"

    response = requests.get(f'{base_url}/users/2')

    assert response.status_code == 200
    assert response.json()['data']['first_name'] == first_name
    assert response.json()['data']['last_name'] == last_name


def test_unknown_users():
    per_page = 6

    response = requests.get(f'{base_url}/unknown')

    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page

def test_user_not_found():
    result = {}

    response = requests.get(f'{base_url}/unknown/23')

    assert response.status_code == 404
    assert response.text == '{}'


def test_create_user():
    name = 'An'
    job = 'student'

    response = requests.post(
        url = f'{base_url}/users',
        json={
           'name': name,
            'job': job
        }
    )

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job

def test_delete_user():
    response = requests.delete(f'{base_url}/users/2')

    assert response.status_code == 204


def test_patch():
    name = 'An'
    job = 'student'

    response = requests.patch(
        url=f'{base_url}/users/2',
        json={
            'name': name,
            'job': job
        }
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job

def test_put():
    name = 'An'
    job = 'student'

    response = requests.put(
        url=f'{base_url}/users/2',
        json={
            'name': name,
            'job': job
        }
    )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job

def test_successful_register():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = requests.post(
        url = f'{base_url}/register',
        json = {
            'email': email,
            'password': password
    })

    assert response.status_code == 200

def test_successful_loin():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    response = requests.post(
        url=f'{base_url}/login',
        json={
            'email': email,
            'password': password
        })

    assert response.status_code == 200
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
