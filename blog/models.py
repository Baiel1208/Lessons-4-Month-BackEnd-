from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    cover = models.ImageField(upload_to="uploads/blog", blank=True, default="image.jpg")



    def __str__(self):
        return f'{self.title} - {self.created}'
