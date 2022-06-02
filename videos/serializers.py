from rest_framework import serializers
from .models import Video,Category

class GetAllVideosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video 
    fields = ['id','title','category', 'youtube_link', 'created_at', 'updated_at']

class GetAllCategoriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category 
    fields = ['id','name','created_at', 'updated_at']


class VideoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video 
    fields = ['id','title','category', 'youtube_link', 'updated_at']

  def save(self):
    try:
      title = self.validated_data['title']
      category=self.validated_data['category']
      youtube_link=self.validated_data['youtube_link']
      video = Video(
        title=title, category=category, youtube_link=youtube_link
      )
      video.save()
      return video
    except KeyError:
      raise serializers.ValidationError({"response": "Data is not correct"})

