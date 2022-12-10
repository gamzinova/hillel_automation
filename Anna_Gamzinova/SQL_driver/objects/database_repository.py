import psycopg2

from Anna_Gamzinova.SQL_driver.objects.base_repository import BaseRepository


class DatabaseRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self._products_table_name = "products"
        self._orders_table_name = "orders"

    def create_table_orders(self):
        try:
            self._cursor.execute(
                f"create table {self._orders_table_name}(id serial primary key, product_id int,quantity int, "
                f"constraint fk_product_id foreign key (product_id) references {self._products_table_name}(id));")
        except psycopg2.errors.DuplicateTable:
            raise ValueError("DuplicateTable")

    def my_request(self):
        self._cursor.execute(
            f'select {self._products_table_name}.name,{self._products_table_name}.price,{self._orders_table_name}.quantity,{self._products_table_name}.price * '
            f'{self._orders_table_name}.quantity as total from {self._products_table_name} inner join {self._orders_table_name} on {self._products_table_name}.id = '
            f'{self._orders_table_name}.product_id;')
        return self._cursor.fetchall()

    def get_all_orders(self):
        try:
            self._cursor.execute(f'select * from {self._orders_table_name};')
            return self._cursor.fetchall()
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")

