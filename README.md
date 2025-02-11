# Сейчас работает бот так, что в контейнере bot находится сам бот, а в контейнере db лежит psql

### После pull, нужно выполнить 2 команды
    git pull origin main    
    sudo docker-compose down -v
    sudo docker-compose up --build -d

### Запуск
Создать в корневой директории файл .env по аналогии с docs/example.env

### Пользование инструментами
- [systemctl](docs/systemctl.md)
- [GIT](docs/git_doc.md)
- [POSTGRESQL](docs/db_doc.md)
- [pyTelegramBotAPI](docs/telegram_bot_api.md)
- [DOCKER](docs/docker_commands.md)
- [MANUAL](docs/manual_commands.md)
- [.ENV](docs/example.env)
- [db_command]()