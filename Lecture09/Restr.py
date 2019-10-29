seq="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut=seq.find("AATTC")
s=(seq[cut:len(seq)])
s1=len(seq)-len(s)
s2=len(s)
print("The size of the fragments are: ", s1, s2)
