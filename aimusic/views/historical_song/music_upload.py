import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone

from aimusic.models import HistoricalSongs

from aimusic.utils.cos_utils import simple_upload_by_stream, get_object_url

logger = logging.getLogger("django")

class MusicUploadView(APIView):

    def post(self, request):
        # TODO 1: 解析request
        title = request.data.get('title').strip()
        artist = request.data.get('artist').strip()
        chinese_lyrics = request.data.get('chineseLyrics').strip()
        english_lyrics = request.data.get('englishLyrics').strip()
        hot_term = request.data.get('hotTerm').strip()
        uploaded_file = request.data.get('file')
        data = request.data.get('dataValue')

        # TODO 2: 非空验证
        if title == "" or artist == "" or chinese_lyrics == "" \
            or english_lyrics == "" or hot_term == "":
            return Response({
                "result": "未填写完毕!",
                "status": "fail",
            })
        
        if uploaded_file == None:
            return Response({
                "result": "未上传音频!",
                "status": "fail",
            })
        
        # TODO 3: 解析时间
        # 使用strptime方法解析日期字符串
        current_time = timezone.now()
        formatted_date = current_time.strftime("%Y-%m-%d")
        data = data.replace(" GMT+0800 (中国标准时间)","")  # 删除 "GMT+0800 (中国标准时间)" 部分
        date_object = datetime.strptime(data, "%a %b %d %Y %H:%M:%S")
        year = date_object.year
        month = date_object.month
        day = date_object.day

        
        # TODO 4: 视频文件上传至cos
        file_data = uploaded_file.read()
        folder_name = "-".join(list(map(str,[year, month, day])))
        key = folder_name + "/" + uploaded_file.name

        simple_upload_by_stream(
            BucketName="aimusic-1314972228",
            Body=file_data,
            Key=key,
        )
        

        # TODO 5: 保存至数据库
        # 创建一个 HistoricalSongs 对象
        historical_song = HistoricalSongs.objects.create(
            title=title,                        # 歌曲标题
            artist=artist,                      # 歌曲歌手
            release_date=formatted_date,        # 发布时间
            chinese_lyrics=chinese_lyrics,      # 中文歌词
            english_lyrics=english_lyrics,      # 英文歌词
            original_hot_term=hot_term,         # 原始热词       
            video_url=key,                      # 视频地址
        )

        return Response({
            "result": "上传成功！",
            "status": "success",
        })
