from datetime import datetime
from psycopg2 import Error
from bot.data_base.data_base_connect import connect_to_db, close_connection

def get_all_user_names():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users")
            users = cursor.fetchall()
            user_names = [user[0] for user in users]
            return user_names
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)
    else:
        print("Не удалось установить соединение с базой данных.")
        return []

def get_all_user_names_without_yana():
    """Функция для получения списка пользователей."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для получения данных
            cursor.execute("SELECT user_name FROM users WHERE sucker = True")
            users = cursor.fetchall()
            user_names = [user[0] for user in users]
            return user_names
        except Error as e:
            print(f"Ошибка при получении пользователей: {e}")
            return []
        finally:
            close_connection(connection)

def user_add(user_name, sucker=True):
    """Функция для добавления пользователя."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для добавления пользователя
            cursor.execute(
                "INSERT INTO users (user_name, sucker) VALUES (%s, %s);",
                (f"@{user_name}", sucker)
            )
            connection.commit()
            return f"Пользователь @{user_name} успешно добавлен."
        except Error as e:
            return f"Ошибка при добавлении пользователя: {e}"
        finally:
            close_connection(connection)
    else:
        return "Ошибка подключения к базе данных."


def user_delete(user_name):
    """Функция для удаления пользователя."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос для удаления пользователя
            cursor.execute("DELETE FROM users WHERE user_name = %s;", (f"@{user_name}",))
            connection.commit()

            # Проверяем, был ли пользователь удален
            if cursor.rowcount > 0:
                return f"Пользователь @{user_name} успешно удален."
            else:
                return f"Пользователь @{user_name} не найден в базе данных."
        except Error as e:
            return f"Ошибка при удалении пользователя: {e}"
        finally:
            close_connection(connection)
    else:
        return "Ошибка подключения к базе данных."

def game_add(user_ids, url_game):
    """Функция для добавления игры."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            current_date = datetime.now().strftime('%Y-%m-%d')

            # Убираем пробелы вокруг запятых в user_ids
            user_ids_clean = ",".join([uid.strip() for uid in user_ids.split(",")])

            cursor.execute(
                "INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES (%s, %s, %s);",
                (user_ids_clean, url_game, current_date)
            )
            connection.commit()

            return f"✅ Игра успешно добавлена: {url_game} для пользователей {user_ids_clean}."
        except Error as e:
            return f"❌ Ошибка при добавлении игры: {e}"
        finally:
            close_connection(connection)
    else:
        return "❌ Ошибка подключения к базе данных."

def game_get(user_name):
    """Функция для получения всех покупок пользователя."""
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # SQL-запрос: выбираем только steam_link и purchase_date
            cursor.execute(
                """
                SELECT p.steam_link, p.purchase_date
                FROM purchases p
                JOIN users u ON u.id::text = ANY(string_to_array(REGEXP_REPLACE(p.user_ids, '\s', '', 'g'), ','))
                WHERE u.user_name = %s
                ORDER BY p.purchase_date DESC;
                """,
                (user_name,)
            )
            results = cursor.fetchall()
            return results
        except Error as e:
            return f"Ошибка при получении данных: {e}"
        finally:
            close_connection(connection)
    else:
        return "Ошибка подключения к базе данных."
