from django.db import models

# Create your models here.
class ImageModel(models.Model):

    image = models.ImageField(upload_to='images',null=True,blank=True)

    # description = models.TextField(max_length=2000)

