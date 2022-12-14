# -*- coding: utf-8 -*-
"""dse_news-scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/159lQwVjwbuMP-P3wtusZCMxo1gjaMMOp
"""

!pip install requests-html

from requests_html import HTMLSession

session = HTMLSession()

for year in range(2020,2023):
  url = f"https://dsebd.org/old_news.php?startDate={year}-01-01&endDate={year}-12-30&criteria=4&archive=news"
  print(url)
  r = session.get(url)
  # with open("june_news.html", "w") as jun:
  #   jun.write(r.text)
  dse_news = r.html.find(".table-news")[0].text
  dse_news_lst = dse_news.split('\n')
  trading_code = dse_news_lst[1::8]
  news_title = dse_news_lst[3::8]
  news = dse_news_lst[5::8]
  post_date = dse_news_lst[7::8]
  with open(f"{year}_news.txt", "w") as f:
    f.write("No, Trading Code, News Title, News, Post Date\n")
    for i, t, nt, n, p in zip(range(1, len(trading_code)+1), trading_code, news_title, news, post_date):
      f.write(f"{i}, {t}, {nt}, {n}, {p}")
      f.write('\n')

session = HTMLSession()

from google.colab import drive
drive.mount('/content/drive')

