# -*- coding: utf-8 -*-
import os
import json
import time
import argparse

"""
Problema a resolver:

Necesitaría un comando en bash, para el siguiente caso, partiendo de un archivo llamado silences.txt el cual contiene las siguientes variables (adjunto el archivo):

start=0
end=3.29354
start=3.2936
end=4.45381
start=6.01685
end=8.52908
start=8.52915
end=9.0376
start=9.20075
end=11.1182
start=13.068
end=13.6636
...

Necesitaría un bucle que lea cada variable $start y $end, en el siguiente script:

ffmpeg -i in.wav -c:v copy -af volume=0:enable='between(t\,$start\,$end)' output.wav


A nivel informativo, lo que hace el script es limpiar los ruidos comprendidos en los tiempos entre $start y $end, bajándoles el volumen completamente. El archivo de audio se llama in.wav, y el archivo resultante completamente limpio de ruidos, se llama output.wav
Para ello uso la maravillosa librería de audio ffmpeg, pero no te compliques yo hago todo el testing que necesites.

"""

descrip = str("FFMPEG AUDIO CLEANER:\n "
"Utilidad para limpiar audio de archivos wav con ffmpeg ")


class AudioCleaner:

    def __init__(self):
        self.read = []
        self.lines = []
        self.source_silences = "./silences_duration.txt"
        self.input_wav = "./in.wav"
        self.sound_delay = 0.01000

    def convert_json(self):
        sfile = open(self.source_silences, "r")
        dfile = open("./silences.txt", "w")
        jline = ""
        for aline in sfile:
            if "silence_start" in aline:
                jline = "{\"start\": " + str(round(float(aline.split("=")[1].rstrip("\n")) + float(self.sound_delay), 5))
            elif "silence_end" in aline:
                jline += ", \"end\": " + str(round(float(aline.split("=")[1].rstrip("\n")) - float(self.sound_delay), 5)) + "}\n"
                dfile.write(jline)
        sfile.close()
        dfile.close()

    def get_from_file(self):
        with open('./silences.txt') as f:
            self.read = f.read().splitlines()
            for r in self.read:
                print(r)
                self.lines.append(json.loads(r))
            # print(self.lines)

    def clean_audio(self):
        os.system("cp " + self.input_wav + " temporal_input.wav")
        time.sleep(3)
        for line in self.lines:
            print("Limpando desde: " + str(line['start']) + " hasta: " + str(line['end']))
            # print("ffmpeg -i in.wav -c:v copy -af volume=0:enable='between(t\," + str(line['start']) + "\," + str(line['end']) + ")' output.wav")
            os.system("ffmpeg -y -i temporal_input.wav -c:v copy -af volume=0:enable='between(t\," + str(line['start']) + "\," + str(line['end']) + ")' temporal_output.wav")
            time.sleep(0.5)
            os.system("cp -f temporal_output.wav temporal_input.wav")
            time.sleep(0.5)
        # os.system("cp temporal_output.wav output.wav -f")

    def clean_temp_files(self):
        os.system("rm -f temporal_input.wav")
        # os.system("rm -f temporal_output.wav")
        #os.system("rm -f silences.txt")


if __name__ == "__main__":
    ac = AudioCleaner()

    parser = argparse.ArgumentParser(description=str(descrip))
    parser.add_argument("-C", "--convert", help="Convierte a JSON el fichero silences_duration.txt que le pasemos, si no le pasamos nada coge silences_duration.txt en el directorio donde se ejecute el script.")
    parser.add_argument("-I", "--input", help="Obtiene el input.wav, si no le pasamos este argumento, pilla el archivo in.wav en el directorio donde ejecutemos el script.")
    parser.add_argument("-D", "--delay", help="suma tiempo en start y resta en el end para evitar que se coma letras")
    args = parser.parse_args()

    if args.convert:
        ac.source_silences = args.convert

    if args.input:
        ac.input_wav = args.input

    if args.delay:
        ac.sound_delay = args.delay

    ac.convert_json()
    ac.get_from_file()
    ac.clean_audio()
    ac.clean_temp_files()
