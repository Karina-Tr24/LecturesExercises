
IFS=$'\t'
count=0 
while read querryac subjectac identity alignmentlength mismatches gapopens q_start q_end s_start s_end evalue bitscore
 do 	
 count=$((count +1))
 echo -e "$count\t$subjectac"
done < blastoutput2.out

