语音合成
==============================

1 语音合成的步骤和所需要的文件
-----------------------------------

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

2 训练模型——Duration和声学模型
-----------------------------------

语音合成和语音识别是一个相反的过程, 在语音 识别中, 给定的是一个 HMM 模型和观测序列(也就是 特征参数, 是从输入语音中提取得到), 要计算的是这 些观测序列对应的最有可能的音节序列, 然后根据语 法信息得到识别的文本. 而在合成系统中, 给定的是 HMM 模型和音节序列(经过文本分析得到的结果), 要 计算的是这些音节序列对应的观测序列, 也就是特征 参数.  

HTS的训练部分的作用就是由最初的原始语料库经过处理和模型训练后得到这些训练语料的HMM模型[5]。建模方式的选择首先是状态数的选择,因为语音的时序特性,一个模型的状态数量将影响每个状态持续的长短,一般根据基元确定。音素或半音节的基元,一般采用5状态的HMM;音节的基元一般采用10个状态。在实际的建模中,为了模型的简化,可以将HMM中的转移矩阵用一个时长模型(dur)替代,构成半隐马尔可夫模型HSMM hidden semi-Markov Model。用多空间概率分布对清浊音段进行联合建模,可以取得很好的效果。HTS的合成部分相当于训练部分的逆过程,作用在于由已经训练完成的HMM在输入文本的指导下生成参数,最终生成语音波形。具体的流程是:

 - 通过一定的语法规则、语言学的规律得到合成所需的上下文信息,标注在合成label中。
 - 待合成的label经过训练部分得到的决策树决策,得到语境最相近的叶结点HMM就是模型的决策。
 - 由决策出来的模型解算出合成的基频、频谱参数。根据时长的模型得到各个状态的帧数,由基频、频谱模型的均值和方差算出在相应状态的持续时长帧数内的各维参数数值,结合动态特征,最终解算出合成参数。
 - 由解算出的参数构建源-滤波器模型,合成语音。源的选取如上文所述:对于有基频段,用基频对应的单一频率脉冲序列作为激励;对于无基频段,用高斯白噪声作为激励

HSMM半隐马尔可夫模型的解释如下

A hidden semi-Markov model (HSMM) is a statistical model with the same structure as a `hidden Markov model <https://en.wikipedia.org/wiki/Hidden_Markov_model>`_ except that the unobservable process is `semi-Markov <https://en.wikipedia.org/wiki/Semi-Markov_process>`_ rather than `Markov <https://en.wikipedia.org/wiki/Markov_process>`_ . This means that the probability of there being a change in the hidden state depends on the amount of time that has elapsed since entry into the current state. This is in contrast to hidden Markov models where there is a constant probability of changing state given survival in the state up to that time

