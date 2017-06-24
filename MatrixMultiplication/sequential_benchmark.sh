#!/bin/bash

#constants
MAX_ITERATIONS=100
FILE_EXTENSION=".txt"
MATRIX_DIM=(4x4 8x8 16x16 32x32 64x64 128x128 256x256 512x512 1024x1024 2048x2048)
LANGUAGES=(cpp "python")

count_script=0
max_script=$[${#LANGUAGES[@]} * $MAX_ITERATIONS * ${#MATRIX_DIM[@]}]

for i in ${LANGUAGES[@]};
do
	bench_dir=$i"/benchmark/"
	cmd="nuthing"
	if [ $i = "cpp" ]; then
		cmd="./"$i"/mm"
	else #then python
		cmd="python "$i"/matrix_mult.py"
	fi

	for j in "${MATRIX_DIM[@]}";
	do
		FILE_SHELL=$bench_dir"shell/sequential/"$j$FILE_EXTENSION
		FILE_STD_OUTPUT=$bench_dir"internal/sequential/"$j$FILE_EXTENSION
		rm -f $FILE_SHELL #so it doesnt print unnecessary info
		rm -f $FILE_STD_OUTPUT #so it doesnt print unnecessary info
		count_iterations=0
		#runs the program the desired number of times
		echo -e '\n\n'--------------------BEGIN $i $j--------------------
		for k in `seq 1 $MAX_ITERATIONS`;
		do

			ARGUMENT3="output.txt"
			#choose the matrices randomly since the order for square matrices does not matter
			if [ $((RANDOM % 2)) -eq "0" ]; then
				ARGUMENT1="matrices/a"$j$FILE_EXTENSION
				ARGUMENT2="matrices/b"$j$FILE_EXTENSION
			else
				ARGUMENT1="matrices/b"$j$FILE_EXTENSION
				ARGUMENT2="matrices/a"$j$FILE_EXTENSION
			fi

			start=$( date -I'ns' )
			$cmd $ARGUMENT1 $ARGUMENT2 $ARGUMENT3 >> $FILE_STD_OUTPUT
			end=$( date -I'ns' )
			echo "" >> $FILE_STD_OUTPUT
			echo "-------------------------ITERATION #"$k"-------------------------" >> $FILE_SHELL
			echo "Start time: "$start >> $FILE_SHELL
			echo "Finished time: "$end >> $FILE_SHELL
			echo "Duration: "$(($(($(date -d $end +%s%N) - $(date -d $start +%s%N)))/1000)) "microsecond(s)" >> $FILE_SHELL
			echo"" >> $FILE_SHELL

			count_script=$[$count_script + 1]
			count_iterations=$[$count_iterations + 1]
			perc_script=$(bc -l <<< 'scale=2; '$count_script*100/$max_script)
			#perc_iterations=$(bc -l <<< 'scale=1; '$count_iterations*100/$MAX_ITERATIONS)
			echo -e $i $j $[$count_iterations*100/$MAX_ITERATIONS]% '\t'"Script progress: "$count_script/$max_script '('$perc_script%')'
		done
	done
done