import logging
import json
import pandas as pd

from django.core.management.base import BaseCommand
from django.utils import timezone

from aimusic.models import HotSearch, TFIDFHotSearch
from aimusic.utils.analyze_hot_search import analyze_hot_search

logger = logging.getLogger("django")

class Command(BaseCommand):
    help = 'Analyze hot search at regular intervals'

    def handle(self, *args, **options):
        
        # 当前时间
        # 每个小时执行一次
        current_time = timezone.now()
        current_timestamp = current_time.timestamp()
        
        # TODO 1: 获取12个小时的热搜, 并保存成csv文件
        twelve_hours_ago = current_time - timezone.timedelta(hours=12)
        hot_searches = HotSearch.objects.filter(date__gte=twelve_hours_ago)

        # TODO 2: 分析热搜，得到TF-IDF分数最大的前15热搜字典
        feature_keywords_full = analyze_hot_search(hot_searches)
        feature_keywords_full_str = json.dumps(feature_keywords_full)
    
        # TODO 3: 保存到TFIDFHotSearch表中
        new_tfidf_hot_search = TFIDFHotSearch.objects.create(
            time=current_time,                                      # 当前时间
            timestamp=current_timestamp,                            # 当前时间戳
            processed_result=feature_keywords_full_str,             # 处理后的结果
        )
            
        self.stdout.write(self.style.SUCCESS(f'Current time: {current_time}; Hot search analyze successfully!'))
        
