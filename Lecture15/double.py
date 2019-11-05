#!/usr/bin/python3
import os, sys, subprocess, shutil, re

dnafile=open("long_dna.txt").read()

position=re.search('A.TAAT',dnafile).start()
print('the first contains: '+str(position+3)+ ' bases')
print('the second  contains: '+str(len(dnafile)-(position+3))+ ' bases')