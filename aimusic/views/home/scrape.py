from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
# 爬虫包
from aimusic.scrapers.weibo_scraper import MyScraper
# 接口文档包
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class ScrapeView(APIView):
    """
        爬虫接口
    """
    @swagger_auto_schema(
            operation_summary="首页热搜接口",
            operation_description="使用爬虫获取数据，封装成对应形式返回",
            responses={
                200: openapi.Response(description="数据获取成功"),
                400: openapi.Response(description="请求参数错误"),
                500: openapi.Response(description="服务器内部错误")
            }
    )
    def get(self, request) -> Response:
        try:
            # 创建 MyScraper 的实例
            scraper = MyScraper()
            
            # 获取数据
            name_list, hot_list, url_list = scraper.scrape()
            
            # 创建相对热度列表
            # 只取前30
            relative_hot_list = []
            for i in range(len(hot_list)):
                if i < 5:
                    relative_hot_list.append(1)
                elif 5 <= i < 10:
                    relative_hot_list.append(0.8)
                elif 10 <= i < 15:
                    relative_hot_list.append(0.6)
                elif 15 <= i < 20:
                    relative_hot_list.append(0.4)
                elif 20 <= i < 25:
                    relative_hot_list.append(0.2)
                elif 25 <= i < 30:
                    relative_hot_list.append(0)

            # 保留一位小数
            relative_hot_list = [round(x, 1) for x in relative_hot_list]    

            # 热度字典
            hot_dict = {}

            # 打印每个热词及其相对热度和链接
            for name, relative_hot, url in zip(name_list, relative_hot_list, url_list):
                hot_dict[name] = {'relative_hot': relative_hot, 'url': url}

            # 如果数据为空或获取失败，返回 400
            if not hot_dict:
                return Response({"error": "无法获取数据"}, status=400)

            # 返回数据
            return Response(hot_dict, status=200)
        
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=500)