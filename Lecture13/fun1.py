#!/usr/bin/python3
import os, sys, subprocess

def percentage(seq, aa):
	length=len(seq)
	aac=seq.count(aa)
	per=(aac/length)*100
	return per

#the second doesnt work
assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
