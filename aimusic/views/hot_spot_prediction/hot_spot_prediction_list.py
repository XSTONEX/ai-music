import logging 
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from aimusic.models import TFIDFHotSearch

logger = logging.getLogger("django")

class HotSpotPrediction(APIView):
    """
    热点排行接口

    :param APIView: _description_
    :type APIView: _type_
    """
    
    def get(self, request) -> Response:
        
        # 获取最新的处理过的热点
        latest_tfidf_hot_search_obj = TFIDFHotSearch.objects.order_by('-id').first()

        # 处理结果
        tfidf_hot_search_processed_result = json.loads(latest_tfidf_hot_search_obj.processed_result)
        
        return Response({
            'result': 'success',
            'tfidf_hot_search_processed_result': tfidf_hot_search_processed_result,
        },status=200)