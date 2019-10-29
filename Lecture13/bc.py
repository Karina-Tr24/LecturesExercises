#!/usr/bin/python3
import os, sys, subprocess

def undet(seq):
	length=len(seq)
	bp=seq.count('t') + seq.count('a') + seq.count('c') + seq.count('g')
	per=(bp/length)*100
	if per>40:
		TF='True'
	else:
		TF='False'
	return TF

assert undet("atcggtcsatcscscsca") == 'True'
assert undet("aaatggcagctacxxxxxggggaaattcgcgcgcgc") == 'True'
assert undet("acatctxxxxxxxxddddeeeee") == 'False'
