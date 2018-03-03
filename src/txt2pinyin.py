# -*- encoding: UTF-8 -*-
from __future__ import unicode_literals
import sys
import re
from pypinyin import pinyin, Style, load_phrases_dict

consonant_list = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k',
                  'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z',
                  'c', 's', 'y', 'w']

def _pre_pinyin_setting():
    ''' fix pinyin error'''
    load_phrases_dict({'嗯':[['ēn']]})


def pinyinformat(syllabel):
    '''format pinyin to system's format''' 
    translate_dict = {'ju':'jv', 'qu':'qv', 'xu':'xv', 'zi':'zic',
                      'ci':'cic', 'si':'sic', 'zhi':'zhih', 
                      'chi':'chih', 'shi':'shih', 'ri':'rih',
                      'yuan':'yvan', 'yue':'yve', 'yun':'yvn',
                      'iu':'iou', 'ui':'uei', 'un':'uen'}
    translate_dict_more = {'ya':'yia', 'ye':'yie', 'yao':'yiao',
                           'you':'yiou', 'yan':'yian', 'yin':'yin',
                           'yang':'yiang', 'ying':'ying', 'yong':'yiong',
                           'wa':'wua', 'wo':'wuo', 'wai':'wuai',
                           'wei':'wuei', 'wan':'wuan', 'wen':'wuen',
                           'weng':'wueng', 'wang':'wuang'}
    translate_dict_less = {'ya':'ia', 'ye':'ie', 'yao':'iao',
                           'you':'iou', 'yan':'ian', 'yin':'in',
                           'yang':'iang', 'ying':'ing', 'yong':'iong',
                           'wa':'ua', 'wo':'uo', 'wai':'uai',
                           'wei':'uei', 'wan':'uan', 'wen':'uen',
                           'weng':'ueng', 'wang':'uang'}
 
    #必须先替代yun为yvn，然后再是替代un为uen
    for key, value in translate_dict.items():
        syllabel = syllabel.replace(key, value)
    for key, value in translate_dict_more.items():
        syllabel = syllabel.replace(key, value)
    if not syllabel[-1].isdigit():
        syllabel = syllabel + '5'
    return syllabel


def seprate_syllabel(syllabel):
    '''seprate syllable to consonant + ' ' + vowel '''
    assert syllabel[-1].isdigit()
    if syllabel[0:2] in consonant_list:
        #return syllabel[0:2].encode('utf-8'),syllabel[2:].encode('utf-8')
        return syllabel[0:2], syllabel[2:]
    elif syllabel[0] in consonant_list:
        #return syllabel[0].encode('utf-8'),syllabel[1:].encode('utf-8')
        return syllabel[0], syllabel[1:]
    else:
        #return (syllabel.encode('utf-8'),)
        return (syllabel,)


def txt2pinyin(txt):
    _pre_pinyin_setting()
    phone_list = []
    '''
    if isinstance(txt, str):
        pinyin_list = pinyin(unicode(txt,'utf-8'), style = Style.TONE3)
    elif isinstance(txt, unicode):
        pinyin_list = pinyin(txt, style = Style.TONE3)
    else:
        print('error: unsupport coding form')
    '''

    pinyin_list = pinyin(txt, style = Style.TONE3)
    for item in pinyin_list:
        phone_list.append(seprate_syllabel(pinyinformat(item[0])))
    return phone_list

if __name__ == '__main__':
	print(txt2pinyin('你好看啊'))



'''
用法举例
print(txt2pinyin('中华人民共和国论居然'))
['zh ong1', 'h ua2', 'r en2', 'm in2', 'g ong4', 'h e2', 'g uo2', 'l uen4', 'j
v1', 'r an2']
'''


