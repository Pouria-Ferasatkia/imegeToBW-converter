# tasks.py
import uuid

from django.db import models
from file_app.models import Video 
from time import sleep
from celery import shared_task
from PIL import Image





@shared_task()
def resize(video):
   
    color_image = Image.open(video.file.path)

    bw = color_image.convert('1', dither=Image.NONE)

    videoNew = Video(file =video, file_bw=bw)
    videoNew.save()

