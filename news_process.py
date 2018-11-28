# -*- coding=utf-8 -*-
import jieba
import re
from util import *
jieba.load_userdict("top_person/person_name")

# 先用正则将<content>和</content>去掉
def reTest(content):
  reContent = re.sub('<content>|</content>','',content)
  return reContent

if __name__ == '__main__':
  file_lines = readfile_not_strip('sogou_dataset/corpus_test.txt')
  new_sents = []
  for line in file_lines[:5]:
    content = reTest(line)
    sentences = re.split('(。|！|\!|\.|？|\?)',content)
    
    for i in range(int(len(sentences)/2)):
        sent = sentences[2*i] + sentences[2*i+1]
        
        line_seg = jieba.cut(sent)
        print type(' '.join(line_seg))
        writefile('sogou_dataset/corpus_seg',' '.join(line_seg).encode('utf-8').strip()+'\n')













