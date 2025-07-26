//
//
//
//
import requests
import pandas as pd
import json
url = "https://api.cnyes.com/media/api/v1/newslist/category/headline"
payload = {
    "page":7,
    "limit":30,
    "isCategoryHeadline":1,
    "startAt":1752646755,
    "endAt":1753510755}
res = requests.get(url,params=payload)
jd=json.loads(res.text)
df=pd.DataFrame(jd['items']['data'])
df=df[['newsId','title','summary']]
df['link'] = df['newsId'].apply(lambda x: 'https://m.cnyes.com/news/id/' + str(x))
df.to_csv('news.csv',encoding='utf-8-sig')
print(df)
//