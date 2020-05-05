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


