import re
from itertools import combinations

class Bag:

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.items = []
        self.items.append([[0]])

    def set_cap(self, cap):
        self.capacity = cap

    def add_item(self, weight, price):
        self.items.append([[weight, price]])

    def make_weights(self):
        weights = {}
        for i in range(0, len(self.items)):
            weights[self.items[i][0][0]] = {}
            # weights - словарь
            # ключ - вес рюкзака
            # значение - словарь
            #   ключ - индекс предмета в отсортированном массиве предметов
            #   значение - [ценность рюкзака, [оригинальные индексы предметов в рюкзаке]]
        return weights

    def set_items_indexes(self):
        for i in range(0, len(self.items)):
            self.items[i].append([i])
            # присваиваем каждому предмету его изначальный индекс по порядку добавления
            # index - индекс в отсортированном массиве, index_origin - индекс в
            # исходном массиве

    def recursive(self, bag_weight, item_weight, index, weights, limit=None):
        if bag_weight-item_weight not in weights.keys():
            if bag_weight not in weights.keys():
                weights[bag_weight] = {}
                weights[bag_weight][index] = [0, []]
            if item_weight == 0:
                weights[bag_weight][index] = [0, []]
            elif bag_weight - item_weight >= self.items[1][0][0]:
                self.recursive(bag_weight-item_weight, item_weight, index, weights)
                self.recursive(bag_weight, item_weight, index, weights)
            elif bag_weight == 0:
                weights[bag_weight][index] = [0, []]
            else:
                _prev_v = weights[bag_weight][index-1][0]
                _sum = self.items[index][0][1]
                if _sum > _prev_v:
                    weights[bag_weight][index] = [_sum, []]
                    # weights[bag_weight][index][1].append(self.items[index][1][0])
                    weights[bag_weight][index][1].append(index)
                else:
                    weights[bag_weight][index] = weights[bag_weight][index-1]

            if limit != bag_weight:
                self.recursive(bag_weight, item_weight, index, weights)
        else:
            if bag_weight not in weights.keys():
                weights[bag_weight] = {}
                weights[bag_weight][index] = [0, []]
            if index == 1:
                # weights[bag_weight][index] = [self.items[index][0][1], [self.items[index][1][0]]]
                weights[bag_weight][index] = [self.items[index][0][1], [index]]
            elif index == 0:
                weights[bag_weight][index] = [0, []]
            else:
                sum = self.items[index][0][1] + weights[bag_weight-item_weight][index][0]
                if index-1 not in weights[bag_weight]:
                    self.recursive(bag_weight, self.items[index-1][0][0], index-1, weights)
                prev_v = weights[bag_weight][index-1][0]
                if sum > prev_v:
                    weights[bag_weight][index] = [sum, []]
                    weights[bag_weight][index][1] = \
                        [i for i in weights[bag_weight-item_weight][index][1]]
                    # if self.items[index][1][0] not in weights[bag_weight][index][1]:
                    if index not in weights[bag_weight][index][1]:
                        # weights[bag_weight][index][1].append(self.items[index][1][0])
                        weights[bag_weight][index][1].append(index)
                else:
                    weights[bag_weight][index] = weights[bag_weight][index-1]
        return

    def calculate(self):

        self.set_items_indexes()
        # устанавливаем индексы каждому предмету в соотв. порядка его добавления

        self.items.sort(key=lambda item: item[0][0])
        # сортируем предметы по весу

        weights = self.make_weights()
        # создаем словарь из весов всех предметов, в который будет потом добавлять новые веса рюкзака

        for i in range(0, len(self.items)):
            item_weight = self.items[i][0][0]  # вес предмета
            for bag_weight in weights.keys():
                self.recursive(bag_weight, item_weight, i, weights, bag_weight)

        print()

        for i in range(0, len(self.items)):
            item_weight = self.items[i][0][0]
            self.recursive(self.capacity, item_weight, i, weights, self.capacity)

        result_weight = 0
        result_value = weights[self.capacity][len(self.items)-1][0]
        indexes = []

        for i in weights[self.capacity][len(self.items)-1][1]:
            result_weight += self.items[i][0][0]
            indexes.append(self.items[i][1][0])
        indexes.sort()

        return [result_weight, result_value, indexes]



def process(b: Bag, item):
    if re.fullmatch(r'[\d+]+ [\d+]+', item):
        arguments = item.split(' ')
        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        b.add_item(arguments[0], arguments[1])
        return
    print('error')
    return


def main():

    bag = Bag(8)

    bag.add_item(3, 55)
    bag.add_item(2, 80)
    bag.add_item(4, 60)

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

    result = bag.calculate()
    print(result)

if __name__ == "__main__":

    main()

    # bag = Bag()
    #
    # while True:
    #     try:
    #         size = input()
    #         if size.isnumeric():
    #             bag.set_cap(int(size))
    #             break
    #         elif size != '':
    #             print('error')
    #     except EOFError:
    #         break
    #
    # while True:
    #     try:
    #         text = input()
    #         if text != '':
    #             process(bag, text)
    #     except EOFError:
    #         break

    # result = bag.calculate()
    # print(result[0], result[1])
    # for elem_index in result[2]:
    #     print(elem_index)
