import math
import sys
import re


class Bloom:

    def __init__(self, n, p):
        self.__m = round((-n * math.log2(p) / math.log(2)))
        self.__k = round(-math.log2(p))
        self.__bits = bytearray(math.ceil(self.__m/8))
        self.__primes = set()
        self.__primes.add(2)

    def get_m(self):
        return self.__m

    def get_k(self):
        return self.__k

    def __get_prime(self, last_prime):
        prime = last_prime + 1
        while True:
            if prime in self.__primes:
                return prime
            if all(prime % i != 0 for i in self.__primes):
                self.__primes.add(prime)
                return prime
            prime += 1

    def insert(self, number):
        mersenne = 2147483647
        prime = 2
        for i in range(0, self.__k):
            if i != 0:
                prime = self.__get_prime(prime)
            index = (((i + 1) * number + prime) % mersenne) % self.__m
            self.__bits[index//8] |= 2**(index % 8)

    def search(self, number):
        mersenne = 2147483647
        prime = 2
        for i in range(0, self.__k):
            if i != 0:
                prime = self.__get_prime(prime)
            index = (((i + 1) * number + prime) % mersenne) % self.__m
            value = self.__bits[index // 8]
            value = value & (2 ** (index % 8))
            if not value > 0:
                return 0
        return 1

    def print(self, out=sys.stdout):
        for i in range(0, self.__m):
            value = self.__bits[i//8]
            value = value & (2**(i % 8))
            out.write(f'{(value > 0) * 1}')
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

    bloom = None
    flag = False
    while True:
        try:
            command = input()
            if command == '':
                continue
            elif not flag:
                if re.fullmatch(r'(set) (\d+) (1|0|(0\.\d+))', command):
                    params = command.split(' ')
                    if int(params[1]) > 0:
                        prob = float(params[2])
                        if (0 <= prob) and (prob <= 1):
                            if round(-math.log2(prob)) > 0:
                                flag = True
                                bloom = Bloom(int(params[1]), prob)
                                print(bloom.get_m(), bloom.get_k())
                                continue
                print('error')
                continue
            if flag:
                process(bloom, command)
            else:
                print('error')
        except EOFError:
            break
