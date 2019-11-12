#!/usr/bin/python3
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/localdisk/data/BPSM/Lecture17_AI/eukaryotes.txt', sep="\t")

#how many fungal species have genomes bigger than 100Mb
fungi=df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )]
print(fungi.shape[0]) 
#Set of names of fungi sequences
print(set(df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )]['#Organism/Name']))

#question 2
print('Sequences in Fungi: ', df[df.apply(lambda x : x['Group'] in ['Fungi'], axis=1)].shape[0])
print('Sequences in Plants: ', df[df.apply(lambda x : x['Group'] in ['Plants'], axis=1)].shape[0])
print('Sequences in Animals: ', df[df.apply(lambda x : x['Group'] in ['Animals'], axis=1)].shape[0])
print('Sequences in Protists: ', df[df.apply(lambda x : x['Group'] in ['Protists'], axis=1)].shape[0])
print('Sequences in Other: ', df[df.apply(lambda x : x['Group'] in ['Other'], axis=1)].shape[0])

#third question
df['genus'] = df.apply(lambda x : x['#Organism/Name'].split(' ')[0], axis=1)
print(set(df[df.apply(lambda x: x['genus'] in ['Heliconius'],axis=1)]['#Organism/Name']))
print(df[df.apply(lambda x: x['genus'] in ['Heliconius'],axis=1)]['#Organism/Name'].shape[0])

#4th question
print('Name of the center the center that has sequences most plant genomes and how many: ',df[df.apply(lambda x : x['Group'] in ['Plants'], axis=1)]['Center'].value_counts().head(1))
print('Name of the center the center that has sequences most insect genomes and how many: ',df[df.apply(lambda x : x['SubGroup'] in ['Insects'], axis=1)]['Center'].value_counts().head(1))