seq="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
e2=(seq[90:len(seq)])
e1=seq[0:63]
e=e1 + e2
print(e)

codseq=(len(e)/len(seq))*100
print("percentage of coding: ", codseq)

i=seq[63:90]
print(e1+i.lower()+e2)

