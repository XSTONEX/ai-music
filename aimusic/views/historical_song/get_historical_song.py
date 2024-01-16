from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


from aimusic.models import HistoricalSongs

from aimusic.utils.cos_utils import get_object_url


class HistoricalSong(APIView):
    
    def get(self, request) -> Response:

        id = request.query_params.get('id')
        song = HistoricalSongs.objects.get(id=id)

        video_url = get_object_url(
            BucketName="aimusic-1314972228",
            Key=song.video_url,
            Expired=60*30
        )

        data = {
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'release_date': song.release_date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期时间
                'duration': str(song.duration) if song.duration else None,  # 转换为字符串或者保留为None
                'chinese_lyrics': song.chinese_lyrics,
                'english_lyrics': song.english_lyrics,
                'original_hot_term': song.original_hot_term,
                'video_url': video_url,
            }

        return Response({
            "result": "success",
            "data": data, 
        })


        
        