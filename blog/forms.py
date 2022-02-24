from django import forms
from .models import Post
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    content = RichTextField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags'
        ]

        widget = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput',
                                           'class': 'form-control', 'name': 'tags'})
        }
