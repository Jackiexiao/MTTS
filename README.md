[![Build Status](https://travis-ci.org/Jackiexiao/MTTS.svg?branch=dev)](https://travis-ci.org/Jackiexiao/MTTS)
<!--[![Coverage Status](https://coveralls.io/repos/github/Jackiexiao/MTTS/badge.svg?branch=master)](https://coveralls.io/github/Jackiexiao/MTTS?branch=master)-->
# MTTS Mandarin/Chinese Text to Speech FrontEnd

Mandarin/Chinese Text to Speech based on statistical parametric speech 
synthesis using merlin toolkit

Read the document (write in Chinese) at [MTTS Document](http://mtts.readthedocs.io/zh_CN/latest/#)

## Data
Using 15 hours of wav for a mandarin speech synthesis dataset which is not
open-source, but you can use thchs30 dataset to run the demo (or record wav by
yourself)

## Generated Samples
Using Training Sets Label to generate wav https://jackiexiao.github.io/MTTS/

I also use thchs30 dataset to train (only using 250 wavs for A11 speaker), see
the website above

## How To Reproduce
1. First, you need data contain wav and txt (prosody mark is optional)
2. Second, generate HTS label using this project 
3. Using [merlin/egs/mandarin_voice](https://github.com/CSTR-Edinburgh/merlin/tree/master/egs/mandarin_voice) to train

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
* Usage: Enter dir `MTTS/src` Run `python mtts.py txtfile wav_directory_path output_directory_path` (Absolute path or relative path) Then you will get HTS label
* Attention: Currently only support Chinese Character, txt should not have any
    Arabia number or English alphabet

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

### 2. Generate Label by wav and alignment file
see source code for more information, but pay attention to the sfs file, the
format is `endtime phone_type` not `start_time, phone_type`(which is different
from speech ocean's data)

[mandarin_frontend.py](https://github.com/Jackiexiao/MTTS/blob/master/src/mandarin_frontend.py)

### 3. Forced-alignment
This project use [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) to do forced alignment
1. We trained the acoustic model using thchs30 dataset, see `misc/thchs30.zip`, the dictionary we use [mandarin_mtts.lexicon](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_mtts.lexicon)
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
* Polyphone Problem
* Better Label format and Question Set
* Improvement of prosody analyse
* Better alignment

## Contributor
* Jackiexiao
* willian56

