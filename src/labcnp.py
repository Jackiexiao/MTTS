# -- encoding: utf-8 --
from __future__ import unicode_literals
import copy


class LabNode(object):
    def __init__(self,
                 lbrother=None,
                 rbrother=None,
                 father=None,
                 sons=[],
                 sons_num=0,
                 txt='',
                 rhythm='',
                 index=0,
                 pos=''):
        self.lbrother = lbrother
        self.rbrother = rbrother
        self.father = father
        self.sons = sons
        self.sons_num = sons_num
        self.txt = txt
        self.rhythm = rhythm
        self.index = index
        self.pos = pos
        if (sons):
            self._set_sons()
        #print('add a new node of : {}'.format(txt))

    def _set_sons(self):
        """设置son的father为自己，统计sons的个数，根据son更新自己的txt"""
        for son in self.sons:
            son.father = self
        self.sons_num = len(self.sons)
        if self.rhythm.startswith('#') and self.rhythm != '#0':
            self.txt = ''.join(son.txt for son in self.sons)


Lab = ['t', 'p', 'a', 'b', 'c', 'd', 'e', 'f']

formation=[
    ' ', ' ', 
    '^', '-', '+', '=', '@', '@/A:', 
    '-', '^', '@/B:', 
    '+', '@', '^', '^', '+', '#', '-', '-/C:', 
    '_', '^', '#', '+', '+', '&/D:', 
    '=', '!', '@', '-', '&/E:', 
    '|', '-', '@', '#', '&', '!', '-', '#/F:', 
    '^', '=', '_', '-', '!']

class LabGenerator(object):
    def __init__(self, phone, rhythms, times=None):
        assert phone.rhythm == 'ph'
        self.phone = copy.deepcopy(phone)
        self.adict = {}
        self.rhythms = rhythms
        self.times = times

    def __iter__(self):
        while self.phone:
            self.t()
            self.p()
            self.a()
            self.b()
            self.c()
            self.d()
            self.e()
            self.f()
            lablist = []
            for lab in Lab:
                lablist.extend(self.adict[lab])
            assert len(lablist) == len(formation)
            yield ''.join(
                [lab + form for lab, form in zip(lablist, formation)])
            self.phone = self.phone.rbrother

    def t(self):
        """
        发音时长
        """
        assert len(self.times) >= 2
        self.adict['t'] = [str(self.times[0]), str(self.times[1])]
        del self.times[0]

    def p(self):
        """
        p1  |  前前基元
        p2  |  前一基元
        p3  |  当前基元
        p4  |  后一基元
        p5  |  后后基元
        p6  |  当前音节的元音
        """
        self.adict['p'] = ['xx'] * 6
        self.adict['p'][2] = self.phone.txt
        if self.phone.lbrother:
            self.adict['p'][1] = self.phone.lbrother.txt
            if self.phone.lbrother.lbrother:
                self.adict['p'][0] = self.phone.lbrother.lbrother.txt

        if self.phone.rbrother:
            self.adict['p'][3] = self.phone.rbrother.txt
            if self.phone.rbrother.rbrother:
                self.adict['p'][4] = self.phone.rbrother.rbrother.txt
        
        if self.phone.father:
            self.adict['p'][5] = self.phone.father.sons[-1].txt.rstrip('12345')

    def a(self):
        """
        a1  |  前一音节/字的声调
        a2  |  当前音节/字的声调
        a3  |  后一音节/字的声调
        """
        self.adict['a'] = ['xx'] * 3
        father = self.phone.father
        if father:
            self.adict['a'][1] = father.txt[-1]
            if father.lbrother:
                self.adict['a'][0] = father.lbrother.txt[-1]
            if father.rbrother:
                self.adict['a'][2] = father.rbrother.txt[-1]

    def b(self):
        """
        b1  |  当前音节/字到语句开始字的距离
        b2  |  当前音节/字到语句结束字的距离
        b3  |  当前音节/字在词中的位置（正序）
        b4  |  当前音节/字在词中的位置（倒序）
        b5  |  当前音节/字在韵律词中的位置（正序）
        b6  |  当前音节/字在韵律词中的位置（倒序）
        b7  |  当前音节/字在韵律短语中的位置（正序）
        b8  |  当前音节/字在韵律短语中的位置（倒序）
        """
        self.adict['b'] = ['xx'] * 8
        # 音节层
        father = self.phone.father
        if father:
            # 词层
            gfather = father.father
            self.adict['b'][2] = str(father.index)
            self.adict['b'][3] = str(gfather.sons_num - father.index + 1)
            # 韵律词层
            ggfather = gfather.father
            total = len(ggfather.txt)
            order = sum(
                len(son.txt)
                for son in ggfather.sons[0:gfather.index - 1]) + father.index
            self.adict['b'][4] = str(order)
            self.adict['b'][5] = str(total - order + 1)
            # 韵律短语层
            gggfather = ggfather.father
            total = len(gggfather.txt)
            order = sum(
                len(son.txt)
                for son in gggfather.sons[0:ggfather.index - 1]) + order
            self.adict['b'][6] = str(order)
            self.adict['b'][7] = str(total - order + 1)
            left = 0
            while father.lbrother:
                left = left + 1
                father = father.lbrother
            self.adict['b'][0] = str(left)
            self.adict['b'][1] = str(
                len(gggfather.father.father.txt) - left - 1)

    def c(self):
        """
        c1  |  前一个词的词性
        c2  |  当前词的词性
        c3  |  后一个词的词性
        c4  |  前一个词的音节数目
        c5  |  当前词中的音节数目
        c6  |  后一个词的音节数目
        """
        self.adict['c'] = ['xx'] * 6
        father = self.phone.father
        if father:
            gfather = father.father
            self.adict['c'][1] = gfather.pos
            self.adict['c'][4] = str(len(gfather.txt))
            if gfather.lbrother:
                self.adict['c'][0] = gfather.lbrother.pos
                self.adict['c'][3] = str(len(gfather.lbrother.txt))
            if gfather.rbrother:
                self.adict['c'][2] = gfather.rbrother.pos
                self.adict['c'][5] = str(len(gfather.rbrother.txt))

    def d(self):
        """
        d1  |  前一个韵律词的音节数目
        d2  |  当前韵律词的音节数目
        d3  |  后一个韵律词的音节数目
        d4  |  当前韵律词在韵律短语的位置（正序）
        d5  |  当前韵律词在韵律短语的位置（倒序）
        """
        self.adict['d'] = ['xx'] * 5
        # 音节层
        father = self.phone.father
        if father:
            # 韵律词层
            gfather = father.father.father
            self.adict['d'][1] = str(len(gfather.txt))
            if gfather.lbrother:
                self.adict['d'][0] = str(len(gfather.lbrother.txt))
            if gfather.rbrother:
                self.adict['d'][2] = str(len(gfather.rbrother.txt))
            self.adict['d'][3] = str(gfather.index)
            self.adict['d'][4] = str(gfather.father.sons_num -
                                       gfather.index + 1)

    def e(self):
        """
        e1  |  前一韵律短语的音节数目
        e2  |  当前韵律短语的音节数目
        e3  |  后一韵律短语的音节数目
        e4  |  前一韵律短语的韵律词个数
        e5  |  当前韵律短语的韵律词个数
        e6  |  后一韵律短语的韵律词个数
        e7  |  当前韵律短语在语句中的位置（正序）
        e8  |  当前韵律短语在语句中的位置（倒序）
        """
        self.adict['e'] = ['xx'] * 8
        father = self.phone.father
        if father:
            # 韵律短语层
            gfather = father.father.father.father
            self.adict['e'][1] = str(len(gfather.txt))
            self.adict['e'][4] = str(gfather.sons_num)
            if gfather.lbrother:
                self.adict['e'][0] = str(len(gfather.lbrother.txt))
                self.adict['e'][3] = str(gfather.lbrother.sons_num)
            if gfather.rbrother:
                self.adict['e'][2] = str(len(gfather.rbrother.txt))
                self.adict['e'][5] = str(gfather.rbrother.sons_num)
            total = sum(son.sons_num for son in gfather.father.father.sons)
            order = sum(son.sons_num for son in gfather.father.father.
                        sons[0:gfather.father.index - 1]) + gfather.index
            self.adict['e'][6] = str(order)
            self.adict['e'][7] = str(total - order + 1)

    def f(self):
        """
        f1  |  语句的语调类型
        f2  |  语句的音节数目
        f3  |  语句的词数目
        f4  |  语句的韵律词数目
        f5  |  语句的韵律短语数目
        """
        self.adict['f'] = ['xx'] * 5
        father = self.phone.father
        if father:
            # 句子层
            gfather = father.father.father.father.father.father
            #self.adict['f'][1]=str(len(gfather.txt))
            self.adict['f'][1] = str(len(gfather.txt))
            self.adict['f'][2] = str(len(self.rhythms))
            temp = [x >= '#1' for x in self.rhythms]
            self.adict['f'][3] = str(sum(map(int, temp)))
            temp = [x >= '#3' for x in self.rhythms]
            self.adict['f'][4] = str(sum(map(int, temp)))
