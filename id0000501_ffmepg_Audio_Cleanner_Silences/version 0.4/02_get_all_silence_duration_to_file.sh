#!bin/bash
# See Example 6 from https://digitalcardboard.com/blog/2009/08/25/the-sox-of-silence/
fileName=out
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
newFileName=$fileName.$current_time.wav
yourPathAPP=/Volumes/6TB/Applications/ocenaudio.app
ffmpeg -i in.wav -af silencedetect=n=-30dB:d=0.5,ametadata=print:file=silences_duration.txt -f null -

open -a "$yourPathAPP" $newFileName
