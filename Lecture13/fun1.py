#!/usr/bin/python3
import os, sys, subprocess

def percentage2(seq, aa=['A','I','L','M','F','W','Y','V']):
	aac=0	
	length=len(seq)
	for a in aa:
		aac += seq.count(a)
	per=(aac/length)*100	
	return per

assert round(percentage2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(percentage2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(percentage2("MSRSLLLRFLLFLLLLPPLP")) == 65
