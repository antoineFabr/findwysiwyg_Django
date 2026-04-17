from django.shortcuts import render
from . import forms

# Create your views here.
def test_tinymce(request):
    return render(request, 'blog/test_editeur.html', {'form': forms.TinyMCEForm(), 'titre': 'Test TinyMCE'})
