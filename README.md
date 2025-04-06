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
- [systemctl](bot/docs/systemctl.md)
- [GIT](bot/docs/git_doc.md)
- [POSTGRESQL](bot/docs/db_doc.md)
- [pyTelegramBotAPI](bot/docs/telegram_bot_api.md)
- [DOCKER](bot/docs/docker_commands.md)
- [MANUAL](bot/docs/manual_commands.md)
- [db_command](bot/docs/bot_db_command.md)
- [.ENV](bot/docs/example.env)