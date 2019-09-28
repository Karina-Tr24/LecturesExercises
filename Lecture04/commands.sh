count=0
IFS=$'\t'
while read name email city birthday_day birthday_month birthday_year country;
do
	if test -z $birthday_month
	then 
	echo -e "X\tNO data"
	else 
	if test $birthday_month = "birthday_month"
	then 
	echo -e "X\tHeader line"
	else
	count=$((count+1)); 
	echo -e "$count \t $birthday_month"; 
fi # $name
fi # header
done<example_people_data.tsv


