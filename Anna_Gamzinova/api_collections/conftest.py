import pytest
import json
from Anna_Gamzinova.api_collections.CONSTANTS import ROOT_DIR
from Anna_Gamzinova.api_collections.objects.people_collection import PeopleAPI
from Anna_Gamzinova.api_collections.utilities.configurations import Configurations


@pytest.fixture()
def env():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def delete_last_person():
    response = PeopleAPI().get_list_of_people()
    PeopleAPI().delete_person(person_id=response.json()[0]['id'])
