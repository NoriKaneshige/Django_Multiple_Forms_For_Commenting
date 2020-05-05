from django.contrib import admin
from .models import Comment, Diary

admin.site.register(Diary)
admin.site.register(Comment)
