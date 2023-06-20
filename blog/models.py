from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created = models.DateField(auto_now=True, verbose_name="Дата публикации")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")
    cover = models.ImageField(upload_to="uploads/blog", blank=True, default="image.jpg", verbose_name="Изображение")



    def __str__(self):
        return f'{self.title} - {self.created}'


    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"