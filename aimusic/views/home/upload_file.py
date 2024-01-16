from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
# 工具包
from aimusic.utils import cos_utils
# 接口文档包
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UploadFileView(APIView):
    # 上传文件配置
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        operation_summary="上传图片接口",
        operation_description="根据上传的文件类型（图片或音频）保存到相应的位置",
        # 上传文件配置
        manual_parameters=[
            openapi.Parameter(
                name='file',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description='上传文件'
            ),
        ],
        responses={
            200: openapi.Response(description="成功上传文件", schema=openapi.Schema(
                type='object',
                properties={
                    'message': openapi.Schema(type='string', description='成功消息'),
                    'ETag': openapi.Schema(type='string', description='ETag响应'),
                    'file_url': openapi.Schema(type='string', description='文件URL')
                }
            )),
            400: openapi.Response(description="不支持的文件类型"),
            500: openapi.Response(description="服务器内部错误")
        }
    )
    
    def post(self, request):
        """
            上传图片接口
        """
        uploaded_file = request.FILES.get('file')  # 获取上传的文件对象
        try:
            if uploaded_file.content_type.startswith('image/'):
                response = cos_utils.simple_upload_by_stream(
                    BucketName="main-1314972228",
                    Body=uploaded_file,
                    Key="Photo/" + uploaded_file.name
                )
                file_url = cos_utils.get_object_url(
                    BucketName="main-1314972228",
                    Key="Photo/" + uploaded_file.name
                )
                return Response(
                    {
                        'message': 'Photo File uploaded successfully',
                        'ETag': response,
                        'file_url': file_url
                    }
                )
            elif uploaded_file.content_type.startswith('audio/'):
                response = cos_utils.simple_upload_by_stream(
                    BucketName="main-1314972228",
                    Body=uploaded_file,
                    Key="Audio/" + uploaded_file.name
                )
                file_url = cos_utils.get_object_url(
                    BucketName="main-1314972228",
                    Key="Audio/" + uploaded_file.name
                )
                return Response(
                    {
                        'message': 'Audio File uploaded successfully',
                        'ETag': response,
                        'file_url': file_url
                    }
                )
            else:
                return Response({'error': 'Unsupported file type'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)