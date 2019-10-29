#!/usr/bin/python3

newfile=open("genomic_dna2.txt").read()
exonsfile=open("exons.txt").read().rsplit()
print(exonsfile)

output=open("newex2.txt","w")

for line in exonsfile:
	s=int(line.split(',')[0])-1
	e=int(line.split(',')[1])
	output.write(newfile[s:e])
	summary='Exon runs from '+str(line.split(',')[0])+' to '+str(e)
	print(summary,'\n\t',newfile[s:e])
output.close() 
