from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('text','target',)
        # should not include 'target', otherwise pulldown will be displayed
        fields = ('text',)


