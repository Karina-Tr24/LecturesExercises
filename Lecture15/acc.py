#!/usr/bin/python3
import os, sys, subprocess, shutil, re

accnum=['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

for num in accnum:
  if re.search(r'5',num):
    print('Found a 5 in acc number: ' + num)

print('\n')    
for num in accnum:
  if re.search(r'[d|e]',num):
    print('Found d or e in acc number: ' + num)
    
print('\n')    
for num in accnum:
  if re.search(r'de',num):
    print('Found de in acc number: ' + num)
    
print('\n')    
for num in accnum:
  if re.search(r'(d.e)',num):
    print('Found d and e with a character in the middle in acc number: ' + num)

print('\n')    
for num in accnum:
  if re.search(r'd',num) and re.search(r'e',num):
    print('Found d and e in acc number: ' + num)

print('\n')    
for num in accnum:
  if re.search(r'^[x|y]',num):
    print('Start with x or y in acc number: ' + num)
    
print('\n')    
for num in accnum:
  if re.search(r'^[x|y]',num) and re.search(r'e$',num):
    print('Start with x or y and end with e in acc number: ' + num)
    
print('\n')    
for num in accnum:
  if re.search(r'\d{3,}',num):
    print('3<= row in acc number: ' + num)
    
print('\n')    
for num in accnum:
  if re.search(r'd[arp]$',num):
    print('end with d follow by a,r or p: ' + num)