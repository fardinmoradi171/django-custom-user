from django import forms
from django.forms.models import (inlineformset_factory,
                                 modelform_factory,
                                 modelformset_factory)
from .models import (Blog,BlogLike,BlogDislike,BlogComment)



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title","owner")
        
BlogFormSet = modelform_factory(Blog,BlogForm,["title","owner","description"])


class CommentForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()