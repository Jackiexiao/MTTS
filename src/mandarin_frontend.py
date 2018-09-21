#!/usr/bin/python3

# -*- encoding:utf-8 -*-

from __future__ import unicode_literals
import re
import os
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
    insert_time = 0
    length = len(prosody_words[index])
    i = 0
    while i < len(words):
        done = False
        while not done:
            if (len(words[i]) > length):
                #print(words[i], prosody_words[index])
                length += len(prosody_words[index + 1])
                rhythms[index] = ''
                index += 1
            elif (len(words[i]) < length):
                # print(' less than ', words[i], prosody_words[index])
                rhythms.insert(index + insert_time, '#0')
                insert_time += 1
                length -= len(words[i])
                i += 1
            else:
                # print('equal :', words[i])
                # print(rhythms)
                done = True
                index += 1
        else:
            if (index < len(prosody_words)):
                length = len(prosody_words[index])
            i += 1
    if rhythms[-1] != '#4':
        rhythms.append('#4')
    rhythms = [x for x in rhythms if x != '']
    # print(rhythms)
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

    # delete all character which is not number && alphabet && chinese word
    txt = re.sub(r'(?!#)\W', '', txt)

    # If txt with prosody mark, use prosody mark,
    # else use jieba position segmetation
    if '#' in txt:
        words, poses, rhythms = _adjust(txt)
    else:
        txt = re.sub('[,.，。]', '#4', txt)
        words = []
        poses = []
        for word, pos in posseg.cut(txt):
            words.append(word)
            poses.append(pos[0])
        rhythms = ['#0'] * (len(words) - 1)
        rhythms.append('#4')

    syllables = txt2pinyin(''.join(words))

    phone_num = 0
    for syllable in syllables:
        phone_num += len(syllable)  # syllable is like ('b', 'a3')

    if sfsfile:
        phs_type = []
        times = ['0']
        with open(sfsfile) as fid:
            for line in fid.readlines():
                line = line.strip().rstrip('\n')
                assert len(line.split(' ')) == 2, 'check format of sfs file'
                time, ph = line.split(' ')
                times.append(int(float(time)))
                phs_type.extend(ph)
    else:
        phs_type = []
        for i, rhythm in enumerate(rhythms):
            single_word_pinyin = txt2pinyin(words[i])
            single_word_phone_num = sum(
                [len(syllable) for syllable in single_word_pinyin])
            phs_type.extend(['a'] * single_word_phone_num)
            if i != (len(rhythms) - 1) and rhythm == '#4':
                phs_type.append('s')
        '''
        phs_type = ['a'] * phone_num
        '''
        phs_type.insert(0, 's')
        phs_type.append('s')
        times = [0] * (len(phs_type) + 1)
    '''
    for item in words:
        print(item)

    print ('words: ', words)
    print ('rhythms: ',rhythms)
    print ('syllables: ', syllables)
    print ('poses: ', poses)
    print ('phs_type: ', phs_type)
    print ('times: ', times)
    '''

    phone = tree(words, rhythms, syllables, poses, phs_type)
    return LabGenerator(phone, rhythms, times)


def _txt_preprocess(txtfile, output_path):
    # 去除所有标点符号(除非是韵律标注#1符号)，报错，如果txt中含有数字和字母(报错并跳过）
    with open(txtfile) as fid:
        txtlines = [x.strip() for x in fid.readlines()]
    valid_txtlines = []
    error_list = []  # line which contain number or alphabet
    pattern = re.compile('(?!#(?=\d))(?![，。,.])[\W]')
    for line in txtlines:
        num, txt = line.split(' ', 1)
        if bool(re.search('[A-Za-z]', txt)) or bool(
                re.search('(?<!#)\d', txt)):
            error_list.append(num)
        else:
            txt = re.sub('[,.，。]', '#4', txt)
            txt = pattern.sub('', txt)
            # 去除除了韵律标注'#'之外的所有非中文文本, 数字, 英文字符符号
            valid_txtlines.append(num + ' ' + txt)
    if error_list:
        for item in error_list:
            print('line %s contain number and alphabet!!' % item)
        with open(os.path.join(output_path, 'error.log'), 'a+') as fid:
            for item in error_list:
                fid.write('line %s contain number and alphabet!!  \n' % item)

    return valid_txtlines


if __name__ == '__main__':
    txt = '继续把建设有中国特色社会主义事业推向前进'
    print(list(txt2label(txt)))
    """
    import argparse
    parser = argparse.ArgumentParser(description="convert mandarin_txt to label for merlin.")
    parser.add_argument("txtfile",
                        help="Full path to txtfile which each line contain num and txt (seperated by a white space) ")
    parser.add_argument("output_path",
                        help="Full path to output directory, will be created if it doesn't exist")
    parser.add_argument("-s", "--sfs_dir_path", type=str, default=None,
                        help="Full path to sfs directory, won't generate time stamp if it is None")

    args = parser.parse_args()

    os.system('mkdir -p %s' % args.output_path)
    txtlines = _txt_preprocess(args.txtfile, args.output_path)

    for line in txtlines:
        print('processing: ',line)
        numstr, txt = line.split(' ',1)
        '''
        if args.sfs_dir_path:
            sfs_file = os.path.join(args.sfs_dir_path, numstr+'.sfs')
            labresult = txt2label(txt, sfsfile=sfs_file)
        else:
            labresult = txt2label(txt)
        '''
        try:
            if args.sfs_dir_path:
                sfs_file = os.path.join(args.sfs_dir_path, numstr+'.sfs')
                labresult = txt2label(txt, sfsfile=sfs_file)
            else:
                labresult = txt2label(txt)
        except Exception:
            print('Error at %s, please check your txt or sfs file %s' % (numstr, txt))
        else:
            with open(os.path.join(args.output_path, numstr+'.lab'), 'w') as fid:
                    for lab in labresult:
                        fid.write(lab+'\n')
    """
