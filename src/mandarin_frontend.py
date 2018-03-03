#!/usr/bin/python3
# -*- encoding:utf-8 -*-

from __future__ import unicode_literals
import re
from jieba import posseg
from labcnp import LabGenerator
from labformat import tree 
from txt2pinyin import txt2pinyin

def _adjust(prosody_txt):
    '''Make sure that segment word is smaller than prosody word'''
    prosody_words = re.split('#\d', prosody_txt)
    rhythms = re.findall('#\d', prosody_txt)
    txt = ''.join(prosody_words)
    words = []
    poses = []
    for word, pos in posseg.cut(txt):
        words.append(word)
        poses.append(pos[0])
    index = 0
    length = len(prosody_words[index])
    i = 0
    while i < len(words):
        done = False
        while not done:
            if(len(words[i]) > length):
                del rhythms[0]
                length += len(prosody_words[index+1])
                index += 1
            elif(len(words[i]) < length):
                rhythms.insert(1, '#0')
                length -= len(words[i])
                i += 1
            else:
                done = True
                index += 1
        else:
            if(index < len(prosody_words)):
                length = len(prosody_words[index])
            i += 1
    rhythms.append('#4')
    return (words, poses, rhythms)


def txt2label(txt, sfsfile=None, style='default'):
    '''Return a generator of HTS format label of txt.
    
    Args:
        txt: like raw txt "向香港特别行政区同胞澳门台湾同胞"
             or txt with prosody make like "向#1香港#2特别行政区#1同胞#3澳门台湾#1同胞",
             punctuation is also allow in txt
        sfsfile: absolute path of sfs file (alignment file). A sfs file
            example(measure time by 10e-7 second, 12345678 means 1.2345678
            second)
            --------
            239100 s 
            313000 a 
            323000 d
            400000 b 
            480000 s 
            ---------
            a stands for consonant
            b stands for vowel
            d stands for silence that is shorter than 100ms
            s stands for silence that is longer than 100ms
        style: label style, currently only support the default HTS format
        
    Return:
        A generator of phone label for the txt, convenient to save as a label file
    '''
    assert style == 'default', 'Currently only default style is support in txt2label'

    # del all Chinese punctuation 
    punctuation = "·！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
    #punctuation  = punctuation.decode("utf-8")
    txt = re.sub(r'[%s]'%punctuation, '', txt)
    #txt = re.sub(r'[%s]'%punctuation, '', txt.decode('utf-8')).encode('utf-8')

    # If txt with prosody mark, use prosody mark,
    # else use jieba position segmetation
    if '#' in txt:
        words, poses, rhythms = _adjust(txt)
    else:
        words = []
        poses = []
        for word, pos in posseg.cut(txt):
            words.append(word)
            poses.append(pos[0])
        rhythms = ['#0']*(len(words)-1)
        rhythms.append('#4')

    syllables = txt2pinyin(''.join(words))

    phone_num = 0
    for syllable in syllables:
        phone_num += len(syllable) 

    if sfsfile:
        phs_type = []
        times = ['0']
        with open(sfsfile) as fid:
            for line in fid.readlines():
                line = line.strip().rstrip('\n')
                assert len(line.split(' ')) == 2, 'check format of sfs file'
                time, ph = line.split(' ')
                times.append(int(time))
                phs_type.extend(ph)
    else:
        length = 0
        for syllable in syllables:
            length += len(syllable) 
        phs_type = ['a'] * phone_num
        phs_type.insert(0, 's')
        phs_type.append('s')
        times = [0] * (phone_num + 3)

    '''
    for item in words:
        print(item)

    print (words)
    print (rhythms)
    print (syllables)
    print (poses)
    print (phs_type)

    '''
    phone = tree(words, rhythms, syllables, poses, phs_type)
    return LabGenerator(phone, rhythms, times)

if __name__ == '__main__':
    # 用法举例
    input_txt = '向香港特别行政区同胞澳门和台湾同胞海外侨胞'
    print(type(input_txt))
    result = txt2label(input_txt)


    '''
    带韵律标记的文本也被支持
    result = txt2label('向#1香港#2特别#1行政区#1同胞#4澳门#2和#1台湾#1同胞#4海外#1侨胞')

    可加入发音时长文件
    result = txt2label('向#1香港#2特别#1行政区#1同胞#4澳门#2和#1台湾#1同胞#4海外#1侨胞',
            sfsfile='../example_file/example.sfs')

    注意
    文本中的所有中文标点符号会被删除
    '''

    for line in result:
        print(line)

