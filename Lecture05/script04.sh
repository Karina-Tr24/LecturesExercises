rm -f *.details
IFS=$'\t'
count=0 
while read querryac subjectac identity alignmentlength mismatches gapopens q_start q_end s_start s_end evalue bitscore
 do 	
 if !(test -z $subjectac)
 then
 count=$((count +1))
 echo 	-e "$count\t$subjectac" >> list.details
fi #for get rid of blanck spaces
done < blastoutput2.out | tail -20


