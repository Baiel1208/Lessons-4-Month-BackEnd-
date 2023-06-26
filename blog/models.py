from django.core.exceptions import ValidationError
from django.db import models

CATEGORY_CHOICES = (
    ("PR", "Происшествия"),
    ("POL", "Политика"),
    ("SP", "Спорт"),
    ("KU", "Культура"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")
    cover = models.ImageField(upload_to="uploads/blog", blank=True, default="image.jpg", verbose_name="Изображение")
    category = models.CharField(max_length=3, default="SP", choices=CATEGORY_CHOICES, verbose_name="Категория",
                                blank=True)

    def __str__(self):
        return f"{self.title} - {self.created}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comment(models.Model):
    name = models.CharField(max_length=16, verbose_name="Имя пользователя")
    comment = models.CharField(max_length=300, verbose_name="Текст комментария")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment", verbose_name="Запись")

    def __str__(self):
        return f"{self.name} - {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


