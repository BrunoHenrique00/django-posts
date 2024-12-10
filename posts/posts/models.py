from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
