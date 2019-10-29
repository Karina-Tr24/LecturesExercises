#!/bin/bash
rm -f *.details
count=0
IFS=$'\t'
while read name email city birthday_day birthday_month birthday_year country;
do
	if test -z $birthday_month || test $birthday_month = "birthday_month"
	then 
	echo -e "There is no file"	
	else
	count=$((count+1)); 
	echo -e  "$count\t$name\t$birthday_day\t$birthday_month\t$birthday_year" >> $birthday_month.details;
	 
fi #names and header
done<example_people_data.tsv | head -10


