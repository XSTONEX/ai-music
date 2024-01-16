from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from aimusic.models import HistoricalSongs


class HistoricalSongList(APIView):
    """
    热点预测

    :param APIView: _description_
    :type APIView: _type_
    """
    
    def get(self, request) -> Response:

        # 获取所有记录并按日期倒序排序
        records = HistoricalSongs.objects.all()

        data = []
        for record in records:
            song_data = {
                'id': record.id,
                'title': record.title,
                'artist': record.artist,
                'release_date': record.release_date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期时间
                'duration': str(record.duration) if record.duration else None,  # 转换为字符串或者保留为None
                'chinese_lyrics': record.chinese_lyrics,
                'english_lyrics': record.english_lyrics,
                'original_hot_term': record.original_hot_term,
                'video_url': record.video_url,
            }
            data.append(song_data)

        return Response({
            "result": "success",
            "data": data, 
        })


        
        