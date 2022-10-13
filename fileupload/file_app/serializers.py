from venv import create
from rest_framework import serializers
from .models import Video

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = Video
    fields = ('file','file_bw', 'timestamp')

  def create(self, validated_data):
    video = Video.objects.create(**validated_data)
    return video


    