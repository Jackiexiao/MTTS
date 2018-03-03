#!/bin/bash
# or download montreal-forced-aligner_linux.tar.gz and thchs30.zip and move
# them to accordingly dir by yourself

tools_dir=$(dirname $0)
cd $tools_dir

mfa_path="./montreal-forced-aligner"
thchs_path="../misc/thchs30.zip"

data_mfa_url=https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.0/montreal-forced-aligner_linux.tar.gz
data_thchs30_url=https://github.com/Jackiexiao/MTTS/releases/download/v0.1/thchs30.zip

if [ ! -d $mfa_path ]; then
    wget $data_mfa_url
    tar -zxvf montreal-forced-aligner_linux.tar.gz
fi

if [ ! -e $thchs_path ]; then
    wget $data_thchs30_url
    mv thchs30.zip ../misc
fi
