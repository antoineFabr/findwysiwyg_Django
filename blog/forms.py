from django import forms
from tinymce.widgets import TinyMCE
from django_quill.forms import QuillFormField

class TinyMCEForm(forms.Form):
    contenu = forms.CharField(widget=TinyMCE(), label="TinyMCE")

class QuillJsForm(forms.Form):
    contenu = QuillFormField(label="Quill.js")
