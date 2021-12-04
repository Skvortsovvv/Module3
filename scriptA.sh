RED='\033[0;31m'
GRN='\033[0;32m'
NC='\033[0m'
for i in {1..16};
do 
echo "`<./testsA/Input/${i}.txt`" | python3 A_new2.py > out.txt
RESULT=$(diff out.txt testsA/Output/${i}.txt)
#echo "./testsA/Input/${i}.txt"
#echo "./testsA/Output/${i}.txt"
#echo "`<./testsA/Output/${i}.txt`"
echo "`<./out.txt`"
if [ -z "$RESULT" ]; then
    echo -e ${GRN}"[PASSED]"${NC} "TEST ${i}: ${GRN}OK${NC}"
else
    echo -e ${GRN}"[FAILED]"${NC} "TEST ${i}: ${RED}FAILED${NC}"
fi;
done