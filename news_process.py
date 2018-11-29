# -*- coding=utf-8 -*-
import jieba
import re
from util import *
from collections import Counter
jieba.load_userdict("top_person/person_name")
person_name_set = set(readfile("top_person/person_name"))

# 先用正则将<content>和</content>去掉
def reTest(content):
    reContent = re.sub('<content>|</content>','',content)
    return reContent
    

def news_to_sentence():
    #将新闻语料拆分成单句
    file_lines = readfile_not_strip('sogou_dataset/corpus_content.txt')
    new_sents = []
    for line in file_lines:
        content = reTest(line)
        sentences = re.split('(。|！|\!|\.|？|\?)',content)
        for i in range(int(len(sentences)/2)):
            sent = sentences[2*i] + sentences[2*i+1]
            #print sent       
            line_seg = jieba.cut(sent)
            current_person = set()
            for seg in line_seg:
                if seg.encode("utf-8") in person_name_set:
                    current_person.add(seg.encode("utf-8"))
            if len(current_person) >= 2:
                writefile('sogou_dataset/corpus_seg_all',sent+'\n')
                

def sentence_find_relation():
    #两个人物实体关系
    news_sentences = readfile_not_strip('sogou_dataset/corpus_seg_all')
    person_relations = readfile_not_strip('top_person/relation_distinct')
    #for person_relation in person_relations:
    #    print i.strip().split('\t')
    for sentence in news_sentences:
        line_seg = jieba.cut(sentence.strip())
        count = 0
        current_person = set()
        for seg in line_seg:
            if seg.encode("utf-8") in person_name_set:
                count += 1
                current_person.add(seg.encode("utf-8"))
        current_person = list(current_person)
        if len(current_person) >= 2:
            for person_relation in person_relations:
                person_relation_list = person_relation.strip().split('\t')[:2]
                if current_person[0] in person_relation_list and current_person[1] in person_relation_list: 
                    writefile('sogou_dataset/corpus_relation_all_distinct',person_relation.strip()+'\t'+sentence)
                    break

def relation_to_distinct():
    #去重关系文件
    relation_sentences = readfile_not_strip('sogou_dataset/corpus_relation_all_distinct')
    relation_sentences_new = list(set(relation_sentences))
    writefile('sogou_dataset/relation_final',relation_sentences_new)
                    
def relation_type():
    #统计关系类型的数量
    relation_sentences = readfile_not_strip('sogou_dataset/relation_final')
    relation_list = []
    for relation_sentence in relation_sentences:
        if len(relation_sentence.split('\t')) == 4:
            relation_list.append(relation_sentence.split('\t')[2])
    result = Counter(relation_list)  
    print len(result)
    for key,value in sorted(result.items(), key=lambda d: d[1]):
        print key,value 


if __name__ == '__main__':
    #sentence_find_relation()
    #news_to_sentence()
    relation_type()






