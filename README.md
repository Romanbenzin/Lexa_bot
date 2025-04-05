### Настроен ci/cd. Так же делается backup базы данных при деплое в папку database_old

### После pull, нужно выполнить 2 команды
    git pull origin main    
    sudo docker-compose down -v
    sudo docker-compose up --build -d

### Дамп. Нужно создать том
    docker volume create postgres_data

### Проверить, что используются данные из дампа
    docker exec -it db psql -U postgres -d my_bot_db -c "SELECT COUNT(*) FROM purchases;"

# Посмотреть логи:
    docker-compose logs -f api

### Запуск
    Создать в корневой директории файл .env по аналогии с docs/example.env

### Пользование инструментами
- [systemctl](docs/systemctl.md)
- [GIT](docs/git_doc.md)
- [POSTGRESQL](docs/db_doc.md)
- [pyTelegramBotAPI](docs/telegram_bot_api.md)
- [DOCKER](docs/docker_commands.md)
- [MANUAL](docs/manual_commands.md)
- [db_command](docs/bot_db_command.md)
- [.ENV](docs/example.env)