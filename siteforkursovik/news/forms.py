from .models import News
from django.forms import ModelForm, TextInput, Textarea, BooleanField

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['titel', 'intro', 'full_text', 'photo']

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

class ModerationNewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ['titel', 'intro', 'full_text', 'photo', 'is_modarated']