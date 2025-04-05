package handlers

import (
	"database/sql"
	"net/http"

	"github.com/gin-gonic/gin"
)

func RegisterRoutes(r *gin.Engine, db *sql.DB) {
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{"message": "pong"})
	})

	r.GET("/count_purchases", func(c *gin.Context) {
		GetCountPurchases(c, db)
	})
}

func GetCountPurchases(c *gin.Context, db *sql.DB) {
	var count int
	err := db.QueryRow("SELECT COUNT(*) FROM purchases").Scan(&count)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error":    "Failed to count purchases",
			"details":  err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"purchase_count": count,
	})
}
