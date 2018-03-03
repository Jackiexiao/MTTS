# -- encoding: utf-8 --
from __future__ import unicode_literals
import re
import copy
from sys import exit
from txt2pinyin import txt2pinyin
from labcnp import LabNode, LabGenerator

rhythm_map={'ph':'phone', 'syl':'syllable', '#0':'rhythm0', '#1':'rhythm1_2', '#2':'rhythm1_2', '#3':'rhythm3', '#4':'rhythm4'}

def tree_per_word(word, rhythm, tree_init, syllables, poses):
    def get_list(rhythm):
        return tree_init[rhythm_map[rhythm]]
    
    assert rhythm in rhythm_map
    rhythm_list = get_list(rhythm)

    if rhythm == 'ph':
        pass

    elif rhythm == 'syl':
        pre_rhythm = 'ph'
        for phones in syllables[0]:
            tree_per_word(phones, pre_rhythm, tree_init, syllables, poses)
        del syllables[0]

    elif rhythm == '#0':
        pre_rhythm = 'syl'
        for syllable in syllables[0:len(word)]:
            tree_per_word(''.join(syllable), pre_rhythm, tree_init, syllables, poses)
    
    elif rhythm in ['#1', '#2']:
        pre_rhythm = '#0'
        tree_per_word(word, pre_rhythm, tree_init, syllables, poses)

    elif rhythm == '#3':
        pre_rhythm = '#1'
        tree_per_word(word, pre_rhythm, tree_init, syllables, poses)

    elif rhythm == '#4':
        pre_rhythm = '#3'
        tree_per_word(word, pre_rhythm, tree_init, syllables, poses)
    
    else:
        print('error rhythm input')
        exit(-1)

    if rhythm == 'ph':
        newLab=LabNode(txt=word, index=len(rhythm_list) + 1, rhythm=rhythm)

    else:
        newLab = LabNode(sons=get_list(pre_rhythm), txt = word, index = len(rhythm_list) + 1, rhythm=rhythm)
        tree_init['assist'][rhythm_map[pre_rhythm]] = get_list(pre_rhythm)[-1]
        tree_init[rhythm_map[pre_rhythm]] = []
        newLab.adjust()
    
    if rhythm == '#0':
        newLab.pos=poses[0][0]
        del poses[0]

    if len(rhythm_list)!=0:
        newLab.lbrother = rhythm_list[-1]
        rhythm_list[-1].rbrother = newLab
    elif tree_init['assist'][rhythm_map[rhythm]]:
        newLab.lbrother=tree_init['assist'][rhythm_map[rhythm]]
        tree_init['assist'][rhythm_map[rhythm]].rbrother=newLab
    rhythm_list.append(newLab)


def show(tree_list, shift=0):
    for item in tree_list:
        print ('|\t'*shift + str(item.index) + '\t' + item.txt + '\t' +
                item.rhythm + '\t' + str(item.sons_num) + '\t' + item.pos)
        show(item.sons, shift + 1)


def tree(words, rhythms, syllables, poses, phs_type=None):
    assert len(words) == len(rhythms)
    assert len(words) == len(poses)
    assert len(''.join(words)) == len(syllables)
    tree_init={'assist':{}}
    for key, value in rhythm_map.items():
        tree_init[value]=[]
        tree_init['assist'][value]=None
    # print(tree_init)
    syllables_copy=copy.deepcopy(syllables)
    poses_copy=copy.deepcopy(poses)
    for word, rhythm in zip(words, rhythms):
        tree_per_word(word, rhythm, tree_init, syllables_copy, poses_copy)
    newLab=LabNode(sons=tree_init[rhythm_map['#4']], index=1, rhythm='#5')
    if phs_type:
        newLab.adjust()
    # print(tree_init['rhythm4'])
    # show([newLab], 0)
    # show(tree_init['rhythm4'], 0)
    def get_first():
        return tree_init['rhythm4'][0].sons[0].sons[0].sons[0].sons[0].sons[0]
    
    def adjust():
        fphone=get_first()
        if phs_type[0] == 's':
            newLab=LabNode(txt='sil', rhythm='ph')
            newLab.rbrother=fphone
            fphone.lbrother=newLab
            fphone=newLab
        phone=fphone
        for ptype in phs_type[1:-1]:
            assert phone is not None
            if ptype in ['s', 'd']:
                if ptype == 's':
                    newLab=LabNode(txt='pau', rhythm='ph')
                else:
                    newLab=LabNode(txt='sp', rhythm='ph')
                newLab.rbrother=phone.rbrother
                newLab.lbrother=phone
                phone.rbrother=newLab
                newLab.rbrother.lbrother=newLab
                phone=newLab
            else:
                phone=phone.rbrother
        assert phone is not None
        #assert phone.rbrother is None
        #if phs_type[-1] == 's':
        if phs_type[-1] in ['s', 'd']:
            phone.rbrother=LabNode(txt='sil', rhythm='ph')
            phone.rbrother.lbrother=phone
        return fphone

    return adjust()

if __name__ == '__main__':
    #txt='继续#1把#1建设#2有#1中国#1特色#3社会#1主义#1事业#4推向#1前进'
    txt='继续把建设有中国特色社会主义事业推向前进'
    times=[0,  264200,  360650,  492100,  596550,  737200,  774550,  989300,  1048049,  1211600,  1295550,  1417500,  1483700,  1644000,  1685300,  1719600,  1894300,  1933800,  2065200,  2156650,  2279300,  2370850,  2556100,  2583600,  2703700,  2785200,  2873050,  2992500,  3035150,  3140490,  3198140,  3284050,  3415750,  3507100,  3622700,  3766000,  3862800,  3984500,  4126900,  4213200,  4408500,  4527250,  4703800,  4757350,  4931700,  52253061]
    phs_type=['s',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'd',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'd',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  's',  'a',  'b',  'a',  'b',  'a',  'b',  'a',  'b',  's']
    words=re.split('#\d', txt)
    syllables=txt2pinyin(''.join(words))
    rhythms=re.findall('#\d', txt)
    rhythms.append('#4')
    print(' '.join(words))
    print(rhythms)
    print(syllables)
    poses=['n']*len(words)
    phone=tree(words, rhythms, syllables, poses, phs_type)

    for ph_list in LabGenerator(phone, rhythms, times):
        print(ph_list)


