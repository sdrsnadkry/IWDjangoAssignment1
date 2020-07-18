from django import forms
from .models import Blog, Author


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5'
            })
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5'
            })
        }
