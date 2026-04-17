from django import forms
from tinymce.widgets import TinyMCE

class TinyMCEForm(forms.Form):
    contenu = forms.CharField(widget=TinyMCE(), label="TinyMCE")
