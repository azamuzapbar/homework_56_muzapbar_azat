from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    category = (
        ('phone', 'телефон'),
        ('laptop', 'ноутбук')
    )

    title = models.CharField(verbose_name='название', max_length=100, null=False, blank=False)
    text = models.TextField(verbose_name='описание', max_length=2000, null=False, blank=False)
    image = models.CharField(max_length=100,null=True,blank=True)
    category = models.TextField(verbose_name='категория', choices=category, default='other', null=False, blank=False)
    remainder = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.title} - {self.text} - {self.category}'
