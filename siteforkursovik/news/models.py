from django.db import models
from django.contrib.auth.models import User
from pytils.translit import slugify

import random

class News(models.Model):
    titel = models.CharField('Название новости', max_length=64)
    slug = models.SlugField('Slug', max_length=64, unique=True, db_index=True)
    intro = models.CharField('Краткое описание статьи', max_length=250)
    full_text = models.TextField('Текст статьи')
    date_create = models.DateTimeField('Дата публикации', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    photo = models.ImageField('Фотография', upload_to="photos/uploaded/%Y/%m/%d/", blank=True)
    is_modarated = models.BooleanField('Проведена ли была модерация?')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return f"Новость: {self.titel}"
    
    def get_absolute_url(self):
        return f"/news/{self.slug}"
    
    def save(self, *args, **kwargs):
        randomnumber = str(random.randint(10000000000, 99999999999))
        titelslug = slugify(self.titel)
        self.slug = titelslug + '-' + randomnumber
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'