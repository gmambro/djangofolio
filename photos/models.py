from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from io import BytesIO
from PIL import Image, ImageFile

DEFAULT_SIZE = getattr(settings, 'DJANGOFOLIO_DEFAULT_SIZE', [800, 800])

class Photo(models.Model):
    original    = models.ImageField()
    pub_date    = models.DateTimeField('date published')
    title       = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)

    preview     = models.ImageField(blank=True, null=True)


    @classmethod
    def from_db(cls, db, field_names, values):
        
        instance = super(Photo, cls).from_db(db, field_names, values)

        # customization to store the original field values on the instance
        instance._loaded_values = dict(zip(field_names, values))
        
        return instance


    def _generate_preview(self):
        try:
            img = Image.open(self.original)
            img.thumbnail(DEFAULT_SIZE, Image.ANTIALIAS)
            
            ImageFile.MAXBLOCK = max(ImageFile.MAXBLOCK, img.size[0] * img.size[1])
            preview_content = BytesIO()
            img.save(preview_content, "JPEG")
                
            self.preview.save(
                self.original.name + '-preview',
                    ContentFile(preview_content.getvalue()),
                    False
                )            
            
        except IOError:
            raise Exception("cannot create thumbnail")   
    
    def save(self, *args, **kwargs):
        if self.original != self._loaded_values['original']:        
            self._generate_preview()          

        super(Photo, self).save(*args, **kwargs)
