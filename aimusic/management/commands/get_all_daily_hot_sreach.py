import logging
import json
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from aimusic.models import HotSearch
from django.db.models import Sum

logger = logging.getLogger("django")


# 歌手名称
SONGER_NAME = [
    "Michael Jackson",
    "Elvis Presley",
    "Adele Laurie Blue Adkins",
    "Madonna Louise Ciccone",
    "Bob Dylan",
    "Freddie Mercury",
    "Whitney Houston",
    "John Lennon",
    "Paul McCartney",
    "Stevie Wonder",
    "David Bowie",
    "Prince",
    "Taylor Swift"
]


class Command(BaseCommand):
    help = 'Analyze hot search at regular intervals'

    def handle(self, *args, **options):
        # 19 - 26
         # 当前时间
        current_time = timezone.now()
        formatted_date = current_time.strftime("%Y-%m-%d")
        year = current_time.strftime("%Y")
        month = current_time.strftime("%m")
        day = current_time.strftime("%d")
        current_timestamp = current_time.timestamp()
        
        # TODO: 查询每日最热热搜
        # 获取当前日期的开始和结束时间戳
        start_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = start_time + timedelta(days=1)
        
        
        for i in range(19, 27):
            start_time = f"2023-10-{i} 00:00:00"
            end_time = f"2023-10-{i+1} 00:00:00"
            logger.info(f"start_time {start_time}")
            logger.info(f"今日歌手： {random.choice(SONGER_NAME)} \n")
        
            # 查询并计算每个search_term的search_volume总和，按照search_volume降序排序
            hot_searches = HotSearch.objects.filter(
                date__range=(start_time, end_time)
            ).values('search_term').annotate(total_search_volume=Sum('search_volume')).order_by('-total_search_volume')[:20]
            
            # 将search_term提取出来并存储为一个列表
            search_terms_list = [hot_search['search_term'] for hot_search in hot_searches]
            
            logger.info('\n' + '\n'.join(search_terms_list))         
        
            
        self.stdout.write(self.style.SUCCESS(f'Current time: {current_time}; Hot search analyze successfully!'))
        
