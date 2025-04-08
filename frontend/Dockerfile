# Билд-стадия
FROM node:18 AS build

WORKDIR /app

# Копируем только package.json и lock-файл
COPY package*.json ./

# Если используешь yarn — сначала установи его (и lock-файл переименуй)
# RUN corepack enable && corepack prepare yarn@stable --activate
# COPY yarn.lock ./
# RUN yarn install

# Downgrade ajv и ajv-keywords вручную для совместимости
RUN npm install ajv@6 ajv-keywords@3
# Если npm:
RUN npm install

COPY . .

RUN npm run build

# Прод-стадия — NGINX
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
