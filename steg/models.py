from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class PicModel(models.Model):
	img = models.ImageField(upload_to = path_and_rename)