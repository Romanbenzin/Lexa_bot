# SQL
    postgresql-x64-15
    sudo service postgresql start

# Для кодировки в терминале:
    chcp 1251

# Подключиться к базе:
    psql -U postgres -d my_bot_db

# Создал базу:
    CREATE DATABASE my_bot_db;
# Переключился на базу:
    \c my_bot_db;
# Создал таблицу:
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        user_name TEXT NOT NULL,
        sucker BOOLEAN DEFAULT TRUE
    );

    CREATE TABLE purchases (
        id SERIAL PRIMARY KEY,
        user_ids TEXT NOT NULL,
        steam_link TEXT NOT NULL,
        purchase_date DATE NOT NULL
    );

# Таблицы:
    \dt
# Удалить таблицу:
    DROP TABLE users;

# Добавить столбец
    ALTER TABLE users ADD COLUMN "Sucker" BOOLEAN SET default TRUE;
    ALTER TABLE purchases ADD COLUMN purchase_date DATE;

# Добавить в таблицу:
    INSERT INTO users (user_name) VALUES ('@user_name');
    INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/3159330/Assassins_Creed_Shadows/', '2025-01-29');

# Запрос для даты покупки:
    SELECT id, user_ids, steam_link, TO_CHAR(purchase_date, 'YYYY-MM') AS purchase_month FROM purchases;

# Выбрать каждого, кто скидывался на игру
    SELECT *
    FROM users
    INNER JOIN purchases p ON users.id = ANY(string_to_array(p.user_ids, ',')::int[]);

# Снять дамп
    pg_dump -U postgres -h localhost -d my_bot_db --encoding=UTF8 -f lexa_dump.sql

# Отправить дамп на сервер
    scp C:\lexa_bot\Lexa_bot\lexa_dump.sql benzin@156.67.63.180:/home/benzin/Lexa_bot/lexa_dump.sql
