#-*- coding=utf-8 -*-
#top关系对
#2018.11.26
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

if __name__=="__main__":

	lines = readfile('top_person/test1')
	relation_dict = {}
	relation_list = []

	lines_list = list(set(lines))

	for line in lines_list:
		try:
			relation = line.split('\t')[2]
		except IndexError:
			continue
		relation_list.append(relation)
	result = Counter(relation_list)
	#items = result.items()
	
	print len(result)
	for key,value in sorted(result.items(), key=lambda d: d[1]):
		print key,value


