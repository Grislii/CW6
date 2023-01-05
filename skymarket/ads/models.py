from django.conf import settings
from django.db import models


"""
- title — название товара.
- price — цена товара (целое число).
- description — описание товара.
- author — пользователь, который создал объявление.
- created_at — время и дата создания объявления.

*Все записи при выдаче должны быть отсортированы по дате создания 
(чем новее, тем выше).*

Модель **отзыва** должна содержать следующие поля:

- text — текст отзыва.
- author — пользователь, который оставил отзыв.
- ad — объявление, под которым оставлен отзыв.
- created_at - время и дата создания отзыва
"""

class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.text