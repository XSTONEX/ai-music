import requests
import logging
from lxml import etree

logger = logging.getLogger("django")


class MyScraper:

    # 爬取数据
    def scrape(self):

        # 确认目标的 url
        _url = "https://s.weibo.com/top/summary"

        # 手动构造请求的参数
        _headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
            "cookie" : "SUB=_2AkMTkDXvf8NxqwFRmPATy2nmbItxyQvEieKlzMQ0JRMxHRl-yT9kql0FtRB6OBAbAAXxgJwbSiZMZLMUGQYQwlIGJuUe; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhkJr9OD7433QJQKHpI9p3I; SINAGLOBAL=3040244700386.5586.1691139075412; UOR=www.baidu.com,s.weibo.com,www.baidu.com; _s_tentry=-; Apache=6828055440717.387.1691316033577; ULV=1691316033583:2:2:1:6828055440717.387.1691316033577:1691139075415",
        }

        # 发送请求
        _response = requests.get(_url, headers = _headers)
        _data = _response.text

        # 提取数据
        html_obj = etree.HTML(_data)

        # 热搜榜名称
        name_list = html_obj.xpath('//td/span/preceding-sibling::a/text()')

        # 热搜榜热度
        hot_list = html_obj.xpath('//td/span/text()')

        # 热搜榜链接
        url_list = html_obj.xpath('//td/span/preceding-sibling::a/@href')
        url_list = ["https://s.weibo.com/" + url for url in url_list]

        # 移除热度中的非数字部分
        hot_list = [int(''.join(filter(str.isdigit, hot))) for hot in hot_list if ''.join(filter(str.isdigit, hot)) != '']
        # 排序热度列表，假设最热的在前面
        hot_list = sorted(hot_list, reverse=True)

        return name_list, hot_list, url_list
        
