sequence="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A=sequence.count('A')
T=sequence.count('T')
ATcontent=(A+T)/len(sequence)
print("AT content: "+str(ATcontent))

