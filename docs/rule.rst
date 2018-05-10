本项目的设计规则
================
1 合成基元
-----------------------------------------
这里选取声韵母作为基元，同时为了模拟发音中的停顿，可以将短时停顿和长时停顿看做是合成基元，此外，将句子开始前和结束时的静音sil也当做合成基元

**合成基元的列表**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
本项目选用的合成基元为

* 声母 | 21个声母+wy（共23个）
* 韵母 | 39个韵母
* 静音 | sil pau sp 

sil(silence) 表示句首和句尾的静音，pau(pause) 表示由逗号，顿号造成的停顿，句中其他的短停顿为sp(short pause)

声母（23个）
    b p m f d t n l g k h j q x zh ch sh r z c s y w 

韵母（39个）
    * 单韵母 a、o、e、 ê、i、u、ü、-i（前）、-i（后）、er
    * 复韵母 ai、ei、ao、ou、ia、ie、ua、uo、 üe、iao 、iou、uai、uei
    * 鼻韵母 an、ian、uan、 üan 、en、in、uen、 ün 、ang、iang、uang、eng、ing、ueng、ong、iong

韵母（39个）（转换标注后）
    * 单韵母 a、o、e、ea、i、u、v、ic、ih、er
    * 复韵母 ai、ei、ao、ou、ia、ie、ua、uo、 ve、iao 、iou、uai、uei
    * 鼻韵母 an、ian、uan、 van 、en、in、uen、 vn 、ang、iang、uang、eng、ing、ueng、ong、iong


**其他项目的方法-引入零声母，这里没有采用**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

6个零声母的引入是为了减少上下文相关的tri-IF数目，这样就可以使得每个音节都是由声母和韵母组成，原先一些只有韵母音节可以被视作是声母和韵母的结构，这样一来，基元就只有 声母-韵母-声母 以及 韵母-声母-韵母 两种结构，而不会出现两个韵母相邻的情况，进而明显减少了上下文相关的基元。

如果这么做的话就是21+6=27个声母，可以将零声母标记成 aa, ee, ii, oo, uu, vv，一是将yw替换，二是将一个韵母组成的音节手动添加上零声母，举例
    * ye,yan,yang（整体认读音节）标注成——ii ie, ii ian, ii iang （ie, ian, iang是真实发音的韵母）
    * ao an ou 熬 安 欧, 标记成 aa ao, aa an, oo ou



2上下文相关标注与问题集
-----------------------------------------

上下文相关标注的规则要综合考虑有哪些上下文对当前音素发音的影响，总的来说，需要考虑发音基元及其前后基元的信息，以及发音基元所在的音节、词、韵律词、韵律短语、语句相关的信息。

本项目的设计规则参考了 `面向汉语统计参数语音合成的标注生成方法 <https://github.com/Jackiexiao/MTTS/tree/master/docs/mddocs/mandarin_example_label.md>`_

具体规则与示例
* `上下文相关标注 <https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/mandarin_label.md>`_
* `问题集设计规则和示例 <https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/question.md>`_
* `完整问题集文件 <https://github.com/Jackiexiao/MTTS/blob/master/docs/misc/23_initial_39_final_3_sil/question.hed>`_

问题集(Question Set)即是决策树中条件判断的设计。问题集通常很大，由几百个判断条件组成。 `一个典型的英文问题集文件(merlin) <https://github.com/CSTR-Edinburgh/merlin/blob/master/misc/questions/questions-radio_dnn_416.hed>`_

问题集的设计依赖于不同语言的语言学知识，而且与上下文标注文件相匹配，改变上下文标注方法也需要相应地改变问题集，对于中文语音合成而言，问题集的设计的规则有:

* 前前个，前个，当前，下个，下下个声韵母分别是某个合成基元吗，合成基元共有65个(23声母+39韵母+3静音)，例如判断是否是元音a QS "LL-a" QS "L-a" QS "C-a" QS "R-a" QS "RR-a"
* 声母特征划分，例如声母可以划分成塞音，擦音，鼻音，唇音等，声母特征划分24个
* 韵母特征划分，例如韵母可以划分成单韵母，复合韵母，分别包含aeiouv的韵母，韵母特征划分8个
* 其他信息划分，词性划分，26个词性; 声调类型，5个; 是否是声母或者韵母或者静音，3个
* 韵律特征划分，如是否是重音，重音和韵律词/短语的位置数量
* 位置和数量特征划分

对于三音素模型而言，对于每个划分的特征，都会产生3个判断条件，该音素是否满足条件，它的左音素（声韵母）和右音素（声韵母）是否满足条件，有时会扩展到左左音素和右右音素的情况，这样就有5个问题。其中，每个问题都是以 QS 命令开头，问题集的答案可以有多个，中间以逗号隔开，答案是一个包含通配符的字符串。当问题表达式为真时，该字符串成功匹配标注文件中的某一行标注。格式如：

QS  问题表达式 {答案 1，答案 2，答案 3，……}

QS "LL==Fricative"    {f^*,s^*,sh^*,x^*,h^*,lh^*,hy^*,hh^*} 

对于3音素上下文相关的基元模型的3个问题，例如：
* 判断当前，前接，后接音素/单元是否为擦音
* QS 'C_Fricative'
* QS 'L_Fricative'
* QS 'R_Fricative'

更多示例：

================== =====================
Question           含义
================== =====================
QS "C_a"           当前单元是否为韵母a
QS "L_Fricative"   前接单元是否为擦音
QS "R_Fricative"   后接单元是否为擦音
QS "C_Fricative"   当前单元是否为擦音
QS "C_Stop"        当前单元是否为塞音
QS "C_Nasal"       当前单元是否为鼻音
QS "C_Labial"      当前单元是否为唇音
QS "C_Apieal"      当前单元是否为顶音
QS "C_TypeA"       含有a的韵母
QS "C_TypeE"       含有e的韵母
QS "C_TypeI"       含有i的韵母
QS "C_POS==a"      当前单元是否为形容词
QS "C_Toner==1"    当前单元音调是否为一声
================== =====================

值得注意的是，merlin中使用的问题集和HTS中有所不同，Merlin中新增加了CQS问题，Merlin处理Questions Set 的模块在merlin/src/frontend/label_normalisation 中的Class HTSLabelNormalisation

Question Set 的格式是
    QS + 一个空格 + "question_name" + 任意空格+ {Answer1, answer2, answer3...} # 无论是QS还是CQS的answer中，前后的**不用加，加了也会被去掉
    CQS + 一个空格 + "question_name" + 任意空格+ {Answer} #对于CQS，这里只能有一个answer 比如 CQS C-Syl-Tone {_(\d+)+} merlin也支持浮点数类型，只需改为CQS C-Syl-Tone {_([\d\.]+)+} 
