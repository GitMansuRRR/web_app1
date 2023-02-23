from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'anons', 'full_text', 'date')

        widgets = {
            "title": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Текст статьи'
            }),
        }

