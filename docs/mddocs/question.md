# 问题集示例

设置此中文上下文标注和对应问题集时参考了 
* [HTS label](http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf)
* [Merlin Questions](https://github.com/CSTR-Edinburgh/merlin/tree/master/misc/questions)
* [本项目使用的上下文相关标注](https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/mandarin_label.md)

问题集中的中英文对照

* initial：声母
* final: 韵母
* syllable(abbr: syl): 音节
* character: 字
* word : 词
* prosodic word: 韵律词
* prosodic phrase: 韵律短语
* intonational phrase: 语调短语

### 问题集设计规则

问题集的设计依赖于不同语言的语言学知识，而且与上下文标注文件相匹配，改变上下文标注方法也需要相应地改变问题集，对于中文语音合成而言，问题集的设计的规则有:
* 前前个，前个，当前，下个，下下个声韵母分别是某个合成基元吗，合成基元共有65个，例如判断是否是元音a QS "LL-a" QS "L-a" QS "C-a" QS "R-a" QS "RR-a"
* 声母特征划分，例如声母可以划分成塞音，擦音，鼻音，唇音等，声母特征划分24个
* 韵母特征划分，例如韵母可以划分成单韵母，复合韵母，分别包含aeiouv的韵母，韵母特征划分8个
* 其他信息划分，词性划分，26个词性; 声调类型，5个; 是否是声母或者韵母或者静音，3个
* 韵律特征划分，如是否是重音，重音和韵律词/短语的位置数量
* 位置和数量特征划分

### 可能的改进
问题集中基元加上声调，例如
```
QS "C-a1"
```

### 问题集的优化

问题集中问题的数量并不是越多越好（经验之谈），具体优化方法[todo]

### 声母的划分特征

划分特征  | 描述    | 基元列表
-------- | ------- | -------
Stop|塞音|b, d, g, p, t, k
Aspirated Stop|塞送气音|b，d，g
Unaspirated Stop|非塞送气音|P，t,k
Affricate|塞檫音|z，zh，j，c，ch，q
Aspirated Affricate|塞擦送气音|z，zh，j
Unaspirated Affricate|非塞檫送气音|c，ch，q
Fricative|擦音|f，s，sh，x, h，r
Fricative2|擦音2|f，s, sh，x，h，r，k
Voiceless Fricative|清檫音|f，s，sh，x，h
Voice Fricative|浊擦音|r，k
Nasal|鼻音|m, n
Nasal2|鼻音2|m, n, l
Labial|唇音|b，p，m
Labial2|唇音2|b，p，m，f
Apical|顶音|z，c，s，d，t，n，l，zh，ch，sh，r
Apical Front|顶前音|z，c，s
Apical 1|顶音1|d，t，n，l
Apical2|顶音2|d，t
Apical3|顶音3|n，l
Apical End|顶后音1|zh，ch，sh，r
Apical End2|顶后音2|zh，ch, sh
Tongue Top|舌前音|j，q，x
Tongue Root|舌根音|g, k，h
Zero|零声母|y w

### 韵母的划分特征

划分特征|描述|基元列表
-------- | ------- | -------
Simple_Final|单韵母|a，i，u，e，ea, o，v, ic，ih, er
Compound_Final|复韵母| ai、ei、ao、ou、ia、ie、ua、uo、 ve、iao 、iou、uai、uei
Nasal_Vowel|鼻韵母| an、ian、uan、 van 、en、in、uen、 vn 、ang、iang、uang、eng、ing、ueng、ong、iong
Anterior_Nasal_Vowel|前鼻韵母|an、ian、uan、 van 、en、in、uen、 vn
Posterior_Nasal_Vowel|后鼻韵母|ang、iang、uang、eng、ing、ueng、ong、iong
Type A|含有a的韵母|a, ia, an, ang, ai, ua, ao
Type E|含有e的韵母|e，ie，ve，ei, uei, ea, er
Type I|含有I的韵母|i，ai，ei，uei, ia, ian, iang，iao， ie, in, ing, iong, iou
Type O|含0的韵母|o, ao, uo, ou, ong, iou
Type U|含u的韵母|u, ua, uen, ueng, uo, iou
Type V|含V的韵母|v，vn, ve

### 声韵母
Initial|声母| b p m f d t n l g k h j q x zh ch sh r z c s y w 
Final|韵母|a、o、e、ea、i、u、v、ic、ih、er、ai、ei、ao、ou、ia、ie、ua、uo、 ve、iao 、iou、uai、uei、an、ian、uan、 van 、en、in、uen、 vn 、ang、iang、uang、eng、ing、ueng、ong、iong
Silence|静音| sil, pau, sp

### 位置数量，韵律特征问题

主要参见上下文相关标注进行对应的问题集设计

### 重音

如果考虑重音，下面关于重音的示例问题，可以参照 `HTS label <http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf>`_ 以及 `Merlin Questions <https://github.com/CSTR-Edinburgh/merlin/tree/master/misc/questions>`_ 设计相关的数量，位置问题

例如
* 前后、当下基元是否是重音
* 韵律短语中，当前音节前面的重音有多少个
* 重音的位置

#问题集
  
### 韵母  
QS "C-Simple_Final"  
QS "C-Compound_Final"  
QS "C-Nasal_Vowel"
QS "C-Anterior_Nasal_Vowel"
QS "C-Posterior_Nasal_Vowel"
QS "C-TypeA"  
QS "C-TypeE"  
QS "C-TypeI"  
QS "C-TypeO"  
QS "C-TypeU"  
QS "C-TypeV"  

### 声母  
QS "C-Stop"  
QS "C-Aspirated_Stop"  
QS "C-Unaspirated_Stop"  
QS "C-Affricate"  
QS "C-Aspirated_Affricate"  
QS "C-Unaspirated_Affricate"  
QS "C-Fricative"  
QS "C-Fricative2"  
QS "C-Voiceless_Fricative"  
QS "C-Voice_Fricative"  
QS "C-Nasal"  
QS "C-Nasal2"  
QS "C-Labial"  
QS "C-Labial2"  
QS "C-Apical"  
QS "C-Apical_Front"  
QS "C-Apical1"  
QS "C-Apical2"  
QS "C-Apical3"  
QS "C-Apical_End"  
QS "C-Apical_End2"  
QS "C-Tongue_Top"  
QS "C-Tongue_Root"  
QS "C-Zero"  
    
    
### 判断是否是声母，韵母，精音(sil+pau+sp)  
QS "C-initial"  
QS "C-final"  
QS "C-silence"  
QS "L-initial"  
QS "L-final"  
QS "L-silence"  
QS "R-initial"  
QS "R-final"  
QS "R-silence"  
        
### 词性部分  
QS "C-POS==a"  
QS "C-POS==b"  
QS "C-POS==c"  
QS "C-POS==d"  
QS "C-POS==e"  
QS "C-POS==f"  
QS "C-POS==g"  
QS "C-POS==h"  
QS "C-POS==i"  
QS "C-POS==j"  
QS "C-POS==k"  
QS "C-POS==l"  
QS "C-POS==m"  
QS "C-POS==n"  
QS "C-POS==o"  
QS "C-POS==p"  
QS "C-POS==q"  
QS "C-POS==r"  
QS "C-POS==s"  
QS "C-POS==t"  
QS "C-POS==u"  
QS "C-POS==v"  
QS "C-POS==w"  
QS "C-POS==x"  
QS "C-POS==y"  
QS "C-POS==z"  
    
    
### 合成基元部分  
QS "C-b"  
QS "C-p"  
QS "C-m"  
QS "C-f"  
QS "C-d"  
QS "C-t"  
QS "C-n"  
QS "C-l"  
QS "C-g"  
QS "C-k"  
QS "C-h"  
QS "C-j"  
QS "C-q"  
QS "C-x"  
QS "C-zh"  
QS "C-ch"  
QS "C-sh"  
QS "C-r"  
QS "C-z"  
QS "C-c"  
QS "C-s"  
QS "C-y"  
QS "C-w"  
QS "C-a"  
QS "C-o"  
QS "C-e"  
QS "C-ea"  
QS "C-i"  
QS "C-u"  
QS "C-v"  
QS "C-ic"  
QS "C-ih"  
QS "C-er"  
QS "C-ai"  
QS "C-ei"  
QS "C-ao"  
QS "C-ou"  
QS "C-ia"  
QS "C-ie"  
QS "C-ua"  
QS "C-uo"  
QS "C-ve"  
QS "C-iao"  
QS "C-iou"  
QS "C-uai"  
QS "C-uei"  
QS "C-an"  
QS "C-ian"  
QS "C-uan"  
QS "C-van"  
QS "C-en"  
QS "C-in"  
QS "C-uen"  
QS "C-vn"  
QS "C-ang"  
QS "C-iang"  
QS "C-uang"  
QS "C-eng"  
QS "C-ing"  
QS "C-ueng"  
QS "C-ong"  
QS "C-iong"  
QS "C-sil"  
QS "C-sp"  
QS "C-pau"  
    
QS "L-b"  
QS "L-p"  
QS "L-m"  
QS "L-f"  
QS "L-d"  
QS "L-t"  
QS "L-n"  
QS "L-l"  
QS "L-g"  
QS "L-k"  
QS "L-h"  
QS "L-j"  
QS "L-q"  
QS "L-x"  
QS "L-zh"  
QS "L-ch"  
QS "L-sh"  
QS "L-r"  
QS "L-z"  
QS "L-c"  
QS "L-s"  
QS "L-y"  
QS "L-w"  
QS "L-a"  
QS "L-o"  
QS "L-e"  
QS "L-ea"  
QS "L-i"  
QS "L-u"  
QS "L-v"  
QS "L-ic"  
QS "L-ih"  
QS "L-er"  
QS "L-ai"  
QS "L-ei"  
QS "L-ao"  
QS "L-ou"  
QS "L-ia"  
QS "L-ie"  
QS "L-ua"  
QS "L-uo"  
QS "L-ve"  
QS "L-iao"  
QS "L-iou"  
QS "L-uai"  
QS "L-uei"  
QS "L-an"  
QS "L-ian"  
QS "L-uan"  
QS "L-van"  
QS "L-en"  
QS "L-in"  
QS "L-uen"  
QS "L-vn"  
QS "L-ang"  
QS "L-iang"  
QS "L-uang"  
QS "L-eng"  
QS "L-ing"  
QS "L-ueng"  
QS "L-ong"  
QS "L-iong"  
QS "L-sil"  
QS "L-sp"  
QS "L-pau"  
    
    
QS "R-b"  
QS "R-p"  
QS "R-m"  
QS "R-f"  
QS "R-d"  
QS "R-t"  
QS "R-n"  
QS "R-l"  
QS "R-g"  
QS "R-k"  
QS "R-h"  
QS "R-j"  
QS "R-q"  
QS "R-x"  
QS "R-zh"  
QS "R-ch"  
QS "R-sh"  
QS "R-r"  
QS "R-z"  
QS "R-c"  
QS "R-s"  
QS "R-y"  
QS "R-w"  
QS "R-a"  
QS "R-o"  
QS "R-e"  
QS "R-ea"  
QS "R-i"  
QS "R-u"  
QS "R-v"  
QS "R-ic"  
QS "R-ih"  
QS "R-er"  
QS "R-ai"  
QS "R-ei"  
QS "R-ao"  
QS "R-ou"  
QS "R-ia"  
QS "R-ie"  
QS "R-ua"  
QS "R-uo"  
QS "R-ve"  
QS "R-iao"  
QS "R-iou"  
QS "R-uai"  
QS "R-uei"  
QS "R-an"  
QS "R-ian"  
QS "R-uan"  
QS "R-van"  
QS "R-en"  
QS "R-in"  
QS "R-uen"  
QS "R-vn"  
QS "R-ang"  
QS "R-iang"  
QS "R-uang"  
QS "R-eng"  
QS "R-ing"  
QS "R-ueng"  
QS "R-ong"  
QS "R-iong"  
QS "R-sil"  
QS "R-sp"  
QS "R-pau"  
    
    
QS "LL-b"  
QS "LL-p"  
QS "LL-m"  
QS "LL-f"  
QS "LL-d"  
QS "LL-t"  
QS "LL-n"  
QS "LL-l"  
QS "LL-g"  
QS "LL-k"  
QS "LL-h"  
QS "LL-j"  
QS "LL-q"  
QS "LL-x"  
QS "LL-zh"  
QS "LL-ch"  
QS "LL-sh"  
QS "LL-r"  
QS "LL-z"  
QS "LL-c"  
QS "LL-s"  
QS "LL-y"  
QS "LL-w"  
QS "LL-a"  
QS "LL-o"  
QS "LL-e"  
QS "LL-ea"  
QS "LL-i"  
QS "LL-u"  
QS "LL-v"  
QS "LL-ic"  
QS "LL-ih"  
QS "LL-er"  
QS "LL-ai"  
QS "LL-ei"  
QS "LL-ao"  
QS "LL-ou"  
QS "LL-ia"  
QS "LL-ie"  
QS "LL-ua"  
QS "LL-uo"  
QS "LL-ve"  
QS "LL-iao"  
QS "LL-iou"  
QS "LL-uai"  
QS "LL-uei"  
QS "LL-an"  
QS "LL-ian"  
QS "LL-uan"  
QS "LL-van"  
QS "LL-en"  
QS "LL-in"  
QS "LL-uen"  
QS "LL-vn"  
QS "LL-ang"  
QS "LL-iang"  
QS "LL-uang"  
QS "LL-eng"  
QS "LL-ing"  
QS "LL-ueng"  
QS "LL-ong"  
QS "LL-iong"  
QS "LL-sil"  
QS "LL-sp"  
QS "LL-pau"  
    
    
    
QS "RR-b"  
QS "RR-p"  
QS "RR-m"  
QS "RR-f"  
QS "RR-d"  
QS "RR-t"  
QS "RR-n"  
QS "RR-l"  
QS "RR-g"  
QS "RR-k"  
QS "RR-h"  
QS "RR-j"  
QS "RR-q"  
QS "RR-x"  
QS "RR-zh"  
QS "RR-ch"  
QS "RR-sh"  
QS "RR-r"  
QS "RR-z"  
QS "RR-c"  
QS "RR-s"  
QS "RR-y"  
QS "RR-w"  
QS "RR-a"  
QS "RR-o"  
QS "RR-e"  
QS "RR-ea"  
QS "RR-i"  
QS "RR-u"  
QS "RR-v"  
QS "RR-ic"  
QS "RR-ih"  
QS "RR-er"  
QS "RR-ai"  
QS "RR-ei"  
QS "RR-ao"  
QS "RR-ou"  
QS "RR-ia"  
QS "RR-ie"  
QS "RR-ua"  
QS "RR-uo"  
QS "RR-ve"  
QS "RR-iao"  
QS "RR-iou"  
QS "RR-uai"  
QS "RR-uei"  
QS "RR-an"  
QS "RR-ian"  
QS "RR-uan"  
QS "RR-van"  
QS "RR-en"  
QS "RR-in"  
QS "RR-uen"  
QS "RR-vn"  
QS "RR-ang"  
QS "RR-iang"  
QS "RR-uang"  
QS "RR-eng"  
QS "RR-ing"  
QS "RR-ueng"  
QS "RR-ong"  
QS "RR-iong"  
QS "RR-sil"  
QS "RR-sp"  
QS "RR-pau"  
     
### 重音问题  
重音为1，不重音为0
QS "C-Stressed"  
QS "L-Stressed"  
QS "R-Stressed"     
     
### 声调  
CQS "Toner_C-Syl"
CQS "Toner_L-Syl"
CQS "Toner_R-Syl"
 
### 位置问题  
CQS "Pos_C-Syl_in_C-Word(Fw)"	                     
CQS "Pos_C-Syl_in_C-Word(Bw)"	                     
CQS "Pos_C-Syl_in_C-Prosodic-Word(Fw)"	                   
CQS "Pos_C-Syl_in_C-Prosodic-Word(Bw)"	                   
CQS "Pos_C-Syl_in_C-Prosodic-Phrase(Fw)"	                   
CQS "Pos_C-Syl_in_C-Prosodic-Phrase(Bw)"	                   
CQS "Pos_C-Syl_in_Utterance(Fw)"	                   
CQS "Pos_C-Syl_in_Utterance(Bw)"	                   
    
CQS "Pos_C-Word_in_C-Prosodic-Word(Fw)"	                   
CQS "Pos_C-Word_in_C-Prosodic-Word(Bw)"	                   
CQS "Pos_C-Word_in_C-Prosodic-Phrase(Fw)"	                   
CQS "Pos_C-Word_in_C-Prosodic-Phrase(Bw)"	                   
CQS "Pos_C-Word_in_Utterance(Fw)"	                   
CQS "Pos_C-Word_in_Utterance(Bw)"	                   
    
CQS "Pos_C-Prosodic-Word_in_C-Prosodic-Phrase(Fw)"	                   
CQS "Pos_C-Prosodic-Word_in_C-Prosodic-Phrase(Bw)"	                   
CQS "Pos_C-Prosodic-Word_in_Utterance(Fw)"	                   
CQS "Pos_C-Prosodic-Word_in_Utterance(Bw)"	                   
    
CQS "Pos_C-Prosodic-Phrase_in_Utterance(Fw)"	                   
CQS "Pos_C-Prosodic-Phrase_in_Utterance(Bw)"	                   
    
### 数量问题  
CQS "Num_Syl_in_C-Word"	                     
CQS "Num_Syl_in_L-Word"	                     
CQS "Num_Syl_in_R-Word"	                     
CQS "Num_Syl_in_C-Prosodic-Word"	                     
CQS "Num_Syl_in_L-Prosodic-Word"	                     
CQS "Num_Syl_in_R-Prosodic-Word"	                     
CQS "Num_Syl_in_C-Prosodic-Phrase"	                     
CQS "Num_Syl_in_L-Prosodic-Phrase"	                     
CQS "Num_Syl_in_R-Prosodic-Phrase"	                     
    
CQS "Num_Word_in_C-Prosodic-Word"	                     
CQS "Num_Word_in_L-Prosodic-Word"	                     
CQS "Num_Word_in_R-Prosodic-Word"	                     
CQS "Num_Word_in_C-Prosodic-Phrase"	                     
CQS "Num_Word_in_L-Prosodic-Phrase"	                     
CQS "Num_Word_in_R-Prosodic-Phrase"	                     
    
CQS "Num_Prosodic-Word_in_C-Prosodic-Phrase"	                     
CQS "Num_Prosodic-Word_in_L-Prosodic-Phrase"	                     
CQS "Num_Prosodic-Word_in_R-Prosodic-Phrase"	                     
    
CQS "Num_Syl_in_Utterance"	                     
CQS "Num_Word_in_Utterance"	                     
CQS "Num_Prosodic-Word_in_Utterance"	                     
CQS "Num_Prosodic-Pharse_in_Utterance"	                     
    