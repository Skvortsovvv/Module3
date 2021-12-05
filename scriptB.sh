RED='\033[0;31m'
GRN='\033[0;32m'
NC='\033[0m'
for i in {1..102};
do 
echo "`<./testsB/Input/${i}.txt`" | python3 B.py > out.txt
RESULT=$(diff out.txt testsB/Output/${i}.txt)
#echo "./testsB/Input/${i}.txt"
#echo "./testsB/Output/${i}.txt"
#echo "`<./testsB/Output/${i}.txt`"
#echo "`<./out.txt`"
if [ -z "$RESULT" ]; then
    echo -e "${GRN} [PASSED] ${NC} TEST ${i}"
else
    echo -e "${RED} [FAILED] ${NC} TEST ${i}"
fi;
done