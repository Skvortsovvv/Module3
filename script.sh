for i in {1..8};
do 
echo "`<./testsA/Input/${i}.txt`" | python3 A.py > out.txt
RESULT=$(diff out.txt testsA/Output/${i}.txt)
echo "./testsA/Input/${i}.txt"
echo "./testsA/Output/${i}.txt"
if [ -z "$RESULT" ]; then
    echo "TEST ${i}: OK"
else
    echo "TEST ${i}: FAILED"
fi;
done