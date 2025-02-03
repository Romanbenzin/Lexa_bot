# Обновить ветку из папки Lexa_bot
git pull origin main

# Если потерялся гит
git remote add origin https://github.com/Romanbenzin/Lexa_bot.git

# Удалены файлы, перечисленные в .gitignore
git rm -r --cached .
git add .
git commit -m

# Удалить из отслеживания гитом файлы
git rm --cached .\pass_bot.py
git rm --cached .\draft.py

