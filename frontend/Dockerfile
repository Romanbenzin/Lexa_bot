# Используем легковесный образ Nginx для раздачи статики
FROM nginx:alpine

# Копируем HTML, CSS и JS файлы в папку Nginx
COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Если у вас есть отдельные CSS/JS:
# COPY style.css /usr/share/nginx/html/
# COPY app.js /usr/share/nginx/html/

# Открываем порт 80 (по умолчанию для Nginx)
EXPOSE 80