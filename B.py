import re


def greed(dig):
    counter = 0
    number = dig

    while number != 0:

        if number % 2 == 0:
            number /= 2
            counter += 1
        elif number == 1:
            number -= 1
            counter += 1
        elif number % 2 == 1:
            less = bin(int(number-1))[2:]
            more = bin(int(number+1))[2:]

            power1 = len(re.findall(r'1', str(less)))
            power2 = len(re.findall(r'1', str(more)))

            if power1 > power2:
                number += 1
                counter += 1
            elif power1 < power2:
                number -= 1
                counter += 1

            else:
                index = len(more)//2
                for i in range(index, len(more)-1):
                    if int(less[i]) < int(more[i]):
                        number += 1
                        counter += 1
                        break
                    elif int(less[i]) > int(more[i]) or len(more) > len(less):
                        number -= 1
                        counter += 1
                        break

    return counter

if __name__ == "__main__":

    while True:
        try:
            num = input()
            if num != '':
                result = greed(int(num))
                print(result)
        except EOFError:
            break










    # while True:
    #     number = input()
    #     result = greed(int(number))
    #     print('res', result)
