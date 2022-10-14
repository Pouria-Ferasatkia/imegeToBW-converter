# tasks.py
from importlib.resources import contents
import uuid

from django.db import models
from file_app.models import Video 
from time import sleep
from celery import shared_task
from PIL import Image
from pathlib import Path
from file_app.serializers import FileSerializer
from django.core.files import File
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile


@shared_task()
def resize(videoid,textt,file):


  reverse_text = textt[::-1]
  obj = get_object_or_404(Video, id=videoid)
  
  color_image = Image.open(obj.file)
  bw = color_image.convert('1', dither=Image.NONE)
  path = "media/bwImage/a.png"
  bw.save(path)
  path = Path(path)
  
  obj.newtext = reverse_text
 # path = Path(obj.file.path)
  obj.file_bw.save("abc.png",File(open('media/bwImage/a.png', 'rb')))
  
#  obj.file_bw.save(obj.file.name,File(bw))
 # obj.file_bw = File(bw,name=obj.file.name)
 
