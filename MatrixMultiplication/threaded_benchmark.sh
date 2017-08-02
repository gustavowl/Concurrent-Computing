#!/bin/bash

#constants
MAX_ITERATIONS=10
FILE_EXTENSION=".txt"
MATRIX_DIM=(4x4 8x8 16x16 32x32 64x64 128x128 256x256 512x512)

#used for initial benchmarking. Depending of the results obtained
#it may be necessary to test with more threads
MAX_NUMBER_THREADS=(4 8 16 32 32 32 64 128)
LANGUAGES=(cpp "python" go)

count_script=0
max_script=0
for h in ${MAX_NUMBER_THREADS[@]};
do
	max_script=$[$max_script + $h * $MAX_ITERATIONS]
done
max_script=$[$max_script * ${#LANGUAGES[@]}]
echo $max_script
for i in ${LANGUAGES[@]};
do
	bench_dir=$i"/benchmark/"
	cmd="nuthing"
	if [ $i = "cpp" ]; then
		cmd="./"$i"/tmm"
	elif [ $i = "python" ]; then
		cmd="python "$i"/threaded_matrix_mult.py"
	else #then go
		cmd="go run "$i"/threaded_matrix_mult.go"
	fi
	index=0

	for j in "${MATRIX_DIM[@]}";
	do
		mkdir -p $bench_dir"threaded/shell/" #guarantees that path exists
		mkdir -p $bench_dir"threaded/internal/" #guarantees that path exists
		FILE_SHELL=$bench_dir"threaded/shell/"$j$FILE_EXTENSION
		FILE_STD_OUTPUT=$bench_dir"threaded/internal/"$j$FILE_EXTENSION
		rm -f $FILE_SHELL #so it doesnt print unnecessary info
		rm -f $FILE_STD_OUTPUT #so it doesnt print unnecessary info
		count_iterations=0
		#runs the program the desired number of times
		echo -e '\n\n'================================================================
		echo -e ====================BEGIN $i $j====================
		echo ================================================================
		for th_num in `seq 1 $[MAX_NUMBER_THREADS[$index]]`;
		do
			ARGUMENT3="output.txt"
			echo -e "\n-----------------"$i $j": "$th_num" Thread(s)-----------------"
			echo -e "\n-----------------"$th_num" Thread(s)-----------------" >> $FILE_STD_OUTPUT

			for k in `seq 1 $MAX_ITERATIONS`;
			do
				#choose the matrices randomly since the order for square matrices does not matter
				if [ $((RANDOM % 2)) -eq "0" ]; then
					ARGUMENT1="matrices/a"$j$FILE_EXTENSION
					ARGUMENT2="matrices/b"$j$FILE_EXTENSION
				else
					ARGUMENT1="matrices/b"$j$FILE_EXTENSION
					ARGUMENT2="matrices/a"$j$FILE_EXTENSION
				fi

				start=$( date -I'ns' )
				$cmd $ARGUMENT1 $ARGUMENT2 $ARGUMENT3 $th_num >> $FILE_STD_OUTPUT
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
				echo -e $i $j $[$count_iterations*100/($MAX_ITERATIONS*$[MAX_NUMBER_THREADS[$index]])]% '\t'"Script progress: "$count_script/$max_script '('$perc_script%')'
			done
		done

		index=$[$index + 1]
	done
done
