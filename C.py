import math
import sys
import re


class Bloom:

    def __init__(self, n, p, out=sys.stdout):
        self.__m = round((-n * math.log2(p) / math.log(2)))
        self.__k = round(-math.log2(p))
        self.__bits = bytearray([False for _ in range(0, self.__m)])
        out.write(f'{self.__m} {self.__k}\n')

    @staticmethod
    def __get_prime(last_prime):
        prime = last_prime + 1
        while True:
            if all(prime % i != 0 for i in range(2, int(math.sqrt(prime)) + 1)):
                return prime
            prime += 1

    def insert(self, number):
        mersenne = 2147483647
        prime = 1
        for i in range(0, self.__k):
            prime = self.__get_prime(prime)
            index = (((i + 1) * number + prime) % mersenne) % self.__m
            self.__bits[index] = True

    def search(self, number):
        mersenne = 2147483647
        prime = 1
        for i in range(0, self.__k):
            prime = self.__get_prime(prime)
            index = (((i + 1) * number + prime) % mersenne) % self.__m
            if self.__bits[index] == 0:
                return 0
        return 1

    def print(self, out=sys.stdout):
        for i in range(0, len(self.__bits)):
            out.write(f'{self.__bits[i] * 1}')
        out.write('\n')


def process(bl: Bloom, cmd):
    if re.fullmatch(r'add \d+', cmd):
        elem = cmd[4:]
        bl.insert(int(elem))
    elif re.fullmatch(r'search \d+', cmd):
        elem = cmd[7:]
        result = bl.search(int(elem))
        print(result)
    elif re.fullmatch(r'print', cmd):
        bl.print()
    else:
        print('error')


if __name__ == "__main__":

    # bl = Bloom(2, 0.250)
    # bl.insert(7)
    # bl.insert(5)
    # bl.insert(14)
    # bl.print()
    # print(bl.search(7))
    # print(bl.search(10))
    # print(bl.search(15))
    # print(bl.search(14))
    # print(bl.search(5))
    # print(bl.search(13))

    bloom = None
    flag = False
    while True:
        try:
            command = input()
            if command == '':
                continue
            elif re.fullmatch(r'(set) (\d+) (1|0|(0\.\d+))', command):
                if not flag:
                    params = command.split(' ')
                    p = float(params[2])
                    if (0 <= p) and (p <= 1):
                        flag = True
                        bloom = Bloom(int(params[1]), p)
                        continue
                else:
                    print('error')
                    continue
            if flag:
                process(bloom, command)
            else:
                print('error')
        except EOFError:
            break
