import re
"""""
    Последовательно считываем со входного потока параметры n предметов. Добавляем в рюкзак.
    Рюкзак: Список:
                Элемент: [[Вес предмета, Цена предмета], [Индекс по порядку добавления в рюкзак]]
    В методе set_items_indexes как устанавливаем "оригинальные индексы"
    Сортируем предметы рюкзака по весу
    Методом make_weights формиркем словарь weights возможных весов словаря. Сначала состоит из весов самих
    предметов по возрастанию.
    weights: Словарь: Допустимые веса рюкзака
                Словарь: Индекс (0, 1,  ... , n) - означает сколькько предметов может быть помещено в рюкзак
                    Значение: Список
                        Список: [Ценность рюкзака при данных предметах в нем, [Индексы предметов в рюкзаке]]
    В первом цикле метода calculate вычисляем наполнение рюкзака предметами в пределах массы самих предметов.
    То есть грузоподъемность рюкзака меняется от 0 до веса самого тяжелого предмета.
    Во втором цикле проходимся опять по всем предметам, но теперь в метод recursive первым аргументом подаем
    заданную грузоподъемоность и вычисляем для нее наборы предметов, рекурсивно вычитая из макс. грузоподъемности
    вес придмета на данной итерации цикла. Так мы проходим от capacity до известного вычесленного веса
    рюкзака на предыдущих итерациях. Вычислив наполнение рюкзака на данном весе рюкзака и при данном
    предмете, мы выходим из рекурсии и вычисляем наполнение рюкзака на большем весе, доходя тем самым 
    до максимальной грузоподъемности.
        Пример: 
            Вес предмета: 2
            Макс. груз. рюкзака: 10
            Вычеслено наполнение для веса рюкзака 4
            1-ый вызов: recursive(10, 2, index, weights)
            2-ой вызов: recursive(10-2, 2, index, weights)
            3-й вызов: recursive(10-2-2, index, weights)
            На третьем вызове, функции recursive убеждаемся, что столбец weights[4] посчитан, и начинаем вычислять
            для weights[6]. Вычислив для 6, поднимаемся по рекурсии до weights[8], вычисляем для него. Поднялись до
            weights[10] и на основе weights[8] вычислеям его наполнение.
"""""


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
            # ключ (bag_weight) - вес рюкзака
            # значение - словарь
            #   ключ (index) - индекс предмета в отсортированном массиве предметов
            #   значение - [ценность рюкзака, [индексы предметов в рюкзаке]]
        return weights

    def set_items_indexes(self):
        for i in range(0, len(self.items)):
            self.items[i].append([i])
            # Присваиваем каждому предмету его изначальный индекс по порядку добавления

    def recursive(self, bag_weight, item_weight, index, weights):
        if bag_weight-item_weight not in weights.keys():
            if bag_weight not in weights.keys():
                weights[bag_weight] = {}
                weights[bag_weight][0] = [0, []]

            elif bag_weight - item_weight >= self.items[1][0][0]:
                self.recursive(bag_weight-item_weight, item_weight, index, weights)
                self.recursive(bag_weight, item_weight, index, weights)

            else:
                if index-1 not in weights[bag_weight]:
                    self.recursive(bag_weight, self.items[index-1][0][0], index-1, weights)
                _prev_v = weights[bag_weight][index-1][0]
                _sum = self.items[index][0][1]

                if self.items[index][0][0] <= bag_weight:
                    if ((_sum == _prev_v) and (self.items[index][0][0] < self.items[index-1][0][0]))\
                            or (_sum > _prev_v):
                            weights[bag_weight][index] = [_sum, []]
                            weights[bag_weight][index][1].append(index)
                            return
                weights[bag_weight][index] = weights[bag_weight][index - 1]
        else:
            if bag_weight not in weights.keys():
                weights[bag_weight] = {}
                weights[bag_weight][0] = [0, []]

            elif index == 1:
                weights[bag_weight][index] = [self.items[index][0][1], [index]]

            elif index == 0:
                weights[bag_weight][index] = [0, []]

            else:
                if index-1 not in weights[bag_weight-item_weight]:
                    self.recursive(bag_weight-item_weight, self.items[index-1][0][0], index-1, weights)
                sum = self.items[index][0][1] + weights[bag_weight - item_weight][index - 1][0]

                if index-1 not in weights[bag_weight]:
                    self.recursive(bag_weight, self.items[index-1][0][0], index-1, weights)
                prev_v = weights[bag_weight][index-1][0]

                if self.items[index][0][0] <= bag_weight:
                    if ((sum == prev_v) and (self.items[index][0][0] < self.items[index-1][0][0])) or (sum > prev_v):
                        weights[bag_weight][index] = [sum, []]
                        weights[bag_weight][index][1] = \
                            [i for i in weights[bag_weight - item_weight][index - 1][1]]

                        if index not in weights[bag_weight][index][1]:
                            weights[bag_weight][index][1].append(index)
                            return
                weights[bag_weight][index] = [prev_v, []]
                weights[bag_weight][index][1] = \
                    [j for j in weights[bag_weight][index - 1][1]]
        return

    def calculate(self):

        self.set_items_indexes()
        # Устанавливаем индексы каждому предмету в соотв. порядка его добавления

        self.items.sort(key=lambda item: item[0][0])
        # Сортируем предметы по весу

        weights = self.make_weights()
        # Создаем словарь из весов всех предметов, в который будет потом добавлять новые веса рюкзака

        for i in range(0, len(self.items)):
            item_weight = self.items[i][0][0]  # вес предмета
            for bag_weight in list(weights):
                self.recursive(bag_weight, item_weight, i, weights)

        for i in range(0, len(self.items)):
            # Проходим по всем весам предметов, которые вычитаем рекурсивно вычитаем из максимальной
            # грузоподъемности рюкзака, чтобы найти промежуточные веса рюкзака, при помощи которых найдем
            # ценность при макс. грузе  при каждом возможном количестве предметов
            item_weight = self.items[i][0][0]
            self.recursive(self.capacity, item_weight, i, weights)

        result_weight = 0
        result_value = weights[self.capacity][len(self.items)-1][0]
        indexes = []

        for i in weights[self.capacity][len(self.items)-1][1]:
            result_weight += self.items[i][0][0]
            indexes.append(self.items[i][1][0])
        indexes.sort()

        return [result_weight, result_value, indexes]


def process(b, item):
    if re.fullmatch(r'[\d+]+ [\d+]+', item):
        arguments = item.split(' ')
        arguments[0] = int(arguments[0])
        arguments[1] = int(arguments[1])
        b.add_item(arguments[0], arguments[1])
        return
    print('error')
    return


if __name__ == "__main__":
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
