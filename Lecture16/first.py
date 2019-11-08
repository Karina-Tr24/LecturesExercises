import os,sys
import numpy as np
import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]
window = 10000

AT=[]
GC=[]

for start in range(len(ecoli)-window):
  win = ecoli[start:start+window]
  AT1=(win.count('T')/window)
  AT2=(win.count('A')/window)
  AT.append((AT1+AT2))
  GC1=(win.count('G' and 'C')/window)
  GC2=(win.count('G' and 'C')/window)
  GC.append((GC1+GC2))
  #GC.append(win.count('C')/window)
plt.figure(figsize=(20,10))
plt.plot(AT, label="AT")
plt.plot(GC, label="GC")
plt.ylabel('Fraction of AT or GC')
plt.xlabel('Position on genome')
plt.legend()
plt.savefig("Lecture16_ATc.png",transparent=True)
plt.show()