from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Название темы'}
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Например: Изучение Django'}),
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Текст записи'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Опишите, что нового вы узнали...'}),
        }
