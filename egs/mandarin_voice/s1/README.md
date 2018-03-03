# Mandarin Voice

(1) Create the following dir and copy your file to dir (suppose current dir is merlin/egs/mandarin_voice/s1/)

* database/wav 
* database/labels/label_phone_align 
* database/prompt-lab 
* cp MTTS/misc/questions-mandarin.hed to ~/merlin/misc/questions/

(2) modify merlin's source code
* in `merlin/src/frontend/label_normalisation.py`, add after line 903(function wildcards2regex ) ` question = question.replace('\\?', '.')`
 so it can support Question Set '?' style
* in `src/frontend/label_normalisation.py` replace all `frame_number = int((end_time - start_time) / 50000)` to `frame_number = int(end_time/50000) - int(start_time / 50000)` because not every time stamp is exactly divisible by 50000
* ~~If your wav's sampleing rate is 44.1khz, you should modify all conf, set
framelength = 2048 fw_alpha = 0.76 (these parametes is using in vocoder world~~ script already do it

(3) modify params as per your own data in 01_setup.sh file, especially

* Voice Name
* QuestionFile
* Labels_Type(phone_align or state_align)
* SamplingFreq
* Train
* Valid
* Test

default setting is 

* QuestionFile=questions-mandarin.hed
* Labels=phone_align
* SamplingFreq=44100
* Train=40
* Valid=5
* Test=5

(4) then run

```
./run_mandarin_voice.sh
```
