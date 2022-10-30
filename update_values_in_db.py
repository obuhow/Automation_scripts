from getpass import getpass
from mysql.connector import connect, Error

HOST = "localhost"
DATABASE = "tom"
TABLE = "modx_ms2_product_options"
USER = "admin"
PASSWORD = ""

def connect_to_db(query_func):
    def connection_func(*args, **kwargs):
        try:
            with connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE,
            ) as connection:
                with connection.cursor() as cursor:
                    query_func(cursor, *args, **kwargs)
                    connection.commit()
        except Error as e:
            print(e)
    return connection_func

@connect_to_db
def update_values_with_key(cursor, key, current_value, result_value)
    update_query = """
    UPDATE
        "%s"
    SET
        value = "%s"
    WHERE
        key = "%s" AND value = "%s"
    """ % (
        TABLE,
        result_value,
        key,
        current_value,
    )
    cursor.execute(update_query, multi=True)

@connect_to_db
def print_table_with_key(cursor, key):
    select_query = """
    SELECT *
    FROM "%s"
    WHERE
        key = "%s"
    """ % (
        TABLE,
        key,
    )
    for result in cursor.execute(select_query, multi=True):
        if result.with_rows:
            print(result.fetchall())

if __name__ = __main__:
    values = [("Начальный", "Начальный класс"),
              ("Средний", "Средний класс"),
              ("Высокий", "Высокий класс"),
              ("Экспертный", "Экспертный класс"),
              ("Премиальный", "Премиальный класс")]
    for current_value, result_value in values:
        update_values_with_key(KEY, current_value, result_value)
    print_table_with_key(KEY)


