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

    # def make_combines(self, row, weights):
    #     for i in range(2, len(self.items)+1):
    #         comb = combinations(weights, i)
    #         for c in comb:
    #             comb_weight = 0
    #             for ci in c:
    #                 comb_weight += ci
    #             if comb_weight <= self.capacity:
    #                 if comb_weight not in row:
    #                     row[comb_weight] = [0, []]
    #     return row

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
            if bag_weight - item_weight >= self.items[0][0][0]:
                self.recursive(bag_weight-item_weight, item_weight, index, weights)
            else:
                weights[bag_weight][index] = weights[bag_weight][index-1]
            if limit != bag_weight:
                self.recursive(bag_weight, item_weight, index, weights)
        else:
            if bag_weight not in weights.keys():
                weights[bag_weight] = {}
            if index == 1:
                weights[bag_weight][index] = [self.items[index][0][1], [self.items[index][1][0]]]
            elif index == 0:
                weights[bag_weight][index] = [0, []]
            else:
                sum = self.items[index][0][1] + weights[bag_weight-item_weight][index][0]
                prev_v = weights[bag_weight][index-1][0]
                if sum > prev_v:
                    weights[bag_weight][index] = [sum, []]
                    weights[bag_weight][index][1] = \
                        [i for i in weights[bag_weight-item_weight][index][1]]
                    if self.items[index][1][0] not in weights[bag_weight][index][1]:
                        weights[bag_weight][index][1].append(self.items[index][1][0])
                else:
                    weights[bag_weight][index] = weights[bag_weight][self.items[index-1][0][0]]
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

        for i in range(0, len(self.items)):
            item_weight = self.items[i][0][0]
            self.recursive(self.capacity, item_weight, i, weights, self.capacity)

        result = weights[self.capacity]

        return result

        # if self.capacity not in previous:
        #     previous[self.capacity] = [0, []]
        #     current[self.capacity] = [0, []]
        #
        # for i in range(1, len(self.items)):
        #     for key in current.keys():
        #         if self.items[i][0] > key:
        #             current[key] = previous[key]
        #         else:
        #             v = self.items[i][1]
        #
        #             if key - self.items[i][0] in previous.keys():
        #                 value = max(previous[key][0], v + previous[key - self.items[i][0]][0])
        #
        #                 if value == previous[key][0]:
        #                     current[key] = previous[key]
        #                 else:
        #                     current[key][0] = value
        #                     current[key][1] = [index for index in previous[key - self.items[i][0]][1]]
        #                     current[key][1].append(i)
        #             else:
        #                 value = max(previous[key][0], v)
        #
        #                 if value == previous[key][0]:
        #                     current[key] = previous[key]
        #                 else:
        #                     current[key][0] = value
        #                     current[key][1].append(i)
        #
        #     previous = current
        #     if i != len(self.items)-1:
        #         current = {}
        #         for k in previous.keys():
        #             current[k] = [0, []]

        # result_weight = 0
        # for i in current[self.capacity][1]:
        #     result_weight += self.items[i][0]
        # return [result_weight, current[self.capacity][0], current[self.capacity][1]]

        #
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
        #

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

    bag = Bag(5)

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
