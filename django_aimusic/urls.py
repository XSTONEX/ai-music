"""django_aimusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from aimusic.views.index import IndexView
from aimusic.views.home.scrape import ScrapeView
from aimusic.views.home.upload_file import UploadFileView
from aimusic.views.hot_spot_prediction.hot_spot_prediction_list import HotSpotPrediction
from aimusic.views.historical_song.music_upload import MusicUploadView 
from aimusic.views.historical_song.historical_song_list import HistoricalSongList
from aimusic.views.historical_song.get_historical_song import HistoricalSong

schema_view = get_schema_view(
   openapi.Info(
      title="EveryDay",
      default_version='v1',
      description="新一代热点获取平台",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('weibo/', ScrapeView.as_view(), name='weibo'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path("hot_spot_prediction_list/", HotSpotPrediction.as_view(), name='hot_spot_prediction_list'),
    path("music_upload/", MusicUploadView.as_view(), name='music_upload'),
    path("historical_song_list/", HistoricalSongList.as_view(), name='historical_song_list'),
    path("get_historical_song/", HistoricalSong.as_view(), name='get_historical_song'),



    # 接口文档和测试页面生成工具
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    re_path(r".*", IndexView.as_view()),
]
