from dataclasses import fields
from venv import create
from rest_framework import serializers
from .models import Video

class FileSerializer(serializers.ModelSerializer):
  id = serializers.ReadOnlyField()
  class Meta():
    model = Video
    #fields = ('file','file_bw', 'timestamp')
    fields = ('id','text','newtext','file','file_bw')


  def create(self, validated_data):
    video = Video.objects.create(**validated_data)
    return video




    