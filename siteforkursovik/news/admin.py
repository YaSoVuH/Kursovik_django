from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titel',),}

    def save_model(self, request, obj, form, change):
        if not change: # Проверяем что запись только создаётся
            obj.author = request.user # Присваеваем полю автор текущего пользователя
    
        super(NewsAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )