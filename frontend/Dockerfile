# Первая стадия: сборка приложения
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Вторая стадия: создание образа для Nginx
FROM nginx:alpine

# Удаляем все дефолтные конфиги и скрипты инициализации
RUN rm -rf /etc/nginx/conf.d/* && \
    rm -rf /docker-entrypoint.d/*

# Создаем свою директорию для pid-файла
RUN mkdir -p /var/run/nginx && \
    chmod -R 777 /var/run/nginx

# Копируем билд и конфиги
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Запускаем nginx напрямую, минуя entrypoint скрипты
CMD ["nginx", "-g", "daemon off;"]
