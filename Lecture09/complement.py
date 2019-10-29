seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a=seq.replace('A', 't')
b=a.replace('T', 'a')
c=b.replace('C', 'g')
d=c.replace('G', 'c')

e=d.replace('a', 'A')
f=e.replace('t', 'T')
g=f.replace('c', 'C')
h=g.replace('g', 'G')

print(h)

