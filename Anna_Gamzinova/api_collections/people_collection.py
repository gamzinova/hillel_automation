import json
from os import path

from Anna_Gamzinova.api_collections.base_api import BaseAPI
from Anna_Gamzinova.api_collections.config_file import BASE_URL


class PeopleAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__person_url = 'public/v2/users'

    def get_person(self, person_id):
        return self.get(f'{self.__person_url}/{person_id}')

    def get_list_of_people(self):
        return self.get(f'{self.__person_url}')

    def create_person(self, person_data):
        json_data = json.dumps(person_data)
        response = self.post(url=f'{self.__person_url}', body=person_data)
        return response

    def delete_person(self, person_id):
        response = self.delete(url=path.join(self.__person_url, person_id))
        return response

    def update_person(self, person_id, person_data):
        response = self.patch(url=path.join(self.__person_url, person_id), body=person_data)
        return response
