import json
from http import HTTPStatus

from Anna_Gamzinova.api_collections.conftest import delete_last_person
from Anna_Gamzinova.api_collections.objects.people_collection import PeopleAPI
from Anna_Gamzinova.api_collections.objects.person import Person


def test_get_person_200():
    response = PeopleAPI().get_person(300)
    print(response.json())
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_get_people_200():
    response = PeopleAPI().get_list_of_people()
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_create_person(delete_last_person, env):
    delete_last_person
    new_user = Person(env.name1, env.gender1, env.email1, env.status)
    response = PeopleAPI().create_person(new_user.get_dict())
    assert response.status_code == HTTPStatus.CREATED, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.CREATED}'


def test_create_person_name_check(delete_last_person, env):
    """
    A test checks that the user ws created with the requested name
    """
    delete_last_person
    new_user = Person(env.name1, env.gender1, env.email1, env.status)
    response = PeopleAPI().create_person(new_user.get_dict())
    person_values = response.json().values()
    user_value = new_user.get_dict().values()
    assert list(user_value)[1] in person_values, \
        f'A user was created with a wrong name'


def test_create_existing_person(env):
    existing_user = Person(env.name1, env.gender1, env.email1, env.status)
    response = PeopleAPI().create_person(existing_user.get_dict())
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.UNPROCESSABLE_ENTITY}'


def test_delete_existing_person():
    response = PeopleAPI().get_list_of_people()
    response = PeopleAPI().delete_person(person_id=response.json()[0]['id'])
    assert response.status_code == HTTPStatus.NO_CONTENT, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NO_CONTENT}'


def test_delete_non_existing_person():
    response = PeopleAPI().delete_person(person_id=2747000000)
    assert response.status_code == HTTPStatus.NOT_FOUND, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NOT_FOUND}'


def test_update_existing_person():
    update_user = {
        "name": "Flanders",
        "gender": "male",
        "email": "yesiamflanders@gmail.com",
        "status": "active"}
    response = PeopleAPI().get_list_of_people()
    response = PeopleAPI().update_person(person_id=response.json()[0]['id'], person_data=update_user)
    assert response.status_code == HTTPStatus.OK, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.OK}'


def test_update_non_existing_person():
    update_user = {
        "name": "Nelson",
        "gender": "male",
        "email": "haha@gmail.com",
        "status": "active"}
    response = PeopleAPI().update_person(person_id=2747000000, person_data=update_user)
    assert response.status_code == HTTPStatus.NOT_FOUND, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NOT_FOUND}'


def test_keys():
    response = PeopleAPI().get_list_of_people()
    person_keys = response.json()[0].keys()
    dict_keys = {'id': '', 'name': '', 'email': '', 'gender': '', 'status': ''}
    assert person_keys == dict.keys(dict_keys), f'Dictionary keys are incorrect'
