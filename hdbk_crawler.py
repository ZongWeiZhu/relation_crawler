#-*- coding=utf-8 -*-
#爬去互动百科人物关系信息
#2018.11.25
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import sys
import time
from collections import Counter
from util import *
reload(sys)
sys.setdefaultencoding('utf-8')
logger = log() #全局日志变量


def crawler_realtion(url,s,flag,length_down):
	#得到人物关系下栏的人物关系信息
	#返回下栏长度作为上栏的参照 上栏爬取的行数为 len_total - len_down
	person = []
	relation = []
	f = requests.get(url)
	soup = BeautifulSoup(f.content, "lxml")

	length = 0
	if flag == 'down':
		
		div = soup.find_all('div',class_='text_dir')
		if len(div) == 0:
			return 0,[],[]
		a =  div[0].find_all('a',target = '_blank')
		length = len(a)
	else:
		
		div = soup.find_all('div',id='figurerelation')
		if len(div) == 0:
			return 0,[],[]
		a =  div[0].find_all('a',target = '_blank')
		length = len(a) - length_down
	
	li = div[0].find_all('li')
	for i in range(length):
		#print li[i].get_text().strip().replace(a[i].string,'')
		relation.append(li[i].get_text().strip().replace(a[i].string,''))
		if '[' in a[i].string:
			#print a[i].string
			index = a[i].string.index('[')
			#print a[i].string[:index]
			person.append(a[i].string[:index])
		else:
			#print a[i].string
			person.append(a[i].string)
	return len(a),person,relation


def center_person_crawler():
	#用中心人物爬取与其有关系的用加入到集合（字典），并循环爬取其关系人物
	person_list = readfile('top_person/test')
	person_dict = {}
	for person in person_list:
		if person not in person_dict:
			person_dict[person] = 0
	count = 0
	while count <2:
		print "rount %d"%count
		if 0 not in person_dict.values():
			break		
		for key,value in person_dict.items():

			logger.info(key)
			if value == 1:
				logger.info("已爬取")
				continue

			url = 'http://www.baike.com/wiki/'+key
			logger.info(url)

			write_content = []
			if '[' in key:
				index = key.index('[')
				key = key[:index]

			len_down,person,relation = crawler_realtion(url,key,'down',0)
			for i in range(len_down):
				write_content.append(key.strip()+'\t'+person[i].strip()+'\t'+relation[i].strip()+'\n')
				if person[i] not in person_dict:
					person_dict[person[i]] = 0

			len_up,person,relation = crawler_realtion(url,key,'up',len_down)
			for i in range(len_up-len_down):
				write_content.append(person[i].strip()+'\t'+key.strip()+'\t'+relation[i].strip()+'\n')
				if person[i] not in person_dict:
					person_dict[person[i]] = 0
			rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
			writefile('top_person/'+rq+'_relation',write_content)
			person_dict[key] = 1
		result = Counter(person_dict.values())
		logger.info(result)	
		count += 1
	

if __name__=="__main__":
	center_person_crawler()


















