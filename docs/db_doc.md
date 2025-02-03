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
INSERT INTO purchases (user_name) VALUES ('@user_name');

INSERT INTO purchases (user_ids, steam_link, purchase_month) VALUES ('1', 'https://store.steampowered.com/app/123', '2023-10');

Запрос для даты покупки:
SELECT id, user_ids, steam_link, TO_CHAR(purchase_date, 'YYYY-MM') AS purchase_month
FROM purchases;



INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/3159330/Assassins_Creed_Shadows/', '2025-01-29');
INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2', 'https://store.steampowered.com/app/1426210/It_Takes_Two/', '2025-01-29');
INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/2473480/Tails_of_Iron_2_Whiskers_of_Winter/', '2025-01-29');

INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/1608070/CRISIS_CORE_FINAL_FANTASY_VII_REUNION/', '2025-02-01');
INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/1551360/Forza_Horizon_5/', '2025-02-01');
INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/1373960/INDIKA/', '2025-02-01');
INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1, 2, 4', 'https://store.steampowered.com/app/534380/Dying_Light_2_Stay_Human_Reloaded_Edition/', '2025-02-01');

INSERT INTO purchases (user_ids, steam_link, purchase_date) VALUES ('1', 'https://store.steampowered.com/app/1062830/Embr/', '2025-02-02');


Снять дамп:
pg_dump -U ваш_пользователь -h ваш_хост -d ваша_база -F c -b -v -f ваш_дамп.sql

pg_dump -U postgres -h localhost -d my_bot_db -F c -b -v -f lexa_dump.sql

scp C:\lexa_bot\Lexa_bot\lexa_dump.sql benzin@156.67.63.180:/home/benzin/Lexa_bot

pg_restore -U postgres -h localhost -d my_bot_db -v lexa_dump.sql
