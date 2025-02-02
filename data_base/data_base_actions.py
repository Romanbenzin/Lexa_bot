from psycopg2 import Error
from data_base.data_base_connect import connect_to_db, close_connection

def get_all_uses_name():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users")
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)

def get_all_uses_name_without_yana():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users WHERE sucker = True")
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)