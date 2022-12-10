import json

import psycopg2
import pytest
from Anna_Gamzinova.SQL_driver.CONSTANTS import ROOT_DIR

from Anna_Gamzinova.SQL_driver.utilities.configurations import Configurations


@pytest.fixture()
def env():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def create_connection(env):
    connection = psycopg2.connect(
        user=env.user,
        password=env.password,
        host=env.host,
        port=env.port,
        database=env.database
    )
    yield connection
    connection.close()
