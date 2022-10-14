from django.db import models

# Create your models here.
from django.db import models

class Video(models.Model):
  #file = models.FileField(blank=False, null=False)
 # file_bw = models.FileField(blank=True, null=True)
  #timestamp = models.DateTimeField(auto_now_add=True)
  #time= models.IntegerField(blank=True, null=True)
  text = models.TextField(blank=False, null=True)
  newtext = models.TextField(blank=False, null=True)
  file = models.FileField(upload_to='mainImage', null=True)
  file_bw = models.FileField(upload_to='bwImage', null =True)

  #def save(file):
   #self.file_bw.save(file)