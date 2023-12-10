from flask import Flask, render_template, request, send_file
import pandas as pd
from snownlp import SnowNLP
import urllib.request
import json
import io

app = Flask(__name__)

LANGUAGES = {
    '简体中文': 'cn',
    '繁体中文': 'tw',
    '英语': 'us',
    '日语': 'jp',
    '法语': 'fr',
    '德语': 'de',
    '西班牙语': 'es',
    '葡萄牙语': 'pt',
    '韩语': 'kr',
    '阿拉伯语': 'sa'
}

# 获取评论的函数
def get_reviews(appid, page, country):
    url = "https://itunes.apple.com/{}/rss/customerreviews/page={}/id={}/sortby=mostrecent/json".format(country, page, appid)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    if "entry" in data["feed"]:
        return data["feed"]["entry"]
    else:
        return []

# 情感分析的函数
def sentiment_analysis(text):
    sentiment = SnowNLP(text).sentiments
    if sentiment > 0.6:
        return "好评"
    elif sentiment < 0.4:
        return "差评"
    else:
        return "中性"

# 主页面路由
@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

# 获取评论并下载为Excel的路由
@app.route('/fetch_reviews', methods=['POST'])
def fetch_reviews():
    appid = request.form['appid']
    language = request.form['language']
    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])
    
    result = []
    for page in range(start_page, end_page + 1):
        reviews = get_reviews(appid, page, LANGUAGES[language])
        for review in reviews:
            if isinstance(review, dict):
                date = review["updated"]["label"]
                content = review['content']['label']
                rating = review['im:rating']['label']
                version = review['im:version']['label']
                author = review['author']['name']['label']
                sentiment = sentiment_analysis(content)
                result.append({
                    'updated': date,
                    'content': content,
                    'rating': rating,
                    'version': version,
                    'author': author,
                    'sentiment': sentiment
                })
    
    # 将评论数据保存为Excel文件
    df = pd.DataFrame(result)
    excel_io = io.BytesIO()
    with pd.ExcelWriter(excel_io, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Comments', index=False)
    excel_io.seek(0)
    
    # 设置响应信息并发送文件
    return send_file(
        excel_io,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='comments.xlsx'
    )

# 启动Flask应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8000) 