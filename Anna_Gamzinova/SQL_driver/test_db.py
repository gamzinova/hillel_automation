import pytest
from Anna_Gamzinova.SQL_driver.objects.database_repository import DatabaseRepository
from Anna_Gamzinova.SQL_driver.objects.orders_repository import OrdersRepository
from Anna_Gamzinova.SQL_driver.objects.products_repository import ProductsRepository


def test_del_products(create_connection):
    product_repository = ProductsRepository(create_connection)
    with pytest.raises(Exception) as exc:
        product_repository.drop_table_products()
        product_repository.get_all()
    assert str(exc.value) == 'UndefinedTable'


def test_create_products(create_connection):
    product_repository = ProductsRepository(create_connection)
    product_repository.create_table_products()
    assert type(product_repository.get_all()) is list


def test_create_2n_products(create_connection):
    product_repository = ProductsRepository(create_connection)
    with pytest.raises(Exception) as exc:
        product_repository.create_table_products()
    assert str(exc.value) == 'DuplicateTable'


def test_del_orders(create_connection):
    orders_repository = OrdersRepository(create_connection)
    with pytest.raises(Exception) as exc:
        orders_repository.drop_table_orders()
        orders_repository.get_all()
    assert str(exc.value) == 'UndefinedTable'


def test_create_orders(create_connection):
    database_repository = DatabaseRepository(create_connection)
    database_repository.create_table_orders()
    assert type(database_repository.get_all_orders()) is list


def test_create_2n_orders(create_connection):
    database_repository = DatabaseRepository(create_connection)
    with pytest.raises(Exception) as exc:
        database_repository.create_table_orders()
    assert str(exc.value) == 'DuplicateTable'


def test_add_items_into_products(create_connection):
    product_repository = ProductsRepository(create_connection)
    products = [('tshirt', 49.50), ('trousers', 119.80), ('sweater', 100), ('shoes', 150), ('dress', 80)]
    product_repository.insert_values_into_products(products)
    assert type(product_repository.get_all()) is list


def test_add_items_into_orders(create_connection):
    orders_repository = OrdersRepository(create_connection)
    orders = [(1, 3), (2, 5), (3, 5), (4, 1), (5, 2)]
    orders_repository.insert_values_into_orders(orders)
    assert type(orders_repository.get_all()) is list


def test_join_to_receive_total(create_connection):
    database_repository = DatabaseRepository(create_connection)
    assert type(database_repository.my_request()) is list


def test_get_all_products(create_connection):
    product_repository = ProductsRepository(create_connection)
    assert type(product_repository.get_all()) is list
