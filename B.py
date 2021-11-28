import re


def greed(dig):
    flag = False
    counter = 0
    number = dig
    steps = []

    while number != 0:

        if number % 2 == 0:
            number /= 2
            counter += 1
            steps.append('dbl')
        elif number == 1:
            number -= 1
            counter += 1
            steps.append('inc')
        elif number % 2 == 1:
            less = re.findall(r'[\d]+', bin(int(number-1)))
            more = re.findall(r'[\d]+', bin(int(number+1)))

            if not flag:
                flag = True
                less = less.pop(1)
                more = more.pop(1)
            power1 = len(re.findall(r'1', str(less)))
            power2 = len(re.findall(r'1', str(more)))

            if power1 > power2:
                number += 1
                counter += 1
                steps.append('dec')
            elif power1 < power2:
                number -= 1
                counter += 1
                steps.append('inc')

            else:
                index = len(more)//2
                for i in range(index, len(more)):
                    if int(less[i]) > int(more[i]):
                        number += 1
                        counter += 1
                        steps.append('dec')
                        break
                    elif int(less[i]) < int(more[i]) or len(more) > len(less):
                        number -= 1
                        counter += 1
                        steps.append('inc')
                        break

    _number = dig
    _steps = []
    flag = False
    _counter = 0

    while _number != 0:

        if _number % 2 == 0:
            _number /= 2
            _counter += 1
            _steps.append('dbl')
        elif _number == 1:
            _number -= 1
            _counter += 1
            _steps.append('inc')
        elif _number % 2 == 1:
            less = re.findall(r'[\d]+', bin(int(_number-1)))
            more = re.findall(r'[\d]+', bin(int(_number+1)))
            # if not flag:
            #     flag = True
            #     less = less.pop(1)
            #     more = more.pop(1)
            power1 = len(re.findall(r'1', str(less)))
            power2 = len(re.findall(r'1', str(more)))

            if power1 > power2:
                _number += 1
                _counter += 1
                flag = True
                _steps.append('dec')
            elif power1 < power2:
                _number -= 1
                _counter += 1
                _steps.append('inc')
            else:
                _number -= 1
                _counter += 1
                _steps.append('inc')
                flag = True

    _steps.reverse()
    steps.reverse()
    print(steps)
    print(_steps)

if __name__ == "__main__":

    while True:
        try:
            num = input()
            if num != '':
                greed(int(num))
                # result.reverse()
                # for i in result:
                #     print(i)
        except EOFError:
            break










    # while True:
    #     number = input()
    #     result = greed(int(number))
    #     print('res', result)
