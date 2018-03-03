#!/bin/bash

demo_voice=thchs30_250_demo
data_url=https://github.com/Jackiexiao/MTTS/raw/gh-pages/resource/thchs30_250_demo.tar.gz
data_dir=data
demo_voice_path=${data_dir}/${demo_voice}

mkdir -p $data_dir

if [ ! -d ${demo_voice_path} ]; then
    echo "downloading data......"
    wget $data_url
    tar -zxvf ${demo_voice}.tar.gz -C ${data_dir}
fi

python src/mtts.py ${demo_voice_path}/A11.txt ${demo_voice_path}/wav ${demo_voice_path}/output

