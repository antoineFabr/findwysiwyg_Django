from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('tinymce/', views.test_tinymce, name='tinymce'),
    path('quilljs/', views.test_quilljs, name='quilljs')
]
