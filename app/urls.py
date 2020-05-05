from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/comment/<int:pk>/', views.create_comment, name='comment_create')
]

