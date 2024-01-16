from django.contrib import admin

from .models import HotSearch, TFIDFHotSearch, HistoricalSongs



# admin界面中显示列表
class HotSearchAdmin(admin.ModelAdmin):
    list_display = (
                    "id", "rank", "search_term", "search_link", 
                    "search_volume", "format_date", "time_stamp", "source"
    )
    # 点击进入详情页面
    list_display_links = ("id", "search_term", )
    # 列表页面可更改
    list_editable = ("source", )
    # 列表页面快速过滤, 如过滤日期
    list_filter = ("date", )
    # 指定字段模糊搜索
    search_fields = ("search_term", )

# admin界面中显示列表
class TFIDFHotSearchAdmin(admin.ModelAdmin):
    list_display = (
                    "id", "format_time", "timestamp", "processed_result", 
    )
    # 点击进入详情页面
    list_display_links = ("id", "format_time", )
    # 列表页面快速过滤, 如过滤日期
    list_filter = ("time", )
    
    
# admin界面中显示列表
class HistoricalSongsAdmin(admin.ModelAdmin):
    list_display = (
                    "id", "title", "artist", "format_release_date", "duration", 
                    "chinese_lyrics", "english_lyrics", "original_hot_term", "video_url"
    )
    
    # 列表页面快速过滤, 如过滤日期
    list_filter = ("release_date", )


admin.site.register(HotSearch, HotSearchAdmin)  # 注册订单图片模型
admin.site.register(TFIDFHotSearch, TFIDFHotSearchAdmin)  # 注册用户模型
admin.site.register(HistoricalSongs, HistoricalSongsAdmin)  # 注册用户订单模型
