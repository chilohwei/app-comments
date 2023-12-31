## 简介
本项目是基于获取 App Store 应用评论的需求，与 GPT 协作，零基础全程用 Python Flask 写出来的网页应用。

[访问网站](https://apps.chiloh.cn)

## 部署

**docker-compose.yml**

```yml
version: "3"
services:
  web:
    image: chiloh/apps-comments:latest
    ports:
      - "8000:8000"
```

## 教程
[视频演示](https://chilohdata.s3.bitiful.net/videos/tutorial_link.mp4)
1. 搜索“xx appstore”，例如：gitmind appstore。
2. 获取应用ID。例如：[https://apps.apple.com/us/app/gitmind-ai-powered-mind-map/id1566810191](https://apps.apple.com/us/app/gitmind-ai-powered-mind-map/id1566810191)，“1566810191”部分即是应用ID号。
3. 填入应用ID号，选择“语言”，选择要抓取的页数。点击“获取评论”按钮，会拿到一个comments.xlsx的表格。

## 声明

本项目是由个人（Chiloh）为了学习和研究目的开发的工具，旨在探索与研究与 GPT 协作的共创能力。

1. **使用者声明**：使用本项目的个人或组织必须确保其行为符合所在国家和地区的法律法规，不得将本项目用于任何非法用途，包括但不限于未授权的数据访问、侵犯版权或其他知识产权。

2. **数据采集**：使用者在使用本项目时，应当遵循公平使用原则，不得对目标网站进行高频率的数据抓取，以免对网站正常运营造成影响。

3. **责任限制**：本项目开发者不对任何使用者使用本项目而导致的任何形式的直接或间接损失承担责任。使用者应当自行承担使用本爬虫项目可能引起的一切后果和法律责任。

4. **知识产权**：使用者在使用本项目过程中，应当尊重目标网站的版权及相关知识产权。

5. **最终解释权**：对于本免责声明的最终解释权归本项目开发者所有。

本声明的修改和更新不另行通知，使用者使用本项目即视为同意本声明的全部内容。
