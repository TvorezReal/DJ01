from .models import News_post
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'feedback', 'pub_date']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
            'feedback': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }