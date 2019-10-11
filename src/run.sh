current_time=$(date "+%Y.%m.%d-%H:%M:%S")
file_name=drawing-$current_time.draw
file_name=drawing.draw
python3 -O -u ./simulator.py run --number-of-peers 4 --number-of-monitors 1 --number-of-rounds 100 --set-of-rules dbs --drawing-log ./drawing-logs/$file_name $1
