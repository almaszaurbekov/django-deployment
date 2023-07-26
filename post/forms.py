from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['author'].initial = user
            self.fields['author'].widget.attrs['readonly'] = True

    class Meta:
        model = Post
        fields = ['author', 'topic', 'text']