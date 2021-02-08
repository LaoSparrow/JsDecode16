#!/bin/python

#This script is really a rubbish. (Also my English)
#Because I will only use it for once.
#I won't left any comments on it

#Author: LaoSparrow

ret = input('Path to the file:')

f = open(ret,'r')
f.seek(0, 0)
inpf = f.read()
f.close()

outf = open('output.js','a+',encoding='UTF-8')
outf.seek(0,0)

jumpchar = 0
Hi4Bits = 0
Lo4Bits = 0
for i in range(0, len(inpf)):
    if jumpchar <= 0:
        if inpf[i:i+2] == '\\x':

            b = 0
            for char in '0123456789ABCDEF':
                if inpf[i+2] == char:
                    Hi4Bits = b
                if inpf[i+3] == char:
                    Lo4Bits = b
                b+=1
            asciiNum = Hi4Bits<<4 | Lo4Bits

            ret = chr(asciiNum)
            outf.write(ret)
            jumpchar = 3
        else:
            outf.write(inpf[i])
    else:
        jumpchar-=1

outf.close()