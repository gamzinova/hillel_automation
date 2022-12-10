import psycopg2

from Anna_Gamzinova.SQL_driver.objects.base_repository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self._table_name = 'products'

    def create_table_products(self):
        try:
            self._cursor.execute(f"create table {self._table_name}(id serial primary key, name varchar(30), price float);")
        except psycopg2.errors.DuplicateTable:
            raise ValueError("DuplicateTable")

    def insert_values_into_products(self, values):
        args = ','.join(self._cursor.mogrify("(%s,%s)", value).decode('utf-8') for value in values)
        self._cursor.execute(f"insert into {self._table_name} (name, price) values" + args)

    def drop_table_products(self):
        try:
            self._cursor.execute(f"drop table {self._table_name} cascade;")
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")
