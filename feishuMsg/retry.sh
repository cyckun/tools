

for i in { 1, 2 }
do
    echo $i
    python3 feishu.py  hsyq_$i
    echo '1 round'
done