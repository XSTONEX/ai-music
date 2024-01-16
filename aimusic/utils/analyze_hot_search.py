import pandas as pd
import jieba
import logging
from sklearn.feature_extraction.text import TfidfVectorizer 

logger = logging.getLogger("django")

def analyze_hot_search(hot_search_filter_obj):
    
    # 将hot_searches的查询结果转换为Pandas DataFrame
    data = pd.DataFrame.from_records(hot_search_filter_obj.values())
    
    # 将热词对应热搜链接转化为字典
    hotsearch_dict = dict(zip(map(str.lower, data['search_term']), data['search_link']))
    
    # 获取文本数据列的名称，假设文本数据存储在名为'content'的列中
    texts = list(map(str.lower, data['search_term']))

    # 对文本进行分词
    tokenized_texts = [' '.join(word.lower() for word in jieba.cut(text)) for text in texts]

    # 使用TfidfVectorizer计算TF-IDF矩阵
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(tokenized_texts)

    # 获取特征名字
    feature_names = vectorizer.get_feature_names()

    # 提取特征名字和对应的TF-IDF分数
    feature_scores = tfidf_matrix.sum(axis=0).A1
    features_df = pd.DataFrame({'Feature': feature_names, 'TF-IDF Score': feature_scores})

    # 按TF-IDF分数降序排列
    sorted_features_df = features_df.sort_values(by='TF-IDF Score', ascending=False)[:15]

    # 打印排名结果
    # 重新设置DataFrame的索引
    sorted_features_df.reset_index(drop=True, inplace=True)

    # 创建一个空字典来存储特征和相关联的词语
    feature_keywords = {}

    # 遍历排序后的特征DataFrame
    for index, row in sorted_features_df.iterrows():
        # 获取当前特征和TF-IDF分数
        feature = row['Feature']
        tfidf_score = row['TF-IDF Score']
        
        # 在原始数据中查找包含当前特征的文本
        related_keywords = [text for text in texts if feature in text and tfidf_score > 0]
        
        # 将特征和相关联的词语存储到字典中
        feature_keywords[feature] = related_keywords

    feature_keywords_full = {}
    feature_keywords_full_2 = {}
    
    for index, (feature, keywords) in enumerate(feature_keywords.items(), start=1):
        # 使用集合来确保keywords中的keyword是唯一的
        unique_keywords = set(keywords)
        
        # 创建包含唯一关键词和对应热搜字典值的列表
        keywords_full = [[keyword, hotsearch_dict[keyword]] for keyword in unique_keywords]
        
        # 将关键词和对应热搜字典值的列表添加到feature_keywords_full字典中
        feature_keywords_full[feature] = keywords_full

        feature_keywords_full_2[index] = {feature: feature_keywords_full[feature]}

    logger.info("feature_keywords_full_2")
        
    return feature_keywords_full_2