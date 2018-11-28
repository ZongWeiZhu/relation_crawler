#-*- coding=utf-8 -*-
#处理relation文件的相关脚本
#2018.11.26
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import sys
import time
from collections import Counter
from util import *
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def find_top_relation():
    #统计relation文件中的关系类型数量
    lines = readfile('top_person/relation')
    relation_dict = {}
    relation_list = []

    lines_list = list(set(lines))
    print len(lines_list)

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

def relation_distinct():
    #relation去重
    with open('top_person/relation', 'r') as f:
        lines = f.readlines() 
    relation_dict = {}
    relation_list = []

    lines_list = list(set(lines))
    writefile_write('top_person/relation_distinct',lines_list)


def personname_handle():
    #人物中出现特殊符号影响分词 去除
    result = json_load('json/1_person_name12')
    print len(result)
    result_new = []
    for r in result:
        if '·' in r or '•' in r or ' ' in r or '-' in r or '、' in r:
            continue 
        elif r.isdigit():
            continue
        else:
            result_new.append(r+'\n')
    writefile_write('top_person/person_name',result_new)

if __name__=="__main__":
    personname_handle()




