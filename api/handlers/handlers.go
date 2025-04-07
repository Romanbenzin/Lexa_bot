package handlers

import (
	"database/sql"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func RegisterRoutes(r *gin.Engine, db *sql.DB) {
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{"message": "pong"})
	})

	r.GET("/count_purchases", func(c *gin.Context) {
		GetCountPurchases(c, db)
	})

	r.GET("/get_game", func(c *gin.Context) {
		GetGame(c, db)
	})
}

func GetCountPurchases(c *gin.Context, db *sql.DB) {
	var count int
	err := db.QueryRow("SELECT COUNT(*) FROM purchases").Scan(&count)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error":   "Failed to count purchases",
			"details": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"purchase_count": count,
	})
}

func GetGame(c *gin.Context, db *sql.DB) {
	userName := c.Query("user_name")
	if userName == "" {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "Параметр 'user_name' обязателен",
		})
		return
	}

	// Обновленный SQL-запрос
	query := `
        SELECT p.steam_link, p.purchase_date
        FROM purchases p
        JOIN users u ON u.id::text = ANY(string_to_array(REGEXP_REPLACE(p.user_ids, '\s', '', 'g'), ','))
        WHERE u.user_name = $1
        ORDER BY p.purchase_date DESC;
    `

	rows, err := db.Query(query, userName)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error":   "Ошибка при выполнении запроса к базе данных",
			"details": err.Error(),
		})
		return
	}
	defer rows.Close()

	var games []gin.H
	for rows.Next() {
		var gameLink, purchaseDate string
		if err := rows.Scan(&gameLink, &purchaseDate); err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{
				"error":   "Ошибка при чтении данных из базы",
				"details": err.Error(),
			})
			return
		}

		// Извлекаем название игры из URL
		re := regexp.MustCompile(`/app/\d+/([^/]+)/`)
		match := re.FindStringSubmatch(gameLink)
		gameName := "Unknown Game"
		if len(match) > 1 {
			gameName = strings.ReplaceAll(match[1], "_", " ")
		}

		// Добавляем данные игры в список
		games = append(games, gin.H{
			"game_name":     gameName,
			"game_link":     gameLink,
			"purchase_date": purchaseDate,
		})
	}

	if len(games) == 0 {
		c.JSON(http.StatusOK, gin.H{
			"message": "У пользователя нет покупок.",
		})
		return
	}

	c.JSON(http.StatusOK, games)
}
