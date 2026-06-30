package api

import (
	"time"

	"github.com/gin-gonic/gin"
)

type Post struct {
	ID          uint      `json:"id" gorm:"primaryKey"`
	Title       string    `json:"title"`
	Content     string    `json:"content"`
	Preview     string    `json:"preview"`
	Author      string    `json:"author"`
	PublishDate time.Time `json:"publishDate"`
	Comments    []Comment `json:"comments"`
}

type Comment struct {
	ID              uint   `json:"id" gorm:"primaryKey"`
	Content         string `json:"content"`
	Author          string `json:"author"`
	PostRelatedToID uint
}

type JsonResponse struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    any    `json:"data"`
}

func ResponseJSON(c *gin.Context, status int, message string, data any) {
	response := JsonResponse{
		Status:  status,
		Message: message,
		Data:    data,
	}

	c.JSON(status, response)
}
