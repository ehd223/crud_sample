from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text')
    widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-control'
            }
        ),
        'text': forms.Textarea(attrs={
            'class': 'form-control',
            'rows':'3',
            }
        ),
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('nickname', 'text',)
    widgets = {
        'nickname': forms.TextInput(attrs={
            'class': 'form-control'
            }
        ),
        'text': forms.Textarea(attrs={
            'class': 'form-control',
            'rows':'3',
            }
        ),
    }
    