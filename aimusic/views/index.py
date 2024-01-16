from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
# 接口文档包
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class IndexView(APIView):
    """
        前端界面
    """
    @swagger_auto_schema(
        operation_summary="前端界面接口",
        operation_description="返回前端首页HTML内容",
        responses={
            200: openapi.Response(description="成功返回前端首页"),
            500: openapi.Response(description="服务器内部错误")
        }
    )
    def get(self, request, format=None):
        try:
            return render(request, 'index.html')
        except Exception as e:
            return Response({"error": str(e)}, status=500)