文本分析
===============
1 拼音标注风格
--------------------

读此章节时读者有必要回顾拼音的基础知识

* 中华人民共和国教育部发布的 `汉语拼音方案 <http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html>`_
* `整体认读音节 <https://baike.baidu.com/item/%E6%95%B4%E4%BD%93%E8%AE%A4%E8%AF%BB%E9%9F%B3%E8%8A%82/6147451?fr=aladdin>`_

整体认读音节
    16个整体认读音节分别是：zhi 、chi、shi、ri、zi、ci、si、yi、wu、yu、ye、yue、yuan、yin 、yun、ying，但是要注意没有yan，因为yan并不发作an音

声母
    21个声母没有什么争议，如果说有22个声母，一般指多加一个零声母，yw都属于零声母。如果用23个声母，则是21声母+yw两个零声母，如果用27个声母，则是将不同情况下的yw零声母分成6种情况，标注成aa, ee, ii, oo, uu, vv，即21+6=27个声母（具体见hmm训练，合成基元的选择一节）

韵母
    国家汉语拼音方案中韵母数量为35个，但另一说为39个（如百度百科），在原国家汉语拼音方案上增加了-i（前）、-i（后）、er、ê。

下面新加的4个元音做简要解释
    * ê[ε] 在普通话中，ê只在语气词“欸”中单用【因此一些项目忽略了这个单韵母，即38个韵母】。ê不与任何辅音声母相拼，只构成复韵母ie、üe，并在书写时省去上面的附加符号“ˆ”。
    * er[] 是在[ә]的基础上加上卷舌动作而成。 发音例词：而且érqiě 儿歌érgē 耳朵ěrduō 二胡èrhú 二十èrshí 儿童értóng
    * -i(前) 指zi/ci/si中的i 发音例词：私自sīzì 此次cǐcì 次子cìzǐ 字词zìcí 自私zìsī 孜孜zīzī
    * -i(后) 指zhi/chi/shi/ri中的i 发音例词：实施shíshī 支持zhīchí 知识zhīshi 制止zhìzhǐ 值日zhírì 试制shìzhì

拼音标注风格分成两类，

1.第一类是国家规定的方案，也就是日常生活中用到的风格，规定了声母21个，其韵母表中列出35个韵母，具体参见中华人民共和国教育部发布的 `汉语拼音方案 <http://www.moe.edu.cn/s78/A19/yxs_left/moe_810/s230/195802/t19580201_186000.html>`_

2.第二类是方便系统处理的拼音标注风格，不同项目有不同的注音风格，区别主要在于
    * 对y w的处理，有的项目为了方便处理，也将yw视为声母，有的则会将对应的yw传换成实际发音，如ye,yan,yang（整体认读音节）等改成ie,ian,iang，而不适用yw
    * 是否将整体认读音节还原成单个韵母或声母
    * ju qu xu的标注是否转为实际发音标注，即jv qv xv
    * yuan yue yun的标注是否转成yvan yve yvn
    * 注意到iou, uei, uen 前面加声母时，写成iu ui un，例如牛(niu), 归(gui)，论(lun)，标注时是否还原成niou, guei, luen 的问题
    * 儿化音是否简化标注，例如'花儿'，汉语拼音方案中标注为'huar'，一般我们将其转为'hua er'

本项目使用的风格
    * 将yw视作声母，但同时将ya还原成yia, ye还原成yie,其余类似
    * 标注为 jv qv xv
    * 标注为 yvan yve yvn
    * 将iou, uei, uen 标注还原
    * ê标注为ee, er(包括儿化音中的r)标注为er, i(前)标注为ic, i(后)标记为ih
    * 声调标注，轻声标注为5，其他标注为1234

最终使用的声韵母表如下

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


注意：
* pypinyin中使用的是 yuan ju lun
* 本文语料库使用的是 yvan jv lun，语料库中音素标注将yw视作声母

另外一种推荐的方案是使用27个声母，即去掉yw

声母（27个）
    b p m f d t n l g k h j q x zh ch sh r z c s aa ee ii oo uu vv

2 多音字的处理
-----------------------------------------------------
本项目使用了pypinyin

3 文本规范化
-----------------------------------------------------
本项目暂时没有实现此功能

对文本进行预处理，主要是去掉无用字符，全半角字符转化等

有时候普通话文本中会出现简略词、日期、公式、号码等文本信息，这就需要通过文本规范化，对这些文本块进行处理以正确发音[7]。例如
    * “小明体重是 128 斤”中的“128”应该规范为“一百二十八”，而“G128 次列车”中的“128” 应该规范为“一 二 八”；
    * “2016-05-15”、“2016 年 5 月 15 号”、“2016/05/15”可以统一为一致的发音

对于英文而言，如：
    * 2011   NYER   twenty eleven
    * £100   MONEY   one hundred pounds
    * IKEA   ASWD   apply letter-to-sound
    * 100   NUM   one hundred
    * DVD   LSEQ   D. V. D. ꔄ dee vee dee

4 词性标注
-----------------------------------------------------

本项目使用 结巴 工具进行词性标注。结巴分词工具包采用和 ictclas 兼容的标记法。由于结巴分词的标准较为简单，本项目使用结巴的词性标注规范，在上下文标注和问题集中只取大类标注，即字母a-z所代表的词性，具体见下方列表中给出的结巴词性标注表

词性标注规范
    * `结巴使用的词性标注表 <https://github.com/Jackiexiao/MTTS/tree/master/docs/mddocs/jieba.md>`_
    * `中科院ictclas规范 <https://github.com/Jackiexiao/MTTS/tree/master/docs/mddocs/ictclas.md>`_
    * `斯坦福Stanford coreNLP宾州树库的词性标注规范 <https://github.com/Jackiexiao/MTTS/tree/master/docs/mddocs/Stanford_coreNLP.md>`_
    * `ICTPOS3.0词性标记集 <https://gist.github.com/luw2007/6016931>`_ 链接中还包括了ICTCLAS 汉语词性标注集、jieba 字典中出现的词性、simhash 中可以忽略的部分词性
    * 北大标注集

5 句子语气类型
-----------------------------------------------------

[todo]找到能自动标识句子语气类型的工具

============== ====== ====== ====== ======
句子语气的类型 陈述句 疑问句 祈使句 感叹句
============== ====== ====== ====== ======
标识符         d      e      i      q
============== ====== ====== ====== ======

6 中文分词
-----------------------------------------------------

本项目使用了结巴分词器，读者可以按自己的需要选择其他分词器，可见github项目：`中文分词器分词效果评估对比 <https://github.com/ysc/cws_evaluation>`_

