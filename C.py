import math
import sys
import re


class Bitarray:

    def __init__(self, m):
        self.size = m
        self.array = bytearray(math.ceil(self.size/8))

    def put(self, index):
        self.array[index // 8] |= 2 ** (index % 8)

    def get(self, index):
        value = self.array[index // 8]
        value = value & (2 ** (index % 8))
        return value


class Bloom:

    def __init__(self, n, p):
        self.__m = round((-n * math.log2(p) / math.log(2)))
        self.__k = round(-math.log2(p))
        self.__bits = Bitarray(self.__m)
        self.__primes = self.__k*[0]
        self.__primes[0] = 2
        prime = 2
        for i in range(1, self.__k):
            self.__get_prime(prime, i)

    def get_m(self):
        return self.__m

    def get_k(self):
        return self.__k

    def __get_prime(self, last_prime, j):
        prime = last_prime + 1
        while True:
            for i in self.__primes:
                if i == 0:
                    self.__primes[j] = prime
                    return
                else:
                    if prime % i != 0:
                        continue
                    else:
                        prime += 1
                        break

    def insert(self, number):
        for i in range(0, self.__k):
            index = (((i + 1) * number + self.__primes[i]) % 2147483647) % self.__m
            self.__bits.put(index)

    def search(self, number):
        for i in range(0, self.__k):
            index = (((i + 1) * number + self.__primes[i]) % 2147483647) % self.__m
            value = self.__bits.get(index)
            if not value > 0:
                return 0
        return 1

    def print(self, out=sys.stdout):
        for i in range(0, self.__m):
            value = self.__bits.get(i)
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
        except EOFError:
            break
