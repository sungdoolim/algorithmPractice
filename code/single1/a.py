import tomita.legacy.pysynth as ps
import tomita.legacy.mixfiles as mx
import tomita.legacy.play_wav as pw
import pyaudio
import tomita.legacy.readmidi as mr
from playsound import playsound
import pygame
f=open("C:/Users/bohee/source/pyspace/code/single1/code.txt","w")
ar=['a4','a#4','b4','c4','c#4','d4','d#4','e4','f4','f#4','g4','g#4','a4','a#4','b4','c4','c#4','d4','d#4']
# for i in ar:
#     f.write('song=[[\''+i+'\',16]]\nps.make_wav(song,fn=\"'+i[:-1]+'16.wav\")\n')
for i in range(12):
    f.write('mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/'+ar[i][:-1]+'16.wav","C:/Users/bohee/source/pyspace/code/single16/'+ar[i+3][:-1]+'16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)\n')
    f.write('mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/'+ar[i+7][:-1]+'16.wav","'+ar[i][:-1].upper()+'m16.wav",chann=2,phase=-1.0)\n')



mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/a16.wav","C:/Users/bohee/source/pyspace/code/single16/c16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/e16.wav","Am16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/a#16.wav","C:/Users/bohee/source/pyspace/code/single16/c#16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/f16.wav","A#m16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/b16.wav","C:/Users/bohee/source/pyspace/code/single16/d16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/f#16.wav","Bm16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/c16.wav","C:/Users/bohee/source/pyspace/code/single16/d#16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/g16.wav","Cm16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/c#16.wav","C:/Users/bohee/source/pyspace/code/single16/e16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/g#16.wav","C#m16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/d16.wav","C:/Users/bohee/source/pyspace/code/single16/f16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/a16.wav","Dm16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/d#16.wav","C:/Users/bohee/source/pyspace/code/single16/f#16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/a#16.wav","D#m16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/e16.wav","C:/Users/bohee/source/pyspace/code/single16/g16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/b16.wav","Em16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/f16.wav","C:/Users/bohee/source/pyspace/code/single16/g#16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/c16.wav","Fm16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/f#16.wav","C:/Users/bohee/source/pyspace/code/single16/a16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/c#16.wav","F#m16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/g16.wav","C:/Users/bohee/source/pyspace/code/single16/a#16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/d16.wav","Gm16.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/g#16.wav","C:/Users/bohee/source/pyspace/code/single16/b16.wav","C:/Users/bohee/source/pyspace/code/single16/file1.wav",chann=2,phase=-1.0)
mx.mix_files("C:/Users/bohee/source/pyspace/code/single16/file1.wav","C:/Users/bohee/source/pyspace/code/single16/d#16.wav","G#m16.wav",chann=2,phase=-1.0)
