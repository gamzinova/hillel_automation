from Anna_Gamzinova.api_collections.configurations.config_file import BASE_URL, API_KEY
import requests
from os import path


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self._headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                         'Authorization': f'Bearer {API_KEY}'}
        self.__request = requests

    def get(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.get(path.join(self.__base_url, url), params=params, headers=headers)
        return response

    def post(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
            response = self.__request.post(path.join(self.__base_url, url), json=body, headers=headers, params=params)
            return response

    def delete(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
            response = self.__request.delete(path.join(self.__base_url, url), json=body, headers=headers, params=params)
            return response

    def patch(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
            response = self.__request.patch(path.join(self.__base_url, url), json=body, headers=headers, params=params)
            return response
