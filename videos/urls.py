from django.urls import path
from . import views
app_name= 'videos'

urlpatterns = [
    path('',views.index,name='index'),
    path('video/', views.VideoListView.as_view(), name='get_list_videos'),
    path('category/', views.CategoryListView.as_view(), name='get_all_categories'),
]