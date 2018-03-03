# 论文题目：中文统计参数语音合成系统的实现与改进
本文正在持续更新中，近期更新时间2017.12.28   
作者：Jackiexiao 微信:explorerrr  
[中文语音合成相关思维导图](http://naotu.baidu.com/file/efd4f580e80ed57c7bef115f2d7d5813?token=9b6dd5d2e4bc5b95)  
符号标记  
* todo 需要找时间处理  
* optimize 优化，这是可以优化的点  
* thought 想法，冒出的一些奇怪的想法和idea
* contro  controvesial 争议

# 目录
更详细的目录等我找到好的auto generate table of content 再加上  
* [摘要](#摘要)
* [第一章 绪论](#第一章-绪论)  
* [第二章 统计参数语音合成基础技术综述](#第二章-统计参数语音合成基础技术综述)  
* [第三章 中文语音合成系统的实现](#第三章-中文语音合成系统的实现)  
* [第四章 合成语音质量的评估](第四章-合成语音质量的评估])
* [第五章 个性化语音合成和情感语音合成的研究](#第五章-个性化语音合成和情感语音合成的研究)  
* [第六章 总结和展望](#第六章-总结和展望)  
* [第七章 附录](#第七章-附录)  

# 摘要
随着语音识别技术的成熟，人们逐渐把研究焦点转向了语音合成系统。虽然语音合成已有多年的研究历史，但到目前为止，网络上尚未有基于统计参数语音合成的开源中文语音合成系统，也没有开源的中文语音合成语料库，而英文的语音合成所需的基础语料库和系统早已开源。随着语音合成音质的改善，人们对语音合成系统也提出了更高的要求，如要求个性化（特定人）的语音合成，情感语音合成，与此同时，人们也希望语音合成系统有更高的灵活性和实时性，能够利用有限的语音资源合成优质的语音。统计参数的语音合成系统因其对韵律的灵活控制，不需要很大规模的语料库成为了人们的选择，基于此，本文研究了基于统计参数的语音合成系统，同时综合利用最新的语音合成技术，在英文语音合成系统merlin的基础上搭建了一个开源的、具有灵活性、易于整合和修改的中文语音合成系统，以便今后的研究更好地开展。

本文首先对中文语音合成系统的文本处理前端进行了研究，主要包括了对文本规范化、中文分词、词性标注、拼音标注（包括对多音字的处理）、韵律结构预测的研究，其中我们着重研究了基于神经网络的韵律结构预测方法。之后，为了使系统具有更好的开放性和灵活性，本文研究并设计了上下文属性集、用于决策树聚类的问题集、分别基于音素（声韵母）和音节两种基础合成单元的标注文件。然后基于爱丁堡大学开源的英文语音合成系统merlin，设计并实现了基于HMM的中文统计参数语音合成系统。最后，我们针对当下的热点问题：个性化语音合成和情感语音合成又做了进一步的研究，探讨了如何在统计参数语音合成系统中通过韵律结构预测的改进和声学参数的变换来实现上述两个目标。

正文

# 第一章 绪论
## 1.1 研究背景
### 1.1.1 概述
语音合成技术的应用领域
语音合成技术的历史概况TODO
### 1.1.2 自然语音模拟与合成
### 1.1.2 语音合成技术的分类与研究现状
目前语音合成技术主要分为
* 波形拼接合成
* 统计参数语音合成
* 端到端的语音合成

**波形拼接合成**
波形拼接即是在合成语音时根据一定的规则从语音库中选取合适的语音单元，利用拼接算法将语音单元拼接起来，生成语音。
* 优点:当语音库足够大时，它合成出来的语音自然度相当高。
* 缺点：需要占用大量的存储空间，不适用于嵌入式系统。此外，其发音单一，不利于改变特征。并且当需要改变任何一项语音特征时，就需要重新建立一个新的语音库，成本高昂。
由于其明显的缺点，目前已很少使用波形拼接语音合成系统[2]

**统计参数语音合成**
参数语音合成指的是通过采用数字信号处理的方法，用一个滤波器来模拟人类发音过程，将人类发声过程看做是一个模拟声门状态的源，去激励一个表征声道谐振特性的时变数字滤波器，这个源可能是周期脉冲序列，它代表浊音情况下的声带振动，或者是随机的噪声序列，代表不出声的清音。调整滤波器的参数等效于改变口腔及声道形状，达到控制发出不同声音的目的，而调整激励源脉冲序列的周期或强度，将改变合成语音的音调、重音等。因此，只要正确控制激烈源和滤波器参数（一般每隔10~30ms送一组），这个模型就能灵活地合成出各种语句来，因此称作参数合成的方法。[3]

时变滤波器结构形式有LPC、共振峰、LMA、MLSA，LPC和共振峰合成器整体上不能提供足够自然的语音，但随着LMA的发展，参数合成方法达到了一个新的高峰。[3]

[thought]这样看来，这样的语音合成系统仅仅适用于模拟人类发出的声音而无法发出其他的声音，这很局限也。
* 缺点：合成出的语音容易带有机器味
* 优点：灵活性强，只要经过合理的参数调整，就可以灵活地合成出所需要的语音；只需要较小的语料库

**端到端的语音合成**
TODO  




### 1.1.3 深度学习在语音合成中的应用
最新的研究进展请参见[深度学习于语音合成研究-知乎](https://zhuanlan.zhihu.com/p/30776006)  
## 1.2 论文的研究内容
## 1.3 论文的结构安排
# 第二章 统计参数语音合成基础技术综述
## 2.1 汉语语言分析
TODO 这一部分见书《汉语自然语言处理》，等待补充
### 2.1.1 汉语拼音方案
中华人民共和国教育部发布的[《汉语拼音方案》](http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html)

### 2.1.2 汉语语言特点分析


## 2.2 隐马尔可夫模型
隐马尔可夫模型(Hide Markov Model, HMM)概述：TODO
### 2.2.1 隐马尔可夫模型
### 2.2.2 HSMM半隐马尔可夫模型 
### 2.2.3 HTK工具包
HTK(HMM Tools Kit)是一个由剑桥大学开发的HMM实验工具包。TODO



# 第三章 中文语音合成系统的实现
## 3.1 语料库
### 3.1.1 King_tts_003语料库
语料库使用购买自海天瑞声公司的King_tts_003语料库，该语料库由专业的标准女播音员录制，总时长为15小时，近2万个句子。其中标注包括了拼音、韵律（韵律边界与重音）、音素发音时长、声韵母标注。语音文件以44.1 KHz，16bit，双音道，windows的无压缩PCM格式存储。除了此外，该语料库还提供了记录EGG（electroglottography）信号的音频。

其中标记格式与含义为  
声调的标记格式  
采用数字1、2、3、4、5,代替《汉语拼音方案》中声调阴平（ˉ），阳平（ˊ），上声（ˇ），去声（ˋ），轻声（不标调）这几个标调符号  
   
**韵律的标记格式**
韵律分成四级，分别用#4，#3，#2， #1表示。   
#4  ：
（1）一个完整语意的句子，切除前后可以独立成为一个句子，从听感上调形是完全降下来的，有明显的停顿。   
（2）如果是以二声词结尾的短句，这个二声的词被拖长音，且与后面是转折的关系的，有明显的停顿。   
#3  ：
通常标在一个韵律短语后面，有时会是一个词，从听感上调形是降下来的，但不够完全，不能独立成为一个语意完整的句子。   
#2  ：
（1）表示被‘重读’的词或单个字(为了强调后面)，有停顿，调形上有小的变化, 有‘骤停’的感觉。 （对于单音节词如果是被‘拖长音’，给#1；如果是‘骤停’要给#2  ）
（2）并列关系的词如果被强调重读，给#2；如果是很平滑的，给#1。   
#1  ：
只是韵律词的边界，通常没有停  顿
   

**声韵母与停顿的标记格式**
标注符号采用a，b，d，s四种标记符号进行标注，标注符号的意思如下：
* a表示中文汉字的声母。
* b表示中文汉字的韵母。
* d表示句中的静音长度小于100ms的停顿。
* s表示句子的起始点和结束点以及句中大于100ms的停顿。

**声韵标注的具体规则**
1. 中文汉字拼音的声母用a表示，韵母用b表示。
2. 其中有一些汉字音节以元音开头，称为零声母音节，如a/o/e/ang/eng/en/ai/ei/ao/ou/an/er/，我们用标记点a来进行标注。
3. 其中有一些汉字是特殊读音，仅仅表示鼻子发出的气流，如m/n/ng/，分别对应汉字（呣，嗯，嗯），我们用标记点b来进行标注。
4. 汉字发音为yu/yi/wu/的为整体认读音节，但我们此次把以w，y为声母加韵母的拼音按照声韵进行切分。

举一个例子  
101001 我#1就怕#2自己的#1俗气#3亵渎了#2普者黑的#1风景  
wo3 jiu4 pa4 zi4 ji3 de5 su2 qi4 xie4 du2 le5 pu2 zhe3 hei1 de5 feng1 jing3  

### 3.1.2 语音文本对齐alignment&&音库标记&&音素的时长信息
我们通常需要知道每个音节/音素对应的wav片段以及持续时间是多少，给定一段文本，标注它在音频中的准确位置的任务就叫force-alignment，这里有[forced-alignment-tools](https://github.com/pettarin/forced-alignment-tools)  
从其中可知[aeneas](https://www.readbeyond.it/aeneas/) 是支持中文简体和繁体的alignment的

由此我们可以得到每个句子对应的发音时长标注文件，包括了句子中每个声韵母的发音时长以及每个停顿的发音时长。

**工具** 
Festival-2.1可以用于语音的自动切分和标注

### 3.1.3 语料库的获取
**中文语料库**
目前网络上尚未有免费的语料库，需要自行构建语料库或者是购买。本文使用的语料库King_tts_003购买自海天瑞声公司

**英文语料库**
* 卡内基梅隆大学的免费语料库CMU_ARCTIC


## 3.2 文本分析
文本分析是FrontEnd的一部分，关于英文FrontEnd设计可参考：[front-end Design](http://research.cs.tamu.edu/prism/lectures/sp/l17.pdf),这个pdf大概讲解了frontend的基础架构，frontend的设计需要大量的语言学知识，工作相对也是比较繁琐的。(the front-end provides a symbolic linguistic representation of the text in terms of phonetic transcription and prosody information)
### 3.2.1 拼音标注风格
拼音标注风格分成两类，
1.第一类是国家规定的方案，也就是日常生活中用到的风格，具体参见中华人民共和国教育部发布的[《汉语拼音方案》](http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html)
2.第二类是方便系统处理的拼音标注风格，具体细分有很多种，这里使用的风格为：相比国家方案的其主要变化如下（建议的方法是将所有实际发音为v的改成v，将所有实际只有韵母的改成只有韵母的标记，例如yuan改成van，wan改成uan）
    * y w 如何处理，为了处理方便，是否将其当做声母，还是直接去除，注意到语料库中将y w 当做声母处理，在发音时长中也是如此标记，我觉得这样不好，因为yw本身并不发音，应该将整体认读音节单独处理而非划分成yw [optimize]
    * 是否将ju qu xu 的标注改成 jv qv xu，注意到我们使用的语料库使用的是jvxv
    * 注意到我们使用的语料库标注“援”这个音的时候使用的是yvan而不是yuan，而pypinyin中使用的是yuan
    * 是否将i行韵母中出现的ye,yan,yang等改成ie,ian,iang，毕竟并不存在声母yw，同理于其他的uv行，注意到语料库使用的ye,yan,yang
    * 关于儿化音的处理？

### 3.2.2 多音字的处理
多音字是汉语中的普遍现象，正确地处理多音字才能保证汉语tts系统输出的正确性。

目前字音转换的方式有两种，一种是基于规则的字音转换，一种是基于统计的字音转换。基于规则的方法由于过于依赖语言学知识，存在很大的局限性。目前主流的方法是使用基于统计的字音转换。

### 3.2.3 文本规范化

### 3.2.4 词性标注

### 3.2.5 中文分词

### 3.2.6 情感分析

### 3.2.7 自然语言处理概述

### 3.2.8 经过文本分析后输出的xml格式文档



## 3.3 文本分析工具包
常用的开源自然语言处理/开发包可见[知乎-鉴津Jackie的回答](https://www.zhihu.com/question/19929473/answer/264555333)

文本分析

下面将介绍几个笔者使用的自然语言处理工具包
### 3.3.1 结巴分词
结巴分词很容易安装和使用，可见[结巴分词-github主页](https://github.com/fxsjy/jieba)，这里就不赘述了。
值得注意的是
### 3.3.2 HanLp
### 3.3.3 NLTK
### 3.3.4 python-pinyin
[python-pinyin](https://github.com/mozillazg/python-pinyin)
提供了汉字转换成拼音的工具，它的安装和使用都很方便`pip3 install
pypinyin`，使用可见[官方文档](https://pypinyin.readthedocs.io/zh_CN/master/)  

关于拼音标注的风格，这里使用了pypinyin.Style.TONE3，举个例子`yuan2 jiu4`，再稍加转换就称为本系统中使用的风格

注意：
* pypinyin不提供对数字符号[0-9]进行拼音标记，使用时需要自定义词典，注意覆盖3.4中间有个“点”的声音



## 3.4 韵律处理
语音信号有四个特征参数：
* 音高
* 音长
* 音强
* 音色

其中音色取决于不同人的发音特征，一般汉语韵律规则的主要表现体现在——音节的时长分布、音高的变化、音强的变化以及适当的停顿。[2]
### 3.4.5 重音
**重音的重要性体现在**  
1. 对听感的影响：有了重音人们的语句听起来才有抑扬顿挫的感觉，
2. 对语义的影响：当一个句子的重音落在不同地方时，表达的语义是不同的

**对重音的刻画方式** 
不同语言的重音特点是不同的，例如英语的重音认为是音长、音高、音强的集合，其中音高因素占主导地位，强调语气就是通过扩大调域来形成。对于汉语来说，它的重音主要体现在音长的增长，其次才是调域的扩大以及音高的提升和调性，与发音强度的关系并不是很密切。[2]

### 3.4.6 韵律的标注
参加语料库一节中韵律的标注。


## 3.5 语音学处理

[2]文使用的声学参数为：24阶梅尔倒谱参数，一阶能量以及一阶基频参数，共78维参数；
### 3.5.1 声学建模参数的选取
**mfcc vs mcep vs lsp**
The vocoder extracts the parameters: spectral envelope, f0 contour, and aperiodicities. Then, you can transform them into MGCs (or MCEP), lf0, and bap, respectively.  
Do not confuse MGCs (or MCEP) with MFCCs, they are different features. The forced-alignment process uses MFCCs to recognize the phoneme structures of the data.  
论文”基于HMM的可训练中文语音合成“中提到：用于语音合成的参数 lsp 优于mcep，而mcep 优于mfcc  
可以参考这篇论文：[A Comparative Performance of Various Speech Analysis-Synthesis Techniques ](https://pdfs.semanticscholar.org/7301/b31571786b661b652b2ecbbcec570e00a18d.pdf)


### 3.5.2 使用HTK提取MFCC谱参数和基频F0
可见文献[4]

## 3.6 HMM训练
### 3.6.1 合成基元以及其状态数量的选择
**如何选取合成基元**
[3]对于汉语语音系统而言，常用的基本基元有音节、声韵母和音素。由于汉语有418个无调音节，如考虑语调则有1300多个音节，在进行上下文无关的建模时，选用音节作为基元可以取得比较好的性能。[todo 可以试一下使用音节来作为合成单元，看看合成效果]但如果考虑上下文相关的变化，则会由于基元数目太多而导致模型无法实现。而声韵母（声母21个，韵母todo个）与音素的数目都相对较少，因此可以用来作上下文相关模型的基元。

汉语大概有35个音素，但是音素并没有反映出汉语语音的特点，而且，相对于声韵母，音素显得十分不稳定，这就给标注带来了困难，进而影响声学建模，因此，音素也不适合作为上下文相关的合成基元。[3]

[todo]有没有用音节来做基元的，音素指的是？ming分成 m i n g四个音素？

这里选择音节和声韵母两种，为了模拟发音中的停顿，可以将短时停顿和长时停顿看做是合成基元，此外，将句子开始前和结束时的静音sil也当做合成基元

**合成基元的列表**
声母 | 21个声母+wy+零声母(_A _E _I _O _U _V)
韵母 | 39个韵母
静音 | sil pau sp 

[contro] sil(silence) 表示句首和句尾的静音，pau(pause) 表示由逗号，顿号造成的停顿，句中其他的短停顿为sp(short pause)

[contro] 6个零声母（）的引入是为了减少上下文相关的tri-IF数目，这样就可以使得每个音节都是由声母和韵母组成，原先一些只有韵母音节可以被视作是声母和韵母的结构，这样一来，基元就只有 声母-韵母-声母 以及 韵母-声母-韵母 两种结构，而不会出现两个韵母相邻的情况，进而明显减少了上下文相关的基元。[3]

**基元状态数量的选择**
一般我们选择将一个基元分成5个状态。假设每个状态都由一个高斯分布描述，那么总共的高斯分布数量等于上下文相关基元的数目*5，这样数量过多，在训练数据库不是足够大的情况下，很多基元会存在训练不充分的问题。解决的方法是采用参数共享的技术。例如进行状态共享（state Tying）建模，或者混合密度共享（Tied Mixture）建模

**上下文基元是否带声调**
语音识别中，大多数系统使用的基元时不带有声调的。但在语音合成系统中，我们有两种选择：一是训练中仍采用无声调基元，然后在合成的最后阶段，根据汉语声调的模式调整基音周期，达到合成语调的目的。另一方法是，在训练中即使用带有声调的基元，然后在上下文相关训练时将它们进行状态共享，以降低模型规模，并提供近似合成未知基元的能力。[3]

[todo][contro]直觉上后者合成出来的语音可能更自然，本文选择后者（需要再进行测试评估）


### 3.6.2上下文相关的标注
**设计上下文相关标注的规则**
即要综合考虑有哪些上下文对当前音素发音的影响，总的来说，，需要考虑发音基元及其前后基元的信息，以及发音基元所在的音节、词、韵律词、韵律短语、语句相关的信息。[1]但是具体到哪些上下文是更有必要的就需要再仔细研究研究了[optimize]
**本文的上下文设计原则**
对于以声韵母为合成基元来说，直观上使用使用相邻五音素的上下文相关信息要比3音素的要好。
**具体的上下文设计**
本文将提供多种上下文设计以及对应的问题集，并探讨不同上下文设计对语音合成效果的影响[todo]

[3]也提供了一种上下文设计的思路


### 3.6.3 基于决策树的聚类
[tmp]下面主要参考了[2]中的问题集设计

由于采用了大量的三音素结构，HMM模型数量骤增，过多的模型数量使得难以有足够的数据进行训练。决策树通过将模型进行归类很好地解决了这个问题。此外，实际语音合成时可能遇到训练数据中没有出现的基元，基于决策树（Decision Tree）的方法，可以使用那些可见基元的分布来合成在训练数据中不可见的基元。

决策树介绍TODO(可以抄写[2]中的介绍)

决策树的学习资料可以参见[todo]

### 3.6.4 问题集的设计
主要依据参考文献[3]


问题集(Question Set)即是决策树中条件判断的设计。问题集通常很大，由几百个判断条件组成，一个典型的问题集文件的部分内容如下:
TODO(Question Set 例子，可以找merlin的)

问题集的设计依赖于不同语言的语言学知识，对于中文语音合成而言，问题集的设计主要参考了以下的语言学知识：
* 声母特征划分，例如声母可以划分成塞音，擦音，鼻音，唇音等，具体参见[TODO]
* 韵母特征划分，例如韵母可以划分成单韵母，复合韵母，分别包含aeiouv的韵母，具体参见[TODO]

对于三音素模型而言，对于每个划分的特征，都会产生3个判断条件，该音素是否满足条件，它的左音素和右音素是否满足条件。例如
* 判断当前，前接，后接音素/单元是否为擦音
* QS 'C_Fricative'
* QS 'L_Fricative'
* QS 'R_Fricative'
 

参考微软论文:HMM-based Mandarin Singing Voice Synthesis Using Tailored Synthesis Units and Question Sets

**Question Set for Decision Trees**
Based on unit definition and contextual factors, we define five categories for the questions in the question set. The five categories of the question set are sub-syllable, syllable, phrase, song, and note. The details of the question set are described as follows.
1. Sub-syllable: (current sub-syllable, preceding one and two sub-syllables, and succeeding one and two sub-syllables) Initial/final, final with medial, long model, articulation category of the initial, and pronunciation category of the final
2. Syllable: The number of sub-syllables in a syllable and the position of the syllable in the note
3. Phrase: The number of sub-syllables/syllables in a phrase
4. Song: Average number of sub-syllables/syllables in each measure of the song and the number of phrases in this song
5. Note: The absolute/relative pitch of the note; the key, beat, and tempo of the note; the length of the note by syllable/0.1 second/thirty-second note; the position of the current note in the current measure by syllable/0.1 second/ thirty-second note; and the position of the current note in the current phrase syllable/0.1 second/thirty-second note 

### 3.6.5 决策树的构建
### 3.6.6 HMM拓扑结构以及声学参数结构

**基元状态的拓扑结构**
本文选择了从左至右无跳转的HMM拓扑结构，其他结构详见[3]3.1.2节  

            |v|  |v|  |v|  |v|  |v|  
(begin) 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (end)  

|v|表示可以跳转到自身的状态，1和7分别是起始和结束状态。

**声学参数的结构**
TODO，可参考[3]

### 3.6.6 状态时长模型
### 3.6.7 基音周期模型


## 3.7 Merlin
### 3.7.1 Merlin的安装与运行demo
**安装**
Merlin只能在unix类系统下运行，使用Python，并用theano作为后端
Merlin的Python语言采用的是Python2.7编写，所以我们需要在Python2.7的环境下运行Merlin，为避免python不同版本之间的冲突，我们采用Anaconda对Python运行环境进行管理。  
使用Anaconda创建Merlin运行环境具体操作如下：  
打开终端，使用下面命令查看一下现有python环境  
`conda env list`  
使用下面命令创建一个名为merlin的python环境  
`conda create --name merlin python=2.7`
先进入merlin环境中  
`source activate merlin`
在这个环境下安装merlin  
```
sudo apt-get install csh
pip install numpy scipy matplotlib lxml theano bandmat
git clone https://github.com/CSTR-Edinburgh/merlin.git
cd merlin/tools
./compile_tools.sh
```
如果一切顺利，此时你已经成功地安装了Merlin，但要注意的是Merlin不是一个完整的TTS系统。它提供了核心的声学建模功能：语言特征矢量化，声学和语言特征归一化，神经网络声学模型训练和生成。但语音合成的前端（文本处理器）以及声码器需要另外配置安装。此外，Merlin目前仅提供了英文的语音合成。  
此外，上述安装默认只配置支持CPU的theano，如果想要用GPU加速神经网络的训练，还需要进行其他的步骤。由于语料库的训练时间尚在笔者的接受范围之内（intel-i5，训练slt_arctic_full data需要大概6个小时），因此这里并没有使用GPU进行加速训练。  

**运行Merlin demo**
`.～/merlin/egs/slt_arctic/s1/run_demo.sh`
该脚本会使用50个音频样本进行声学模型和durarion模型的训练，并合成5个示例音频。在此略去详细的操作步骤，具体可参见：Getting started with the Merlin Speech Synthesis Toolkit [installing-Merlin](https://jrmeyer.github.io/merlin/2017/02/14/Installing-Merlin.html)  

### 3.7.2 Merlin源码理解

#### 0 文件含义

Folder        |    Contains
------------- | -------------------
recordings    |     speech recordings, copied from the studio
wav           |     individual wav files for each utterance
pm            |     pitch marks
mfcc          |     MFCCs for use in automatic alignment[mfcc tutorial](http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)
lab           |     label files from automatic alignment
utt           |     Festival utterance structures
f0            |     Pitch contours
coef          |     MFCCs + f0, for the join cost
coef2         |     coef2, but stripped of unnecessary frames to save space, for the join cost
lpc           |     LPCs and residuals, for waveform generation
bap           |     band aperiodicity

免费的语料库

Merlin使用了网络上免费的语料库slt_arctic，可以在以下网址进行下载：[slt_arctic_full_data.zip](http://104.131.174.95/slt_arctic_full_data.zip)

#### 2 训练数据的处理

Merlin自带的demo（merlin/egs/slt_arctic/s1 ）已经事先完成了label文件的提取，所以这里不需要前端FrontEnd对数据进行处理。  
Merlin通过脚本文件setup.sh在～/merlin/egs/slt_arctic/s1 目录下创建目录experiments，在experiments目录下创建目录slt_arctic_demo，完成数据的下载与解压，并将解压后的数据分别放到slt_arctic_demo/acoustic_mode/data，slt_arctic_demo/duration_model/data目录下，分别用于声学模型和持续时间模型的训练。

#### 3 Demo语料库的训练

run_demo.sh文件会进行语音的训练以及合成。这里有许多的工程实现细节，在这里略去说明，其主要进行了如下步骤
![img](/img/image5.png)
其中语料库包含了文本和音频文件，文本需要首先通过前端FrontEnd处理成神经网络可接受的数据，这一步比较繁琐，不同语言也各不相同，下面会着重讲解。音频文件则通过声码器（这里使用的是STRAIGHT声码器）转换成声码器参数（包括了mfcc梅谱倒谱系数，f0基频，bap：band aperiodicity等）再参与到神经网络的训练之中。

#### 4 Demo语料库的合成

Demo中提供了简单的合成方法，使用demo（merlin/egs/slt_arctic/s1 ）下的脚本文件：merlin_synthesis.sh即可进行特定文本的语音合成。  
同样的，由于merlin没有自带frontend，所以其demo中直接使用了事先经过frontend转换的label文件作为输入数据来合成语音。如果想要直接输入txt文本来获得语音，需要安装FrontEnd（下文会提及）并根据merlin_synthesis.sh文件的提示用FrontEnd来转换txt文本成label文件，再进行语音合成。  
对于英文语音合成，merlin中需要首先通过Duration模型确定音素的发音时间，然后根据声学模型合成完整的语音。  

#### 5.Merlin的训练网络

Merlin的训练网络可见[*Merlin: An Open Source Neural Network Speech Synthesis System *](http://ssw9.net/papers/ssw9_PS2-13_Wu.pdf)  
Merlin一共提供了4类神经网络用于HMM模型的训练，分别是  
- 前馈神经网络
- 基于LSTM的RNN网络
- 双向RNN网络
- 其他变体（如blstm）

### 3.7.3 Merlin 前端

Merlin前端FrontEnd 

（1）Label的分类

在Merlin中，Label有两种类别，分别是  
- **state align**（使用HTK来生成，以发音状态为单位的label文件，一个音素由几个发音状态组成）
- **phoneme align**（使用Festvox来生成，以音素为单位的label文件）

（2）txt to utt

文本到文本规范标注文件是非常重要的一步，这涉及自然语言处理，对于英文来说，具体工程实现可使用Festival，参见：[Creating .utt Files for English](http://www.cs.columbia.edu/~ecooper/tts/utt_eng.html)  
Festival 使用了英文词典，语言规范等文件，用最新的EHMM alignment工具将txt转换成包含了文本特征（如上下文，韵律等信息）的utt文件

（3）utt to label    

在获得utt的基础上，需要对每个音素的上下文信息，韵律信息进行更为细致的整理，对于英文的工程实现可参见：[Creating Label Files for Training Data](http://www.cs.columbia.edu/~ecooper/tts/labels.html)  

label文件的格式请参见：[lab_format.pdf](http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf)

（4）label to training-data（HMM模型聚类）TODO

由于基于上下文信息的HMM模型过于庞大，有必要对HMM模型进行聚类，即使用问题集Question file.（可以参考[决策树聚类](http://blog.csdn.net/quhediegooo/article/details/61202901)）（这个Question sets目测可以看HTS的文档来获得进一步的解释）

Question file 的解释：  
The questions in the question file will be used to convert the full-context labels into binary and/or numerical features for vectorization. It is suggested to do a manual selection of the questions, as the number of questions will affect the dimensionality of the vectorized input features.  

在Merlin目录下，merlin/misc/questions目录下，有两个不同的文件，分别是：  
questions-radio_dnn_416.hed        questions-unilex_dnn_600.hed  
查看这两个文件，我们不难发现，questions-radio_dnn_416.hed定义了一个416维度的向量，向量各个维度上的值由label文件来确定，也即是说，从label文件上提取必要的信息，我们可以很轻易的按照定义确定Merlin训练数据training-data；同理questions-unilex_dnn_600.hed确定了一个600维度的向量，各个维度上的值依旧是由label文件加以确定。

### 3.7.4 Merlin vocoder声码器

Merlin中自带的vocoder工具有以下三类：Straight，World，World_v2  
这三类工具可以在Merlin的文件目录下找到，具体的路径如下merlin/misc/scripts/vocoder  
在介绍三类vocoder之前，首先说明几个概念：  

**MGC特征**：通过语音提取的MFCC特征由于维度太高，并不适合直接放到网络上进行训练，所以就出现了MGC特征，将提取到的MFCC特征降维（在这三个声码器中MFCC都被统一将低到60维），以这60维度的数据进行训练就形成了我们所说的MGC特征  
**BAP特征**： Band Aperiodicity的缩写  
LF0：LF0是语音的基频特征  

Straight  

音频文件通过Straight声码器产生的是：60维的MGC特征，25维的BAP特征，以及1维的LF0特征。  
通过 STRAIGHT 合成器提取的谱参数具有独特 特征(维数较高), 所以它不能直接用于 HTS 系统中, 需要使用 SPTK 工具将其特征参数降维, 转换为 HTS 训练中可用的 mgc(Mel-generalized cepstral)参数, 即, 就是由 STRAIGHT 频谱计算得到 mgc 频谱参数, 最后 利用原 STRAIGHT 合成器进行语音合成  

World  

音频文件通过World声码器产生的是：60维的MGC特征，可变维度的BAP特征以及1维的LF0特征，对于16kHz采样的音频信号，BAP的维度为1，对于48kHz采样的音频信号，BAP的维度为5  
网址为：[github.com/mmorise/World](https://github.com/mmorise/World)  

### 3.7.5 生成Merlin的英文label用于语音合成

具体步骤如下参见：[Create_your_own_label_Using_Festival.md](./Create_your_own_label_Using_Festival.md)


## 3.8 声码器Vocoder
这个在merlin源码学习中也讲到了。这里可以讲讲声码器的原理。TODO

## 3.9 语音合成模块
### 3.9.1 语音合成所需要的文件
* 经过文本分析得到的正确的汉语拼音序列
* 上下文标注文件
* 经过训练后得到的决策树文件
* 梅尔倒谱参数、基频参数、时长的模型文件


语音合成的主要步骤有
1. 通过文本分析得到xml标注文件
2. 将xml标注文件转换为上下文相关基元的序列
3. 根据这个序列搜索得到相应的状态时长，基音周期和频谱的HMM模型
4. 由状态时长HMM模型得到基元个状态的持续时长
5. 根据状态的时长、基音周期HMM和频谱HMM构建句子的HMM模型，这样每句文本信息都能够转化为一串无跳转从左至右的HMM模型，进行参数合成，得到每帧的基音周期、对数能量和、对数能量和MFCC参数
6. 将第5步得到的参数传入基于MSLA滤波器的合成器（声码器）进行语音合成


### 3.8.1 训练模型——Duration和声学模型

语音合成和语音识别是一个相反的过程, 在语音 识别中, 给定的是一个 HMM 模型和观测序列(也就是 特征参数, 是从输入语音中提取得到), 要计算的是这 些观测序列对应的最有可能的音节序列, 然后根据语 法信息得到识别的文本. 而在合成系统中, 给定的是 HMM 模型和音节序列(经过文本分析得到的结果), 要 计算的是这些音节序列对应的观测序列, 也就是特征 参数.  

HTS的训练部分的作用就是由最初的原始语料库经过处理和模型训练后得到这些训练语料的HMM模型[5]。建模方式的选择首先是状态数的选择,因为语音的时序特性,一个模型的状态数量将影响每个状态持续的长短,一般根据基元确定。音素或半音节的基元,一般采用5状态的HMM;音节的基元一般采用10个状态。在实际的建模中,为了模型的简化,可以将HMM中的转移矩阵用一个时长模型(dur)替代,构成半隐马尔可夫模型HSMM hidden semi-Markov Model。用多空间概率分布对清浊音段进行联合建模,可以取得很好的效果。HTS的合成部分相当于训练部分的逆过程,作用在于由已经训练完成的HMM在输入文本的指导下生成参数,最终生成语音波形。具体的流程是:

 - 通过一定的语法规则、语言学的规律得到合成所需的上下文信息,标注在合成label中。
 - 待合成的label经过训练部分得到的决策树决策,得到语境最相近的叶结点HMM就是模型的决策。
 - 由决策出来的模型解算出合成的基频、频谱参数。根据时长的模型得到各个状态的帧数,由基频、频谱模型的均值和方差算出在相应状态的持续时长帧数内的各维参数数值,结合动态特征,最终解算出合成参数。
 - 由解算出的参数构建源-滤波器模型,合成语音。源的选取如上文所述:对于有基频段,用基频对应的单一频率脉冲序列作为激励;对于无基频段,用高斯白噪声作为激励

HSMM半隐马尔可夫模型的解释如下

A hidden semi-Markov model (HSMM) is a statistical model with the same structure as a [hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model) except that the unobservable process is [semi-Markov](https://en.wikipedia.org/wiki/Semi-Markov_process) rather than [Markov](https://en.wikipedia.org/wiki/Markov_process). This means that the probability of there being a change in the hidden state depends on the amount of time that has elapsed since entry into the current state. This is in contrast to hidden Markov models where there is a constant probability of changing state given survival in the state up to that time

# 第四章 合成语音质量的评估
对合成语音质量评估一般分为
* 可懂度测试[2]
* 自然度测试[2] 可以使用主观评测的方法MOS(Mean Opinion Score)
* 流畅度测试

具体测试可参考[3][todo 目前暂时跳过这部分内容]

# 第五章 个性化语音合成和情感语音合成的研究
## 5.1 个性化语音合成文献综述
## 5.2 个性化语音合成研究
## 5.3 情感语音合成文献综述
## 5.4 情感语音合成文献综述
### 5.4.1 面向情感语音合成的上下文相关的标注格式
# 第六章 总结和展望
# 第七章 附录
## 7.1 语音合成相关软件
### 7.1.1 Praat
Praat语音学软件
http://www.fon.hum.uva.nl/praat/
### 7.1.2 HTK
### 7.1.3 HTS
### 7.1.4 Merlin
### 7.1.5 开源的自然语言处理项目及其比较
https://www.zhihu.com/question/19929473
目前常用的自然语言处理开源项目/开发包有哪些
## 7.2 语音合成的有趣应用
合成歌声 见https://www.zhihu.com/question/26165668)
参考文献
## 7.3 有用的工具
这里有与中文语言处理相关的Python package
https://pypi.python.org/pypi?:action=browse&show=all&c=98&c=489

## 7.4 术语表
 - Front end 前端  
 - vocoder 声音合成机（声码器）  
 - MFCC 
 - 受限波尔曼兹机  
 - bap [band aperiodicity](http://blog.csdn.net/xmdxcsj/article/details/72420051)  
 - ASR：Automatic Speech Recognition自动语音识别  
 - AM：声学模型  
 - LM：语言模型  
 - HMM：Hiden Markov Model 输出序列用于描述语音的特征向量，状态序列表示相应的文字  
 - HTS：HMM-based Speech Synthesis System语音合成工具包  
 - HTK：Hidden Markov Model Toolkit 语音识别的工具包  
 - 自编码器  
 - SPTK：speech signal precessing toolkit  
 - SPSS : 统计参数语音合成statistical parametric speech synthesis  
 - pitch 音高：表示声音(基本)频率的高低
 - Timbre 音色
 - Zero Crossing Rate 过零率
 - Volume 音量
 - sil silence
 - syllable 音节
 - intonation 声调，语调，抑扬顿挫
 - POS part of speech
 - mgc 
 - mcep Mel-Generalized Cepstral Reprfesentation
 - mcc mel cepstral coefficents
 - mfcc Mel Frequency Cepstral Coefficents
 - LSP: Line Spectral Pair线谱对参数
 - monophone 单音素
 - biphone diphone 两音素
 - triphone 三音素
 - quadphone 四音素
 - 这里有[命名规则](http://wiki.c2.com/?NumericalPrefixes)
 - utterance 语音，发声
 - 英语韵律符号系统ToBI(Tone and Break Index)
 - CD-DNN-HMM（Context-Dependent DNN-HMM）
 - frontend :The part of a TTS system that transforms plain text into a linguistic representation is called a frontend
 - .wpa  word to phonetic alphabet
 - .cmp Composed acoustic features 
 - .scp system control program
 - .mlf master label file
 - .pam phonetic alphabets to model
 - .mgc mel generalized cepstral feature
 - .lf0 log f0 a representation of pitch（音高） 音高用基频表示
 - .mgc
 - .utt .utt files are the linguistic representation of the text that Festival outputs（full context training labels)
 - .cfg




# 参考文献
[1] 面向汉语统计参数语音合成的标注生成方法 
[2] 基于HMM的可训练的汉语语音合成系统
[3] 基于HMM的中文语音合成研究
[4]
[5]
[6]
[7]
[8]
[9]
[10]
[11]
[12]
[13]
[14]




1 参考文献
范会敏, 何鑫. 中文语音合成系统的设计与实现[J]. 计算机系统应用, 2017(2):73-77.  
郝东亮, 杨鸿武, 张策,等. 面向汉语统计参数语音合成的标注生成方法[J]. 计算机工程与应用, 2016, 52(19):146-153.  
Merlin: An Open Source Neural Network Speech Synthesis System   
[英文](http://ssw9.net/papers/ssw9_PS2-13_Wu.pdf)
[中文](http://blog.csdn.net/lujian1989/article/details/56008786)

2 工程实现教程部分

 - [Getting started with the Merlin Speech Synthesis Toolkit](http://jrmeyer.github.io/merlin/2017/02/14/Installing-Merlin.html)  
 - [Merlin官方教程（正在建设中）](http://104.131.174.95/Merlin/dnn_tts/doc/build/html/)  
 - [**Columbia University TTS manual**](http://www.cs.columbia.edu/~ecooper/tts/)  
 - [HTS tutorial](http://hts.sp.nitech.ac.jp/?Tutorial)  
 - [Festvox教程（利用wav 和标记数据创造label）](http://festvox.org/bsv/)  
 - [speech.zone build-your-own-dnn-voice](http://www.speech.zone/exercises/build-your-own-dnn-voice/)   

3 相关软件

 - [Merlin语音合成系统 Github](https://github.com/CSTR-Edinburgh/merlin)
 - [Festvox](https://festvox.org)
 - [HTK](http://htk.eng.cam.ac.uk/) 
 - HTS
 - SPTK
 - World
 - Praat语音学软件

4 语音识别/合成基础知识

 - [机器学习&数据挖掘笔记_13（用htk完成简单的孤立词识别）](http://www.cnblogs.com/tornadomeet/p/3274078.htmli) 了解语音识别的基础
 - [上下文相关的GMM-HMM声学模型](http://www.cnblogs.com/cherrychenlee/p/6780460.html)
 - A beginners’ guide to statistical parametric speech synthesis[英文](http://www.cstr.ed.ac.uk/downloads/publications/2010/king_hmm_tutorial.pdf)[中文](https://shartoo.github.io/texttospeech/)
 - [语音产生原理与特征参数提取](http://blog.csdn.net/u010451580/article/details/51178190)
 - [浅谈语音识别基础](http://www.jianshu.com/p/a0e01b682e8a)
 - [English tutorial for Chinese Spoken Language Processing](http://iscslp2016.org/slides.html)
 - [中文语音合成基本概念](http://staff.ustc.edu.cn/~zhling/Course_SSP/slides/Chapter_13.pdf)
 - [cmu_speech_slide](http://www.speech.cs.cmu.edu/15-492/slides/)
