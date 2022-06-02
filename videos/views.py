from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GetAllVideosSerializer,GetAllCategoriesSerializer,VideoCreateSerializer
from .models import Video, Category

def index(request):
  return render(request, 'index.html')

class VideoListView(APIView):
  def get(self, request):
    videos = Video.objects.select_related('category')
    title = self.request.query_params.get('title')
    category = self.request.query_params.get('category')
    if title is None:
      print('hello')
    print("h1: ",videos)
    if title is not None and category is not None:
      videos = videos.filter(title__contains=title, category__id=category)
    elif title is not None:
      videos = videos.filter(title__contains=title)
    elif category is not None:
      videos = videos.filter(category__id=category)
    print("h2: ",videos)
    serializer = GetAllVideosSerializer(videos, many=True)
    return Response(serializer.data)

  def post(self, request):
    data = request.data
    serializer = VideoCreateSerializer(data=data)
    data = {}
    if serializer.is_valid():
      video = serializer.save()
      data['title'] = video.title
      data['category_name'] = video.category.name
      data['youtube_link'] = video.youtube_link
      data['created_at'] = video.created_at
      return Response(data=data, status=status.HTTP_200_OK)


class CategoryListView(APIView):
  def get(self, request):
    try:
      categories = Category.objects.all()
    except Category.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = GetAllCategoriesSerializer(categories, many=True)
      return Response(serializer.data)

