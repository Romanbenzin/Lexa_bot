# Проверить пользователей в базе:
    /db_user_get
    /db_user_add <имя_пользователя> <sucker (опционально, по умолчанию True)>
    /db_user_delete <имя_пользователя>

# Добавить новую игру в бота
    /db_add_game 'user_ids' https://store.steampowered.com/app/1693980/Dead_Space/
    /db_add_game '1,2,4' https://store.steampowered.com/app/1693980/Dead_Space/

# Узнать купленные игры у пользователя
    /db_get_game @user_name