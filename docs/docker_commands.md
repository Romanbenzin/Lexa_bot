### Переезд в докер:
    docker build -t bot .                           # Сделать образ на основе dockerfile
    docker ps                                       # Проверить запущенные контейнеры
    docker ps -a                                    # Проверить все контейнеры
    docker images                                   # Все контейнеры
    docker run -it bot                              # Запустить контейнер
    docker run -d --restart unless-stopped bot      # Запустить контейнер фоново
    docker stop 56e133d13904                        # Остановить контейнер по ID
    docker container prune                          # Удалить не запущенные контейнеры

### При обновлении:
# из папки с ботом:
    sudo docker build -t bot .
# Проверить запущенные контейнеры:
    sudo docker ps
# Стопнуть контейнер по ID или Имени:
    sudo docker stop ID
# Проверить образы:
    sudo docker image ls
# Удалить контейнеры:
    sudo docker container prune
# Удалить старый образ:
    sudo docker rmi ddf9f47f661d
# Запустить бота:
    sudo docker run -d --restart unless-stopped bot

# docker-compose
    sudo docker-compose down -v                # оставить старые контейнеры
    sudo docker-compose up -d                  # Запустить контейнеры
    sudo docker ps                             # Проверить работу контейнеров

# Подключиться к базе в контейнере
    sudo docker exec -it ff3c636d7116 psql -U postgres -d my_bot_db

# Подключиться к контейнеру
    sudo docker exec -it ff3c636d7116 bash

# Перезапуск контейнеров
    sudo docker-compose down -v
    sudo docker-compose up -d

# Собрать образ
    sudo docker-compose up --build -d

# Проверить логи у постгресс контейнера 
    sudo docker logs 1ca95dde781d

# Почистить кеш в докере
    docker builder prune --all --force

# Проверить базу в докере
    docker exec -it 3e6d79b1d85e psql -U postgres -l

# Проверить доступность порта
    docker exec -it lexa_bot-db-1 netstat -tuln | grep 5432
