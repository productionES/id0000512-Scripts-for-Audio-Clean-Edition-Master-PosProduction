# -*- coding: utf-8 -*-
import os
import json
import time
import argparse
import subprocess
import re

class TalkingPadding:

    def __init__(self):
        self.path_wav = ""
        self.source_silences = "./silences_duration.txt"
        self.sound_delay = 0.00000

    def obtain_duration(self):
        process = subprocess.Popen(['ffmpeg', '-i', self.path_wav], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout.decode("utf-8"), re.DOTALL).groupdict()
        ret_time = float(0)
        ret_time += int(matches['hours'] * 60 * 60)
        ret_time += int(matches['minutes'] * 60)
        ret_time += float(matches['seconds'])
        # print('{:.5f}'.format(round(float(ret_time), 5)))
        return('{:.5f}'.format(round(float(ret_time), 5)))
        # print(round(float(ret_time), 5))
        # print(matches['hours'])
        # print(matches['minutes'])
        # print(matches['seconds'])

    def convert_silences(self):
        sfile = open(self.source_silences, "r")
        dfile = open("./talking_duration_with_padding.txt", "w")
        jline = ""
        jline = "lavfi.silence_start=0.00000" + "\n"
        dfile.write(jline)
        for aline in sfile:
            if "silence_start" in aline:
                jline = "lavfi.silence_end=" + str(round(float(aline.split("=")[1].rstrip("\n")) + float(self.sound_delay), 5)) + "\n"
                dfile.write(jline)
            elif "silence_end" in aline:
                jline = "lavfi.silence_start=" + str(round(float(aline.split("=")[1].rstrip("\n")) - float(self.sound_delay), 5)) + "\n"
                dfile.write(jline)
            else:
                dfile.write(aline)
        jline = "lavfi.silence_end=" + self.obtain_duration() + "\n"
        dfile.write(jline)
        sfile.close()
        dfile.close()


if __name__ == "__main__":
    tp = TalkingPadding()

    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--input", help="Input del silences.txt, si no se le pasa pilla silences_duration.txt")
    parser.add_argument("-D", "--delay", help="suma tiempo en start y resta en el end para evitar que se coma letras")
    parser.add_argument("-P", "--path", help="Se le adjunta el path del archivo wav para obtener la duración total.")
    args = parser.parse_args()

    if args.input:
        tp.input_wav = args.input

    if args.delay:
        tp.sound_delay = args.delay

    if args.path:
        tp.path_wav = args.path

    #tp.obtain_duration()
    tp.convert_silences()
