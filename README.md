# How to use multiple forms for commenting

[referred blog](https://narito.ninja/blog/detail/95/)

![1_how_it_looks](https://github.com/NoriKaneshige/Django_Multiple_Forms_For_Commenting/blob/master/1_how_it_looks.png)


> ## models.py
``` python
from django.db import models


class Diary(models.Model):
    text = models.TextField('diary')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
  
        def __str__(self):
            return self.title


class Comment(models.Model):
    text = models.CharField('comment', max_length=300)
    target = models.ForeignKey(Diary, on_delete=models.CASCADE, verbose_name='related diary')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
  
        def __str__(self):
            return self.title
```

> ## forms.py
``` python
from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('text','target',)
        # should not include 'target', otherwise pulldown will be displayed
        fields = ('text',)
```


> ## views.py
``` python
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentCreateForm
from .models import Diary


def index(request):
    context = {
        'diary_list': Diary.objects.all(),
        'form': CommentCreateForm(),
    }
    return render(request, 'app/diary_list.html', context)


@require_POST
def create_comment(request, pk):
    form = CommentCreateForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.target = get_object_or_404(Diary, pk=pk)
        comment.save()
        return redirect('app:index')
        # 'index' and 'comment_create' is url name

    context = {
        'diary_list': Diary.objects.all(),
        'error_form': form,
        'form': CommentCreateForm(),
    }
    return render(request, 'app/diary_list.html', context)
```
