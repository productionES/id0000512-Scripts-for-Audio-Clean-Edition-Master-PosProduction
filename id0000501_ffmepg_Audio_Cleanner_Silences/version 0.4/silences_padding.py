# -*- coding: utf-8 -*-
import os
import json
import time
import argparse

class SilencesPadding:

    def __init__(self):
        self.source_silences = "./silences_duration.txt"
        self.sound_delay = 0.0000

    def convert_silences(self):
        sfile = open(self.source_silences, "r")
        dfile = open("./silences_duration_with_padding.txt", "w")
        jline = ""
        for aline in sfile:
            if "silence_start" in aline:
                jline = "lavfi.silence_start=" + str(round(float(aline.split("=")[1].rstrip("\n")) + float(self.sound_delay), 5)) + "\n"
                dfile.write(jline)
            elif "silence_end" in aline:
                jline = "lavfi.silence_end=" + str(round(float(aline.split("=")[1].rstrip("\n")) - float(self.sound_delay), 5)) + "\n"
                dfile.write(jline)
            else:
                dfile.write(aline)
        sfile.close()
        dfile.close()


if __name__ == "__main__":
    sp = SilencesPadding()

    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--input", help="Input del silences.txt, si no se le pasa pilla silences_duration.txt")
    parser.add_argument("-D", "--delay", help="suma tiempo en start y resta en el end para evitar que se coma letras")
    args = parser.parse_args()

    if args.input:
        sp.input_wav = args.input

    if args.delay:
        sp.sound_delay = args.delay

    sp.convert_silences()
