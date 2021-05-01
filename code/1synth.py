import tomita.legacy.pysynth as ps
import tomita.legacy.mixfiles as mx
import tomita.legacy.play_wav as pw
import pyaudio
import tomita.legacy.readmidi as mr
from playsound import playsound
import pygame
f=open("C:/Users/bohee/source/pyspace/code/code.txt","w")
ar=['a4','a#4','b4','c4','c#4','d4','d#4','e4','f4','f#4','g4','g#4','a4','a#4','b4','c4','c#4','d4','d#4']
# for i in ar:
#     f.write('song=[[\''+i+'\',1]]\nps.make_wav(song,fn=\"'+i[:-1]+'1.wav\")\n')
# for i in range(12):
#     f.write('mx.mix_files("'+ar[i][:-1]+'1.wav","'+ar[i+4][:-1]+'1.wav","file1.wav",chann=2,phase=-1.0)\n')
#     f.write('mx.mix_files("file1.wav","'+ar[i+7][:-1]+'1.wav","'+ar[i][:-1]+'1.wav",chann=2,phase=-1.0)\n')


# mx.mix_files("a.wav", "b.wav", "d.wav", chann=2, phase=-1.0)
# mx.mix_files("d.wav", "c.wav", "A4.wav", chann=2, phase=-1.0)
# song=[['a4',1]]
# ps.make_wav(song,fn="a.wav")
# song=[['c#4',1]]
# ps.make_wav(song,fn="b.wav")
# song=[['e4',1]]
# ps.make_wav(song,fn="c.wav")




# mx.mix_files("a.wav", "b.wav", "d.wav", chann=2, phase=-1.0)
# mx.mix_files("d.wav", "c.wav", "A4.wav", chann=2, phase=-1.0)


# song=[['f#4',1]]
# ps.make_wav(song,fn="a.wav")
# song=[['a4',1]]
# ps.make_wav(song,fn="b.wav")
# song=[['c#4',1]]
# ps.make_wav(song,fn="c.wav")
# mx.mix_files("a.wav", "b.wav", "d.wav", chann=2, phase=-1.0)
# mx.mix_files("d.wav", "c.wav", "Gbmcode.wav", chann=2, phase=-1.0)


def code(onecode):
    #asm2 / abm4 / a8 / => code2/a#m2.wav    code4/abm4.wav
    #am2 a#2 ab2

    Code="code"
    Code+=(onecode[-1]+"/")
    Code+=onecode[0].upper()
    for s in onecode[1:]:
        if s=="s":
            Code+="#"
        else:
            Code+=s
    Code+=".wav"
   # print(Code)
    return Code
pygame.mixer.init()
global basepath
basepath="C:/Users/bohee/source/pyspace/code/"


def play(codelist):
    global basepath
    for code in codelist:
        while pygame.mixer.get_busy():
            pass
        for _ in range(int(code[1])):
            while pygame.mixer.get_busy():
                pass
            sound=pygame.mixer.Sound(basepath+code[0])
            #print(basepath+code)
            sound.play()    


codelist=[]
C=input().split()
while C[0]!='0':
    
    codelist.append([code(C[0]),C[1]])
    C=input().split()
play(codelist)
input()
# pygame.mixer.init()

# while True:
#     s=input()#code1/a1.wav
#     for i in range(4):  
#         c8()
#     for i in range(4):  
#         g8()



