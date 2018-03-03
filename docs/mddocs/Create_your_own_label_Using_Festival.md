Test on ubuntu 16.04. Language: English 

Tools: Festival && Merlin

**1. download files and copy to merlin/tools**

* [speech_tools](http://festvox.org/packed/festival/2.4/speech_tools-2.4-release.tar.gz)
* [festival](http://festvox.org/packed/festival/2.4/festival-2.4-release.tar.gz)
* [festvox](http://festvox.org/download.html)

**2. Unzip to merlin/tools**

``` 
tar -zxvf speech_tools-2.4-release.tar.gz festival-2.4-release.tar.gz festvox-2.7.0-release.tar.gz
```

**3. INSTALL speech tool && festival && festvox**

Attention: You can read the INSTALL file in(merlin/tools/festival && /speech_tools && /festvox ) if you failed to install festival 

**(1)First download Lexicon and put them in corresponding dir( /merlin/tools/festival/lib/dicts )**

* [http://festvox.org/packed/festival/2.4/festlex_CMU.tar.gz](http://festvox.org/packed/festival/2.4/festlex_CMU.tar.gz)
* [http://festvox.org/packed/festival/2.4/festlex_OALD.tar.gz](http://festvox.org/packed/festival/2.4/festlex_OALD.tar.gz)
* [http://festvox.org/packed/festival/2.4/festlex_POSLEX.tar.gz](http://festvox.org/packed/festival/2.4/festlex_POSLEX.tar.gz)

**(2) Download test Voice and put them in corresponding dir**

* [http://festvox.org/packed/festival/2.4/voices/festvox_rablpc16k.tar.gz](http://festvox.org/packed/festival/2.4/voices/festvox_rablpc16k.tar.gz)
* [http://festvox.org/packed/festival/2.4/voices/festvox_kallpc16k.tar.gz](http://festvox.org/packed/festival/2.4/voices/festvox_kallpc16k.tar.gz)

**(3) Installation order: speech tool——festival ——festvox**

Install Dependent library (as far as I know)
```
sudo apt-get -y install libncurses5 libncurses5-dev libcurses-ocaml 
```

**Speech tool**
```
cd speech_tools
./configure
make
make test
```

**Festival**
```
cd festival
./configure
make
make test
```

**Festvox**

```
cd festival
./configure
make
```
**4.Set Path**
```
bash ~$ export FESTVOXDIR=/home/awb/projects/festvox/

bash ~$ export ESTDIR=/home/awb/projects/speech_tools/
```

**5.Using Merlin to generate label**

There are two ways to generate label file from txt 

**txt format**：
```
( arctic_a0001 "Author of the danger trail, Philip Steels, etc." )
```
**(1) /merlin/misc/scripts/alignment/phone_align**

Please read the README.md

**(2) merlin/egs/slt_arctic/s1/experiments/slt_arctic_demo/test_synthesis/**

create dir /txt which contain txt file  
run merlin/egs/slt_arctic/s1/merlin_synthesis.sh and then you can get your own label for synthesis
