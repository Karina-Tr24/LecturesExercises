#!/usr/bin/python3
newfile=open("input.txt")
output=open("ex1out.txt","a")
for line in newfile:
	output.write(line[14:])
	print(len(line[14:]))
output.close() 
