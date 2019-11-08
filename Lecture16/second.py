import os,sys
import numpy as np
import matplotlib.pyplot as plt

ali = open("alignment.txt")
counter=0
aligned_seq=[]
for line in ali:
  counter+=1
  aligned_seq.append(line.rstrip("\n"))
al_length=len(aligned_seq[0])
uniques=[]

for colnum in range(al_length):
  column=[]
  for seq in aligned_seq:
    aa=seq[colnum]
    if aa != '-':
      column.append(seq[colnum])
  uniq=len(set(column))
  uniques.append(uniq)
  print(len(uniques))
    
window = 15
numbers_to_plot = []
for start in range(len(uniques) - window):
    win = uniques[start:start+window]
    score = sum(win) / len(win)
    numbers_to_plot.append(score)

plt.figure(figsize=(15,8))
plt.xlim(0,len(numbers_to_plot))
plt.plot(numbers_to_plot,linewidth=3,color="purple")
plt.title('EXERCISE 2')
plt.ylabel('Unique amino acid residues')
plt.xlabel('Residue position')
plt.savefig("Lecture16_second.png",transparent=True)
plt.show()
