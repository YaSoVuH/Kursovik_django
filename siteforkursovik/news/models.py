from django.db import models

class News(models.Model):
    titel = models.CharField('Название новости', max_length=64)
    intro = models.CharField('Краткое описание статьи', max_length=250)
    full_text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации')
    #authorid = models.IntegerField('ID автора статьи')

    def __str__(self):
        return f"Новость: {self.titel}"
    
    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'