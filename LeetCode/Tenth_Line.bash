# Read from the file file.txt and output the tenth line to stdout.
LINE=1
while read -r CURRENT_LINE
do
if [ "$LINE" -eq "10" ]
then
echo $CURRENT_LINE
fi
((LINE++))
done < "./file.txt"
