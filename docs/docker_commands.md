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