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

    def make_combines(self, row, weights):
        for i in range(2, len(self.items)+1):
            comb = combinations(weights, i)
            for c in comb:
                comb_weight = 0
                for ci in c:
                    comb_weight += ci
                if comb_weight <= self.capacity:
                    if comb_weight not in row:
                        row[comb_weight] = [0, []]
        return row

    def make_weights(self):
        weights = []
        for w in self.items:
            weights.append(w[0])
        return weights

    def calculate(self):
        previous = {}
        current = {}

        weights = self.make_weights()

        weights.sort()

        previous[0] = [0, []]
        current[0] = [0, []]
        previous = self.make_combines(previous, weights)
        current = self.make_combines(current, weights)

        # for i in range(2, len(self.items)+1):
        #     comb = combinations(weights, i)
        #     for c in comb:
        #         comb_weight = 0
        #         for ci in c:
        #             comb_weight += ci
        #         if comb_weight <= self.capacity:
        #             if comb_weight not in previous:
        #                 previous[comb_weight] = [0, []]
        #                 current[comb_weight] = [0, []]

        if self.capacity not in previous:
            previous[self.capacity] = [0, []]
            current[self.capacity] = [0, []]

        for i in range(1, len(self.items)):
            for key in current.keys():
                if self.items[i][0] > key:
                    current[key] = previous[key]
                else:
                    v = self.items[i][1]

                    if key - self.items[i][0] in previous.keys():
                        value = max(previous[key][0], v + previous[key - self.items[i][0]][0])

                        if value == previous[key][0]:
                            current[key] = previous[key]
                        else:
                            current[key][0] = value
                            current[key][1] = [index for index in previous[key - self.items[i][0]][1]]
                            current[key][1].append(i)
                    else:
                        value = max(previous[key][0], v)

                        if value == previous[key][0]:
                            current[key] = previous[key]
                        else:
                            current[key][0] = value
                            current[key][1].append(i)

            previous = current
            if i != len(self.items)-1:
                current = {}
                for k in previous.keys():
                    current[k] = [0, []]

        result_weight = 0
        for i in current[self.capacity][1]:
            result_weight += self.items[i][0]
        return [result_weight, current[self.capacity][0], current[self.capacity][1]]

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
        b.add_item(arguments[0], arguments[1])
        return
    print('error')
    return


if __name__ == "__main__":

    # bag = Bag(750)
    #
    # bag.add_item(70, 135)
    # bag.add_item(73, 139)
    # bag.add_item(77, 149)
    #
    # bag.add_item(80, 150)
    # bag.add_item(82, 156)
    # bag.add_item(87, 163)
    #
    # bag.add_item(90, 173)
    # bag.add_item(94, 184)
    # bag.add_item(98, 192)
    #
    # bag.add_item(106, 201)
    # bag.add_item(110, 210)
    # bag.add_item(113, 214)
    #
    # bag.add_item(115, 221)
    # bag.add_item(118, 229)
    # bag.add_item(120, 240)


    bag = Bag()

    while True:
        try:
            size = input()
            if size.isnumeric():
                bag.set_cap(int(size))
                break
            elif size != '':
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
