[![Build Status](https://travis-ci.org/Jackiexiao/MTTS.svg?branch=dev)](https://travis-ci.org/Jackiexiao/MTTS)
[![Coverage Status](https://coveralls.io/repos/github/Jackiexiao/MTTS/badge.svg?branch=master)](https://coveralls.io/github/Jackiexiao/MTTS?branch=master)
# MTTS Mandarin/Chinese Text to Speech FrontEnd

[English README](https://github.com/Jackiexiao/MTTS/blob/master/README.md)  
中文版本不保证与英文版本同步

**ON_DEVELOPMENT**

Mandarin/Chinese Text to Speech based on statistical parametric speech 
synthesis using merlin toolkit

文档 [MTTS Document](http://mtts.readthedocs.io/zh_CN/latest/#)  

## 使用的数据
使用了15个小时的音频，但不是开源的音频。你可以使用thchs30的数据来做测试，或者自己录音

## 生成音频样例
使用了训练集内的Label生成语音 https://jackiexiao.github.io/MTTS/

我也用thchs30中A11发音人的250句语音训练并合成了音频样例，见上面的网站

## 如何复现

1. 首先你需要语料库（包含音频文本，韵律标注可以不要）
2. 然后通过这个项目生成HTS Label
3. 使用[merlin/egs/mandarin_voice](https://github.com/CSTR-Edinburgh/merlin/tree/master/egs/mandarin_voice) 进行训练

## 上下文相关标注与问题集
* [Context related annotation上下文相关标注](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_label.md)
* [Question Set问题集](https://github.com/Jackiexiao/MTTS/blob/master/misc/questions-mandarin.hed)
* [Rules to design a Question Set问题集设计规则](https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/question.md)


## 安装
Python : python3.6  
System: linux(tested on ubuntu16.04)  
```
pip install jieba pypinyin
sudo apt-get install libatlas3-base
```
自行下载下面的文件或者run `bash tools/install_mtts.sh`  
Download [montreal-forced-aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.0/montreal-forced-aligner_linux.tar.gz) and unzip to directory tools/  
Download acoustic_model
[thchs30.zip](https://github.com/Jackiexiao/MTTS/releases/download/v0.1/thchs30.zip) and copy to directory misc/  

**测试demo**
```
bash run_demo.sh
```

## 使用方法
### 1. 使用音频文本生成HTS Label
* Usage: Enter dir `MTTS/src` Run `python mtts.py txtfile wav_directory_path output_directory_path` (Absolute path or relative path) Then you will get HTS label
* 注意：只能含有中文文本，不能有阿拉伯数字或者英文字母

**txtfile example**
```
A_01 这是一段文本
A_02 这是第二段文本
```
**wav_directory example**采样率应大于16khz
```
A_01.wav  
A_02.wav  
```

### 2. 使用音频以及对齐好文本和音频的标注文件 生成 HTS Label
具体使用方法见源代码
[mandarin_frontend.py](https://github.com/Jackiexiao/MTTS/blob/master/src/mandarin_frontend.py)

### 3. Forced-alignment 音频文本对齐
This project use [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) to do forced alignment
1. We trained the acoustic model using thchs30 dataset, see `misc/thchs30.zip`, the dictionary we use [mandarin_mtts.lexicon](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_mtts.lexicon)
2. If you want to use mfa's (montreal-forced-aligner) pre-trained mandarin model, this is the dictionary you need [mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon)

## 韵律标注
没有韵律标注也可以生成Label

代码中#0表示词语的边界，#1表示韵律词，#2表示重音，#3表示韵律短语，#4表示语调短语。本项目规定词语比韵律词小，代码里自动进行了调整。当不输入韵律时也能够生成可用的label，不过合成的语音韵律感不强

## 贡献者
* Jackiexiao
* willian56

