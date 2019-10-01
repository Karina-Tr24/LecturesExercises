rm -f *.details
IFS=$'\t'
count=0
while read querryac subjectac identity alignmentlength mismatches gapopens q_start q_end s_start s_end evalue bitscore
 do
 if !(test -z $subjectac)
 then
	if test $mismatches -gt 20
	then
 	count=$((count +1))
 	echo   -e "$count\t$querryac\t$subjectac\t$identity\t$alignmentlength\t$mismatches\t$gapopens\t$q_start\t$q_end\t$s_start\t$s_end\t$evalue\t$bitscore" >> 20mismatches.details
	fi #mismatches
fi #for get rid of blanck spaces
done < blastoutput2.out 

