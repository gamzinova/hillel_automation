from http import HTTPStatus

import requests


from Anna_Gamzinova.api_collections.people_collection import PeopleAPI


def test_get_person_200():
    response = PeopleAPI().get_person(1)
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_get_people_200():
    response = PeopleAPI().get_list_of_people()
    print(response.content)
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_create_person():
    new_user = {
        "name": "Nelson",
        "gender": "female",
        "email": "nchanukaissoon@gmail.com",
        "status": "active"}
    response = PeopleAPI().create_person(new_user)
    assert response.status_code == HTTPStatus.CREATED, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.CREATED}'


def test_create_existing_person():
    existing_user = {
        "name": "Nelson",
        "gender": "female",
        "email": "nchanukaissoon@gmail.com",
        "status": "active"}
    response = PeopleAPI().create_person(existing_user)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.UNPROCESSABLE_ENTITY}'


def test_delete_existing_person():
    response = PeopleAPI().delete_person(person_id='6934')
    assert response.status_code == HTTPStatus.NO_CONTENT, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NO_CONTENT}'


def test_delete_non_existing_person():
    response = PeopleAPI().delete_person(person_id='6934')
    assert response.status_code == HTTPStatus.NO_CONTENT, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NO_CONTENT}'


def test_update_existing_person():
    update_user = {
        "name": "Nelson",
        "gender": "female",
        "email": "nchanukaissoon@gmail.com",
        "status": "active"}
    response = PeopleAPI().update_person(person_id='6925', person_data=update_user)
    assert response.status_code == HTTPStatus.OK, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.OK}'


# def test_get_people_2001():
#     response = get('https://gorest.co.in/public/v2/users')
#     assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
#                                                   f'\nExpected: {HTTPStatus.OK}'

def test_get_people_2002():
    response = requests.post('https://gorest.co.in/public/v2/users', params=dictionary)
    assert response.status_code == HTTPStatus.CREATED, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                       f'\nExpected: {HTTPStatus.CREATED}'
