from django.db import models


class Client(models.Model):
    telegram_id = models.IntegerField(unique=True)
    nik_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="UserName"
    )

    def __str__(self):
        return f"{self.nik_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Category(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Категория торта",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Cake(models.Model):
    # Модель для добавления тортов через админку для каталога
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cakes', blank=True, null=True)
    price = models.IntegerField(
        verbose_name="Стоимость торта"
    )
    # levels = 0
    # form = 0
    # topping = 0
    # berries = 0
    # decor = 0
    # inscription = 0
    # img = 0

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Торты"

