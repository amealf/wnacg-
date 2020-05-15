import requests
import os
import pandas as pd
from bs4 import BeautifulSoup


page_url = []
page_title = []
picture_num = []
pic_num = 0  # 图片编号
os.makedirs('./outcome/', exist_ok=True)

for page in range(1, 3, 1):#从1页开始，到3页结束，每次翻1页
    url = 'https://www.wnacg.org/albums-index-page-{}'.format(page) + '-sname-%E8%AA%BF%E6%95%99.html'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.44 Safari/537.36'
    '''
    res = requests.get(url=url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(res.content, "html.lxml")
    这两行可以缩写成以下一行
    '''
    bs = BeautifulSoup(requests.get(url=url,headers={'User-Agent': user_agent}).content, "lxml")  # 调用lxml作为解析引擎 需要:pip install lxml

    #print(bs)

    for i in bs.select('.pic_box'):
        pic_url = ('https:' + (i.find('img')['src']))
        title = ('https:' + (i.find('a')['title']))
        page = ('https:' + (i.find('a')['href']))
        #print(pic_url)
        pic_file = open('./outcome/'+str(pic_num)+'.jpg', 'wb')  # 二进制创建并写入文件
        pic_file.write(requests.get(pic_url).content)  # 写出请求得到的img资源
        page_url.append(page)
        page_title.append(title)
        picture_num.append(pic_num)
        pic_num += 1
        print(pic_num)

data = {'Number': picture_num, 'URL': page_url ,'Title': page_title}

print(data)
df = pd.DataFrame(data)

print(df)
df.to_csv('./outcome/wnacg.csv', index=False, encoding='utf_8_sig')
