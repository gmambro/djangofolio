from django import forms
from tinymce.widgets import TinyMCE

from album.model import Photo

class PhotoForm(models.Model):

    descrition = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model = Photo
