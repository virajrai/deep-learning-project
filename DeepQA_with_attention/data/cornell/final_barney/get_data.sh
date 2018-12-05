#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "usage: ./get_data.sh num_of_times_characters_conversations_to_append"
    echo "Please enter the number of times you want to append the character conversations to the cornell dataset as your argument"
    exit 1
fi

rm -rf pages
mkdir pages
cd pages

echo "Generating Dataset..."
cd ..
rm -rf output
mkdir output
python3 clean_lines.py
python3 genLines.py
cp ../COPY_movie_conversations.txt ../COPY_movie_lines.txt .
mv COPY_movie_conversations.txt movie_conversations.txt
mv COPY_movie_lines.txt movie_lines.tx
for i in `seq 1 $1`;
do
	cat character_conversations.txt >> movie_conversations.txt
done
cat character_lines.txt >> movie_lines.txt
cp movie_conversations.txt movie_lines.txt ..
echo "Done."
