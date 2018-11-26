#-*- coding=utf-8 -*-
#爬取百度百科人物榜信息
#http://top.baidu.com/buzz?b=612&c=9&fr=topbuzz_b260_c9
#2018.11.22
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def crawler(url):
	f = requests.get(url)

	soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
	a = soup.find_all('a',class_='list-title')
	return a


if __name__=="__main__":
	url_list = ['http://top.baidu.com/buzz?b=260&c=9&fr=topbuzz_b255_c9',
				'http://top.baidu.com/buzz?b=612&c=9&fr=topbuzz_b260_c9',
				'http://top.baidu.com/buzz?b=261&c=9&fr=topbuzz_b612_c9',
				'http://top.baidu.com/buzz?b=255&c=9&fr=topbuzz_b261_c9',
				'http://top.baidu.com/buzz?b=454&c=9&fr=topbuzz_b255_c9',
				'http://top.baidu.com/buzz?b=259&c=9&fr=topbuzz_b454_c9',
				'http://top.baidu.com/buzz?b=257&c=9&fr=topbuzz_b259_c9',
				'http://top.baidu.com/buzz?b=1570&c=9&fr=topbuzz_b257_c9',
				'http://top.baidu.com/buzz?b=1569&c=9&fr=topbuzz_b1570_c9',
				'http://top.baidu.com/buzz?b=491&c=9&fr=topbuzz_b1569_c9']
	f1 = open('./top_person/person.txt', 'w')
	lasting = []
	for url in url_list:
		result = crawler(url)
		for r in result:
			text = r.get_text()
			if text != '':
				lasting.append(text.strip()+'\n')

	
	f1.writelines(lasting)















