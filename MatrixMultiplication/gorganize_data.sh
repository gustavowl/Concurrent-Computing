#!/bin/bash

if [ $# = 2 ]; then
	first=true
	echo -ne '(' > $2
	while read -r line; do
		if [ `expr match "$line" 'Time to multiply matrices: '` -gt 0 ]; then
			seconds=${line:27}
			minutes=0
			submultiple=0
			#echo $[$seconds * 10]
			index=-1

			if [ `expr index "$seconds" 'n'` -gt 0 ]; then
				#nanosecond
				submultiple=-9
				index=$[`expr index "$seconds" 'n'`]
			elif [ `expr index "$seconds" 'u'` -gt 0 ]; then
				#microsecond
				submultiple=-6
				index=$[`expr index "$seconds" 'u'`]
			elif [ $[`expr index "$seconds" 's'` - `expr index "$seconds" 'm'`] -eq 1 ]; then
				#millisecond
				submultiple=-3
				index=$[`expr index "$seconds" 'm'`]
			elif [ `expr index "$seconds" 'm'` -gt 0 ]; then
				#minute
				submultiple=0
				index=$[`expr index "$seconds" 'm'`]
				minutes=${seconds:0:$[$index - 1]}
				seconds=${seconds:index}
				index=$[`expr index "$seconds" 's'`]
			else
				#second
				submultiple=0
				index=$[`expr index "$seconds" 's'`]
			fi

			seconds=${seconds:0:$[$index - 1]}
			echo $seconds
			if [ $first = false ]; then
				echo -ne ', '$(echo "$minutes * 60 + $seconds * 10 ^ $submultiple" | bc -l) >> $2
			else
				first=false
				echo -ne $(echo "$minutes * 60 + $seconds * 10 ^ $submultiple" | bc -l) >> $2
			fi
		fi

	done < $1
	echo ')' >> $2
else
	echo 'Wrong number of arguments. Expecting 2 arguments:'
	echo -e '1 - Benchmark file\n2 - Output file'
fi