import logging
from django.core.management.base import BaseCommand
from django.utils import timezone

from aimusic.models import HotSearch 
from aimusic.scrapers.weibo_scraper import MyScraper
from aimusic.models import HotSearch

logger = logging.getLogger("django")

class Command(BaseCommand):
    help = 'Save hot search at regular intervals'

    def handle(self, *args, **options):
        
        # 当前时间
        current_time = timezone.now()
        current_timestamp = current_time.timestamp()
        
        # TODO: 存储热搜
        # 创建 MyScraper 的实例
        scraper = MyScraper()
        
        # 获取数据
        name_list, hot_list, url_list = scraper.scrape()
        
        for index, (name, search_volume, url) in enumerate(zip(name_list, hot_list, url_list), start=1):
            
            # 创建HotSearch对象并保存到数据库
            hot_search = HotSearch.objects.create(
                rank=index,                                 # 热度排名
                search_term=name,                           # 热搜内容
                search_link=url,                            # 热搜链接
                search_volume=search_volume,                # 搜索量
                date=current_time,                          # 热搜的日期和时间
                time_stamp=current_timestamp,               # 热搜的时间戳
                source='微博',                               # 热搜来源
            )
            
        self.stdout.write(self.style.SUCCESS(f'Current time: {current_time}; Hot search saved successfully!'))
        
