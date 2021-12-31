#### Answer for Q3
## Q3.1
url = "http://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/lastest/index.phtml?p=1"
url2 = "http://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/lastest/index.phtml?p=2"
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_list(url):
    r = requests.get(url)
    content = BeautifulSoup(r.content.decode("gb18030"), "html.parser")
    main_text = content.find("div", class_="main")
    tr_list = main_text.find_all("tr")[2:-1]
    return tr_list


tr_list = get_list(url) + get_list(url2)[:10]


def get_attr(tr):
    title = tr.find("a")['title']
    type = tr.contents[5].contents[0]
    date = tr.contents[7].contents[0]
    insitution = tr.find("span").contents[0]
    return title, type, date, insitution


data_list = []
for tr in tr_list:
    data_list.append(get_attr(tr))
df = pd.DataFrame(data_list, columns=['title', 'type', 'date', 'insitution'])
print(df)

## Q3.2

import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="sina")
cursor = db.cursor()
for data in data_list:
    sql = "insert into report(title, type, date, insitution) values ('%s', '%s', '%s', '%s')" % (
        data[0], data[1], data[2], data[3])
    cursor.execute(sql)

db.commit()

## Q3.3

sql = "select type, count(*) from report group by type"
res = cursor.execute(sql)
print(res)

sql = "select * from report where type = '报告'"
res = cursor.execute(sql)
print(res)

## Q3.4
# (a）
from snownlp import SnowNLP

df['sentiment'] = df['title'].apply(lambda x: SnowNLP(x).sentiments)

# (b)
sentiment_mean = df['sentiment'].mean(axis=0)
print(sentiment_mean)


## Q3.5
def get_content(tr):
    url = "http:" + tr.find("a")['href']
    r = requests.get(url)
    content = BeautifulSoup(r.content.decode("gb18030"), "html.parser")
    main_text = content.find("div", class_="blk_container")
    text = main_text.find("p").text
    return text.strip().replace("\n", "").replace(" ", "").replace("\t", "").replace("\r", "").replace(" ", "")


text_list = []
text_all = ""

for tr in tr_list:
    text = get_content(tr)
    text_list.append(text)
    text_all += text

import jieba.analyse as analyse

print('TF-IDF')
tf_idf_keyword_list = []
for text in text_list:
    for keyword, weight in analyse.extract_tags(text, topK=1, withWeight=True):
        tf_idf_keyword_list.append(keyword)
print('TextRank')
text_rank_keyword_list = []
for text in text_list:
    for keyword, weight in analyse.textrank(text_all, topK=1, withWeight=True):
        text_rank_keyword_list.append(keyword)

tf_idf_keyword_series = pd.Series(tf_idf_keyword_list)
text_rank_keyword_series = pd.Series(text_rank_keyword_list)
print(tf_idf_keyword_series)
print(text_rank_keyword_series)

## Q3.6
from wordcloud import WordCloud
import matplotlib.pyplot as plt

my_wordcloud = WordCloud(font_path="SimHei.ttf").generate(text_list[0])  # 生成词云

plt.imshow(my_wordcloud)  # 绘制词云图片
plt.axis("off")  # 不显示坐标轴
plt.show()  # 显示图片
