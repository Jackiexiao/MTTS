语音识别新手指南
======================================================


本教程适用范围
------------------------------------------------------
面向有计算机专业基础的读者，至少熟悉Linux，掌握shell脚本语言，掌握python，目的是学习语音识别基础知识和理论，并且追踪能够使用Kaldi工具包来完成自己的项目、实验

步骤
------------------------------------------------------
1 对语音识别有粗略的认知
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
推荐：

知乎语音识别的技术原理
https://www.zhihu.com/question/20398418

语音识别技术的前世今生_王赟的知乎live的ppt
https://zhihu-live.zhimg.com/0af15bfda98f5885ffb509acd470b0fa
可以自己手动搭一个孤立词识别，孤立词语音识别跟MNIST手写字识别几乎一模一样，直接输入声音波形，输出声波所对应的孤立词类别。可以参考下面的项目
https://github.com/microic/niy/tree/master/examples/speech_commands

另一个就是使用谷歌的Tensorflow官方语音识别入门教程
这个入门教程将教会你训练一个简单的语音识别网络，能识别10个词，就像是语音识别领域的MNIST（手写数字识别数据集）。同时这个教程也附上了相应的语音指令数据集

见网址http://www.sohu.com/a/167174796_610300

2 跑一遍kaldi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
（1）安装Kaldi
看官方主页的Readme就可以了

（2）跑一个例子
先跑kaldi/egs/yesno 简单识别两个单词，接下来是tidigits，再接下来是hkust中文识别
可参考博客 http://blog.csdn.net/snowdroptulip/article/details/78914687

hkust项目（中文电话数据集），可参考博客
http://blog.csdn.net/AMDS123/article/details/70313787

可以从跑thchs30开始，教程https://www.jianshu.com/p/22fc9906878f
理解thchs30/s5/run.sh的主要步骤http://blog.csdn.net/BBZZ2/article/details/72884979

（3）初步阅读Kaidi的官方文档


3 学习hmm-gmm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
途径：学习htkbook，《语音识别实践》

学习kaldi的话，先从hmm-gmm入手比较好，像steps/train_delta.sh, steps/train_fmllr.sh, steps/decode.sh这些脚本都是基于hmm-gmm模型。kaldi官网上没有多少关于hmm-gmm的资料，没有hmm-gmm基础知识的初学者可能对于decision tree，alignment, lattice这些概念一头雾水。若要搞清楚这些概念，可以看语音识别另一开原工具htk的文档htk book，htk book是学习hmm-gmm很好的一部著作，将hmm-gmm从训练到解码的过程讲解的很透彻。只要知道决策树，训练/识别网络扩展，viterbi解码，EM算法，区分训练这几个概念的原理hmm-gmm也就理解透彻了。htk book对于这些都有讲解，部分内容如EM算法，区分训练需要看一些文献。htk book第二，八，十，十二，十三章需要重点看；在学习htkbook的过程中，可以结合着kaldi的脚本对照理解；比如steps/train_delta.sh中build-tree命令那部分的代码对应htk book第十章tree-based clustering, gmm-est命令那部分的代码对应htk book第八章的Parameter Re-Estimation Formulae;

4 学习神经网络
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

搞清楚hmm-gmm之后对语音识别就有了一个清晰的理解，接下来就可以上手神经网络。kaldi支持很多神经网路，如MLP, RNN, CNN, LSTM，如果对神经网路了解不多还是从MLP入手较好，MLP是神经网路中最基础的模型。
神经网路kaldi有3个工具nnet1, nnet2, nnet3，初学者可以从nnet1开始。nnet1使用的是hmm-dnn架构，相关的知识可以查阅微软俞栋2009-2013期间发表的论文。
nnet2的架构和nnet1同样是hmm-dnn架构，但是使用的是dan povey团队设计的NSGD算法，支持多线程并行训练，学习nnet2可以追dan povey从2012年之后的论文
至于nnet3，chain model,以及其他的神经网路结构(rn,cnn,lstm)的学习，

5 看论文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
当完成我上面的说的学习内容后自然对语音识别有一个大体的认识，后面要做的就是看相关的文献。微软，dan povey，google, 多伦多大学来自这些地方的论文不断的追就行了。
最后总结，语音识别是对理论要求很高的方向，学习过程中一定要注重理论知识的学习，很多公式还是有必要自己去推导下才能有深刻的理解。

资料推荐
------------------------------------------------------
论文
多关注ICASSP，InterSpeech的论文集

文字资料
------------------------------------------------------
Kaldi的官方文档
网友总结的《kaldi的全部资料_v0.4.pdf》
以及《Chinese_doc_of_kaldi》

王赟的知乎live pdf
https://zhihu-live.zhimg.com/0af15bfda98f5885ffb509acd470b0fa

HMM-GMM部分
<htk book>: HTK Speech Recognition Toolkit
http://lasa.epfl.ch/teaching/lectures/ML_Phd/Notes/GP-GMM.pdf
此文献详细讲解了hmm-gmm训练算法的推导过程
http://www.cc.gatech.edu/~dellaert/em-paper.pdf
此文献详细讲解了EM算法的基本原理
Discriminative Training for Large Vocabulary Speech Recognition (PDF Download Available)
此文献详细讲解了区分训练的基本原理
神经网络部分:
Dan Povey
kaldi作者Dan Povey的个人主页，学习nnet2, nnet3, chain model看Povey的论文会很有帮助；

书籍
------------------------------------------------------
htkbook 《语音信号处理》《语音识别实践》《统计学习方法》《机器学习》《模式识别》

《语音识别实践》：微软研究院俞栋对HMM-DNN架构在语音识别中的相关理论讲解；内容主要是2009~2014期间学术界关于HMM-DNN架构的论文；
《模式识别》: 这本书第四章的非线性分类器作为神经网络的入门还是很合适的，理论讲解很详细；

网络课程
------------------------------------------------------

（1）ASR webpage （ASR 课程）
（2）Speech Processing: 15-492/18-492 (CMU ASR课程）

一些工具的使用方法
------------------------------------------------------

FFmpeg
http://blog.csdn.net/Allyli0022/article/details/78355248

sox
todo


常见问题与解答
------------------------------------------------------
kaldi triphone decision tree 训练生成的tree结构是怎样的？
见回答：https://www.zhihu.com/question/263969544/answer/275975955
