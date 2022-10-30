from getpass import getpass
from mysql.connector import connect, Error

HOST = "localhost"
DATABASE = "tom"
TABLE = "modx_ms2_product_options"
KEY = "class"
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
def update_values_with_key(cursor, key, current_value, result_value):
    update_query = f"""
    UPDATE
        `{TABLE}`
    SET
        `value` = "{result_value}"
    WHERE
        `key` = "{key}" AND `value` = "{current_value}"
    """
    cursor.execute(update_query, multi=True)

if __name__ == "__main__":
    values = [("Начальный", "Начальный класс"),
              ("Средний", "Средний класс"),
              ("Высокий", "Высокий класс"),
              ("Экспертный", "Экспертный класс"),
              ("Премиальный", "Премиальный класс")]
    for current_value, result_value in values:
        update_values_with_key(KEY, current_value, result_value)



