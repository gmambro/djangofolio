from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE

from .models import Photo



class PhotoForm(forms.ModelForm):
    
    class Meta:
        model   = Photo
        fields  = [ 'title', 'description', 'original' ]
        
        widgets = {
            'description': TinyMCE(attrs={'cols': 40, 'rows': 20}),
        }

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm


admin.site.register(Photo, PhotoAdmin)
