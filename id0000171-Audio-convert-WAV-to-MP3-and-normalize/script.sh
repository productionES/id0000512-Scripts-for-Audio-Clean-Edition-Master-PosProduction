#!/bin/sh

sox in.wav --norm out.wav
lame -b 192 out.wav out.mp3