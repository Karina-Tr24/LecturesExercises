#!/usr/bin/python3
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/localdisk/data/BPSM/Lecture17_AI/eukaryotes.txt', sep="\t")

#how many fungal species have genomes bigger than 100Mb
fungi=df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )].shape[0]
print(fungi) 