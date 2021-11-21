import re
from itertools import combinations
class Bag:

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.items = []
        self.items.append([0])

    def set_cap(self, cap):
        self.capacity = cap

    def add_item(self, weight, price):
        self.items.append([weight, price])

    def calculate(self):
        previous = {}
        current = {}
        weights = []
        for w in self.items:
            weights.append(w[0])
        weights.sort()
        previous[0] = [0, []]
        current[0] = [0, []]
        for i in range(2, len(self.items)+1):
            comb = combinations(weights, i)
            for c in comb:
                comb_weight = 0
                for ci in c:
                    comb_weight += ci
                if comb_weight <= self.capacity:
                    if comb_weight not in previous:
                        previous[comb_weight] = [0, []]
                        current[comb_weight] = [0, []]
        print('done')
        
        # previous = [[0, []] for _ in range(0, self.capacity+1)]
        # current = [[0, []] for _ in range(0, self.capacity+1)]
        # # массив вида current[i] = [value, [indexes]], где value - ценность всего рюкзака
        # # [indexes] - индексы предметов, находящихся в рюкзаке при данной ценности
        # # i - вес рюкзака
        # for i in range(1, len(self.items)):  # индексы предметов
        #     for j in range(1, self.capacity+1):  # индексы весов рюкзака
        #         if self.items[i][0] > j:
        #             current[j] = previous[j]
        #         else:
        #             value = max(previous[j][0], self.items[i][1] + previous[j-self.items[i][0]][0])
        #             if previous[j][0] == value:
        #                 current[j] = previous[j]
        #             else:
        #                 current[j][0] = value
        #                 current[j][1] = [e for e in previous[j-self.items[i][0]][1]]
        #                 current[j][1].append(i)
        #     previous = current
        #     if i != len(self.items)-1:
        #         current = [[0, []] for _ in range(0, self.capacity+1)]
        #
        # result_weight = 0
        # for index in current[self.capacity][1]:
        #     result_weight += self.items[index][0]
        # return [result_weight, current[self.capacity][0], current[self.capacity][1]]


def process(b: Bag, item):
    if re.fullmatch(r'[\d+]+ [\d+]+', item):
        arguments = item.split(' ')
        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        if arguments not in b.items:
            b.add_item(arguments[0], arguments[1])
            return
    print('error')
    return


if __name__ == "__main__":

    bag = Bag(5)
    bag.add_item(3, 55)
    bag.add_item(2, 80)
    bag.add_item(4, 60)
    bag.calculate()
    """"
    while True:
        try:
            size = input()
            if size.isnumeric():
                bag.set_cap(int(size))
                break
            else:
                print('error')
        except EOFError:
            break

    while True:
        try:
            text = input()
            if text != '':
                process(bag, text)
        except EOFError:
            break

    result = bag.calculate()
    print(result[0], result[1])
    for elem_index in result[2]:
        print(elem_index)
        
    """
