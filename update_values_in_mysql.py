from mysql.connector import connect, Error

# Конфигурация подключения к базе данных MySQL
config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 8889,
  'database': 'db_1',
  'raise_on_warnings': True
}

def update_values_with_key(cursor):
    sql = "SELECT * FROM `b_iblock_element`"
    cursor.execute(sql)

if __name__ == "__main__":
    # Подключение к базе данных MySQL
    try:
        with connect(**config) as connection:
            # Пример использования: выполнение запроса к базе данных
            with connection.cursor() as cursor:
                update_values_with_key(cursor)
                result = cursor.fetchall()
                print("Success")
                for row in result:
                    print(row)
                # Закрытие соединения с базой данных
                connection.close()
    except Error as e:
        print(e)



