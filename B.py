import re


def count_power(number):
    power = 0
    while number != 0:
        power += number % 2
        number = number // 2
    return power

def bin_leght(number):
    lenght = 0
    while number != 0:
        lenght += 1
        number //= 2
    return lenght


def greedy(dig):
    operations = []
    counter = 0
    number = dig

    while number != 0:

        if number % 2 == 0:
            number //= 2
            counter += 1
            operations.append('dbl')
        elif number == 1:
            number -= 1
            counter += 1
            operations.append('inc')
        elif number % 2 == 1:
            less = number-1
            more = number+1

            power1 = count_power(less)
            power2 = count_power(more)

            if power1 > power2:
                number += 1
                counter += 1
                operations.append('dec')
            elif power1 < power2:
                number -= 1
                counter += 1
                operations.append('inc')

            else:
                index = bin_leght(more)//2

                for i in range(index - 1, -1, -1):
                    if ((less >> i) % 2) < ((more >> i) % 2):
                        number += 1
                        counter += 1
                        operations.append('dec')
                        break
                    elif ((less >> i) % 2) > ((more >> i) % 2) or (bin_leght(more) > bin_leght(less)):
                        number -= 1
                        counter += 1
                        operations.append('inc')
                        break
    operations.reverse()
    return operations


if __name__ == "__main__":

    #res = greedy(11)

    while True:
        try:
            num = input()
            if num != '':
                result = greedy(int(num))
                for op in result:
                    print(op)
        except EOFError:
            break
