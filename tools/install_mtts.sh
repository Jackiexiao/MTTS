#!/bin/bash

tools_dir=$(dirname $0)
cd $tools_dir

mfa_path="./montreal-forced-aligner"
thchs_path="../misc/thchs30.zip"

if [ ! -d $mfa_path ]; then
    wget https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/download/v1.0.0/montreal-forced-aligner_linux.tar.gz
    tar -zxvf montreal-forced-aligner_linux.tar.gz
fi

if [ ! -e $thchs_path ]; then
    wget https://github.com/Jackiexiao/MTTS/raw/gh-pages/resource/thchs30.zip
    mv thchs30.zip ../misc
fi
