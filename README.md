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


```


> ## views.py
``` python


```
