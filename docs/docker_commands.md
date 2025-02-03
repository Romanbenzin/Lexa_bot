# Переезд в докер:
- docker build -t bot .                           # Сделать образ на основе dockerfile
- docker ps                                       # Проверить запущенные контейнеры
- docker ps -a                                    # Проверить все контейнеры
- docker images                                   # Все контейнеры
- docker run -it bot                              # Запустить контейнер
- docker run -d --restart unless-stopped bot      # Запустить контейнер фоново
- docker stop 56e133d13904                        # Остановить контейнер по ID
- docker container prune                          # Удалить не запущенные контейнеры

# При обновлении:
1. из папки с ботом:
sudo docker build -t bot .
2. Проверить запущенные контейнеры:
sudo docker ps
3. Стопнуть контейнер по ID или Имени:
sudo docker stop ID
4. Проверить образы:
sudo docker image ls
5. Удалить старый образ:
sudo docker rmi ddf9f47f661d
6. Запустить бота:
sudo docker run -d --restart unless-stopped bot


# docker-compose
    docker-compose down -v                # оставить старые контейнеры
    docker-compose up -d                  # Запустить контейнеры
    docker ps                             # Проверить работу контейнеров

# Подключиться к базе в контейнере
    docker exec -it ff3c636d7116 psql -U postgres -d my_bot_db

# Подключиться к контейнеру
    docker exec -it ff3c636d7116 bash

# Перезапуск контейнеров
    docker-compose down -v
    docker-compose up -d

# Собрать образ
    docker-compose up --build -d

# Проверить логи у постгресс контейнера 
    docker logs 1ca95dde781d

# Почистить кеш в докере
    docker builder prune --all --force

# Проверить базу в докере
    docker exec -it 3e6d79b1d85e psql -U postgres -l

cp lexa_dump.sql 4181b65187c4:/lexa_dump.sql
docker exec -it 4181b65187c4 psql -U postgres -d my_bot_db -f /lexa_dump.sql

# Проверить доступность порта
docker exec -it lexa_bot-db-1 netstat -tuln | grep 5432