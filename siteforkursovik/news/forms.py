from .models import News
from django.forms import ModelForm, TextInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['titel', 'intro', 'full_text']

        widgets = {
            "titel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полное описание'
            }),
        }