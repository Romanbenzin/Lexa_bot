package main

import (
	"Lexa_bot/api/db"
	"Lexa_bot/api/handlers"

	"github.com/gin-gonic/gin"
)

func main() {
	// Подключение к БД
	dbConn, err := db.NewPostgresDB()
	if err != nil {
		panic(err)
	}
	defer dbConn.Close()

	// Инициализация роутера
	r := gin.Default()

	// Регистрация обработчиков
	handlers.RegisterRoutes(r, dbConn)

	// Запуск сервера
	r.Run(":8080") // Можно вынести в конфиг
}
