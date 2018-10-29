import jieba
from jieba import analyse
import time

start_time = time.time()
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags
# textrank = analyse.textrank
# jieba.suggest_freq('半导体行业', True)
# 原始文本
# text = "线程是程序执行时的最小单位，它是进程的一个执行流，\
#         是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，\
#         线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。\
#         线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。\
#         同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"
with open('paper.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    # 基于TF-IDF算法进行关键词抽取
    # keywords = textrank(text, withWeight=True, topK=30)
    keywords = tfidf(text, withWeight=False, topK=30)
    print("keywords by tfidf:")
    # 输出抽取出的关键词
    # for keyword, weight in keywords:
    #     print(keyword, weight)
    print(keywords)

end_time = time.time()

print('提取关键词耗时：', end_time - start_time)
