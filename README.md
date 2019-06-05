# 本项目已停止维护

[![Build Status](https://travis-ci.org/Jackiexiao/MTTS.svg?branch=dev)](https://travis-ci.org/Jackiexiao/MTTS)
<!--[![Coverage Status](https://coveralls.io/repos/github/Jackiexiao/MTTS/badge.svg?branch=master)](https://coveralls.io/github/Jackiexiao/MTTS?branch=master)-->
# A Demo of MTTS Mandarin/Chinese Text to Speech FrontEnd

Mandarin/Chinese Text to Speech based on statistical parametric speech 
synthesis using merlin toolkit

这只是一个语音合成前端的Demo，没有提供文本正则化，韵律预测功能，文字转拼音使用pypinyin，分词使用结巴分词，这两者的准确度也达不到商用水平。

欢迎加入语音合成技术交流QQ群：882726654

其他语音合成项目[传送门](https://github.com/topics/text-to-speech)，端到端是不错的方向，自然度要优于merlin。

This is only a demo of mandarin frontend which is lack of some parts like "text normalization" and "prosody prediction", and the phone set && Question Set this project use havn't fully tested yet.

一个粗略的文档：A draft [documentation](http://mtts.readthedocs.io/zh_CN/latest/#) written in Mandarin

## Data
There is no open-source mandarin speech synthesis dataset on the internet, this
proj used thchs30 dataset to demostrate speech synthesis

**UPDATE**

open-source mandarin speech synthesis data from data-banker company, 开源的中文语音合成数据，感谢标贝公司

【数据下载】https://weixinxcxdb.oss-cn-beijing.aliyuncs.com/gwYinPinKu/BZNSYP.rar
【数据说明】http://www.data-baker.com/open_source.html

## Generated Samples
Listen to  https://jackiexiao.github.io/MTTS/

## How To Reproduce
1. First, you need data contain wav and txt (prosody mark is optional)
2. Second, generate HTS label using this project 
3. Using [merlin/egs/mandarin_voice](https://github.com/CSTR-Edinburgh/merlin/tree/master/egs/mandarin_voice) to train and generate Mandarin Voice

## Context related annotation & Question Set
* [Context related annotation上下文相关标注](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_label.md)
* [Question Set问题集](https://github.com/Jackiexiao/MTTS/blob/master/misc/questions-mandarin.hed)
* [Rules to design a Question Set问题集设计规则](https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/question.md)

## Install
Python : python3.6  
System: linux(tested on ubuntu16.04)  
```
pip install jieba pypinyin
sudo apt-get install libatlas3-base
```
Run `bash tools/install_mtts.sh`  
**Or** download file by yourself
* Download [montreal-forced-aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.0/montreal-forced-aligner_linux.tar.gz) and unzip to directory tools/  
* Download acoustic_model
[thchs30.zip](https://github.com/Jackiexiao/MTTS/releases/download/v0.1/thchs30.zip) and copy to directory misc/  

**Run Demo**
```
bash run_demo.sh
```
## Usage
### 1. Generate HTS Label by wav and text
* Usage: Run `python src/mtts.py txtfile wav_directory_path output_directory_path` (Absolute path or relative path) Then you will get HTS label, if you have your own acoustic model trained by monthreal-forced-aligner, add`-a your_acoustic_model.zip`, otherwise, this project use thchs30.zip acoustic model as default
* Attention: Currently only support Chinese Character, txt should not have any
    Arabia number or English alphabet(不可包含阿拉伯数字和英文字符)

**txtfile example**
```
A_01 这是一段文本
A_02 这是第二段文本
```
**wav_directory example**(Sampleing Rate should larger than 16khz)
```
A_01.wav  
A_02.wav  
```

### 2. Generate HTS Label by text with or without alignment file
* Usage: Run `python src/mandarin_frontend.py txtfile output_directory_path` 
* or import mandarin_frontend
```
from mandarin_frontend import txt2label

result = txt2label('向香港特别行政区同胞澳门和台湾同胞海外侨胞')
[print(line) for line in result]

# with prosody mark and alignment file (sfs file)
# result = txt2label('向#1香港#2特别#1行政区#1同胞#4澳门#2和#1台湾#1同胞#4海外#1侨胞',
            sfsfile='example_file/example.sfs')
```
see [source
code](https://github.com/Jackiexiao/MTTS/blob/master/src/mandarin_frontend.py) for more information, but pay attention to the alignment file(sfs file), the format is `endtime phone_type` not `start_time, phone_type`(which is different from speech ocean's data)

### 3. Forced-alignment
This project use [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) to do forced alignment, if you want to get a better alignment, use your data to train a alignment-model, see [mfa: algin-using-only-the-dataset](https://montreal-forced-aligner.readthedocs.io/en/latest/aligning.html#align-using-only-the-data-set)
1. We trained the acoustic model using thchs30 dataset, see `misc/thchs30.zip`, the dictionary we use [mandarin_mtts.lexicon](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_mtts.lexicon). If you use larger dataset than thchs30, you may get better alignment.
2. If you want to use mfa's (montreal-forced-aligner) pre-trained mandarin model, this is the dictionary you need [mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon)

## Prosody Mark
You can generate HTS Label without prosody mark. we assume that word segment is
smaller than prosodic word(which is adjusted in code)

"#0","#1", "#2","#3" and "#4" are the prosody labeling symbols.
* #0 stands for word segment
* #1 stands for prosodic word
* #2 stands for stressful word (actually in this project we regrad it as #1)
* #3 stands for prosodic phrase
* #4 stands for intonational phrase 


## Improvement to be done in future
* Text Normalization
* Better Chinese word segment
* G2P: Polyphone Problem
* Better Label format and Question Set
* Improvement of prosody analyse
* Better alignment

## Contributor
* Jackiexiao
* willian56

