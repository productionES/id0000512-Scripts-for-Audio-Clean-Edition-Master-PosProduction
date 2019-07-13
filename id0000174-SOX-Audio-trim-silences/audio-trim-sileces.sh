#!/bin/bash
# sox in.wav out.wav silence 1 00:00:01.100 -44d
#sox in.wav out.wav silence -l 1 0.2 -44d -1 0.3 -44d

# get the path of Adobe Audition and add timestamp in the output filename
fileName=out
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
newFileName=$fileName.$current_time.wav
#yourPathAPP=/Applications/Adobe\ Audition\ CC\ 2019/Adobe\ Audition\ CC\ 2019.app
yourPathAPP=/Volumes/6TB/Applications/ocenaudio.app

# begining silence=00:00:03.000 and above-period=00:00:04.000 --> delete the file silence
# begining silence=00:00:03.000 and above-period=00:00:03.000 --> delete the file silence
# begining silence=00:00:03.000 and above-period=00:00:02.990 --> delete the file silence
# begining silence=00:00:03.000 and above-period=00:00:02.900 --> delete the file silence
# begining silence=00:00:03.000 and above-period=00:00:02.500 --> do nothing
# begining silence=00:00:03.000 and above-period=00:00:02.000 --> do nothing
# begining silence=00:00:03.000 and above-period=00:00:02.000 --> do nothing
# begining silence=00:00:03.000 and above-period=00:00:02.000 --> do nothing
sox in.wav $newFileName silence 1 00:00:02.000 -80d

# open the new output file in Adobe Audition
open -a "$yourPathAPP" $newFileName

