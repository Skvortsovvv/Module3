import re


def greedy(dig):
    operations = []
    counter = 0
    number = dig

    while number != 0:

        if number % 2 == 0:
            number /= 2
            counter += 1
            operations.append('dbl')
        elif number == 1:
            number -= 1
            counter += 1
            operations.append('inc')
        elif number % 2 == 1:
            less = bin(int(number-1))[2:]
            more = bin(int(number+1))[2:]

            power1 = len(re.findall(r'1', str(less)))
            power2 = len(re.findall(r'1', str(more)))

            if power1 > power2:
                number += 1
                counter += 1
                operations.append('dec')
            elif power1 < power2:
                number -= 1
                counter += 1
                operations.append('inc')

            else:
                index = len(more)//2
                for i in range(index, len(more)-1):
                    if int(less[i]) < int(more[i]):
                        number += 1
                        counter += 1
                        operations.append('dec')
                        break
                    elif int(less[i]) > int(more[i]) or len(more) > len(less):
                        number -= 1
                        counter += 1
                        operations.append('inc')
                        break
    operations.reverse()
    return operations


if __name__ == "__main__":

    while True:
        try:
            num = input()
            if num != '':
                result = greedy(int(num))
                for op in result:
                    print(op)
        except EOFError:
            break
