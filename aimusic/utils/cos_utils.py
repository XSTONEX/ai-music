# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括 secret_id, secret_key, region 等
tmp_secret_id = 'AKIDwRt9Mk1DlEb0HXgfSCvY1NjyFcrskpZI'     # 临时密钥的 SecretId
tmp_secret_key = '5HViu8Mds5ADGJIhe5n870oXQI3c5bVK'   # 临时密钥的 SecretKey
region = 'ap-guangzhou'      # 替换为用户的 region

config = CosConfig(Region=region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key)
client = CosS3Client(config)

# 创建存储桶
def create_bucket(BucketName):
    response = client.create_bucket(
        # 桶的名称
        Bucket=BucketName,
        ACL='public-read',
    )
    return response

# 获取存储桶列表
def get_bucket_list():
    response = client.list_buckets()
    return response

# 字节流简单上传
def simple_upload_by_stream(BucketName, Body, Key):
    response = client.put_object(
        Bucket=BucketName,
        Body=Body,
        Key=Key,
    )
    print(response['ETag'])
    return response

# 获取url
def get_object_url(BucketName, Key, Expired):
    # url = client.get_object_url(
    #     Bucket=BucketName,
    #     Key=Key
    # )

    url = client.get_presigned_url(
        Method='GET',
        Bucket=BucketName,
        Key=Key,
        Expired=Expired,
    )

    return url
