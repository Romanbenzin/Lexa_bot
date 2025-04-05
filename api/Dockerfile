# Стадия сборки
FROM golang:1.23 as builder

WORKDIR /app

# Копируем только файлы модулей сначала (для кэширования)
COPY go.mod go.sum ./
RUN go mod download

# Копируем ВСЕ остальные файлы
COPY . .

# Устанавливаем правильный путь для модуля
ENV GO111MODULE=on

# Собираем приложение (важно использовать полный путь модуля)
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o main .

# Финальный образ
FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]