from django.db import models
from django.contrib import admin

class HotSearch(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='热搜ID')  
    rank = models.IntegerField(verbose_name='热度排名') 
    search_term = models.CharField(max_length=255, verbose_name='热搜内容')  
    search_link = models.CharField(max_length=255, verbose_name='热搜链接')
    search_volume = models.BigIntegerField(verbose_name='搜索量')  
    date = models.DateTimeField(verbose_name='热搜的日期和时间')  
    time_stamp = models.BigIntegerField(verbose_name='热搜的时间戳') 
    source = models.CharField(max_length=100, verbose_name='热搜来源')    
    class Meta:
        verbose_name = '热搜'  
        verbose_name_plural = '热搜列表' 
        
    @admin.display(description="热搜的日期和时间")
    def format_date(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")
        
    def __str__(self):
        return f"{self.rank}: {self.search_term}"


class TFIDFHotSearch(models.Model):
    id = models.BigAutoField(primary_key=True)  
    time = models.DateTimeField() 
    timestamp = models.BigIntegerField() 
    processed_result = models.TextField() 
    
    @admin.display(description="热搜的日期和时间")
    def format_time(self):
        return self.time.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = 'TF-IDF处理后的热搜'
        verbose_name_plural = 'TF-IDF处理后的热搜列表'

    def __str__(self):
        return self.term



class HistoricalSongs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='历史歌曲ID')
    title = models.CharField(max_length=100, verbose_name='歌曲标题')
    artist = models.CharField(max_length=100, verbose_name='歌曲歌手')
    release_date = models.DateTimeField(verbose_name='发布时间')
    duration = models.TimeField(null=True, blank=True,verbose_name='歌曲时长')
    chinese_lyrics = models.TextField(verbose_name='中文歌词')
    english_lyrics = models.TextField(verbose_name='英文歌词')
    original_hot_term = models.TextField(verbose_name='原始热词')
    video_url = models.TextField(verbose_name='视频地址')

    class Meta:
        verbose_name = '历史歌曲'
        verbose_name_plural = '历史歌曲列表'
        
        
    @admin.display(description="发布时间")
    def format_release_date(self):
        return self.release_date.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.release_date}: {self.title}"
