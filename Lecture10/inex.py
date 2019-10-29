#!/usr/bin/python3
import os, subprocess, shutil
import sys
plain=input("Name of the file where the sequence is: ")

plain_text=open(plain)
seq=plain_text.read()

e2=(seq[90:len(seq)])
e1=seq[0:63]
e=e1 + e2

i=seq[63:90]

exon=open("exons.fasta","w")
exon.write(e1.upper()+"\n"+e2.upper())
exon.close()
print(open("exons.fasta").read())

intron=open("intron.fasta","w")
intron.write(i.upper())
intron.close()
print(open("intron.fasta").read())


