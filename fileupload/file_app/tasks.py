# tasks.py
from importlib.resources import contents
from unicodedata import name
import uuid
import os
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
  nameFile = 'bw'+os.path.basename(obj.file.name)
  path = f"/Users/pouria/Documents/uploadVideo/fileupload/media/temp/{nameFile}"

  bw.save(path) 
  path = Path(path)
  
  obj.newtext = reverse_text
  nameFile_bw = 'bw'+f'media/temp/bw{nameFile}'
  obj.file_bw.save(nameFile,File(open(f'media/temp/{nameFile}', 'rb')))
  os.remove(path)

