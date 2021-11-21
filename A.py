
class Bag:

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.items = []
        self.items.append([0])

    def set_cap(self, cap):
        self.capacity = cap

    def add_item(self, weight, price):
        """""
        if [weight, price] not in self.items:    ВЫНЕСТИ В ОБРАБОТЧИК КОМАНД
        
        else:
            print("error")
        """""
        self.items.append([weight, price])

    def calculate(self):
        previous = [[0, []] for _ in range(0, self.capacity+1)]
        current = [[0, []] for _ in range(0, self.capacity+1)]
        # массив вида current[i] = [value, [indexes]], где value - ценность всего рюкзака
        # [indexes] - индексы предметов, находящихся в рюкзаке при данной ценности
        # i - вес рюкзака
        for i in range(1, len(self.items)):  # индексы предметов
            for j in range(1, self.capacity+1):  # индексы весов рюкзака
                if self.items[i][0] > j:
                    current[j] = previous[j]
                else:
                    value = max(previous[j][0], self.items[i][1] + previous[j-self.items[i][0]][0])
                    if previous[j][0] == value:
                        current[j] = previous[j]
                    else:
                        current[j][0] = value
                        current[j][1] = [e for e in previous[j-self.items[i][0]][1]]
                        current[j][1].append(i)
            previous = current
            if i != len(self.items)-1:
                current = [[0, []] for _ in range(0, self.capacity+1)]

        result_weight = 0
        for index in current[self.capacity][1]:
            result_weight += self.items[index][0]
        return [result_weight, current[self.capacity][0], current[self.capacity][1]]

def process(b: Bag, item):
    pass


if __name__ == "__main__":

    bag = Bag()

    while True:
        size = input()
        if size.isnumeric():
            bag.set_cap(size)
            break
    while True:
        try:
            text = input()
            if text != '':
                process(bag, text)
        except EOFError:
            break





    bag.add_item(23, 92)
    bag.add_item(31, 57)
    bag.add_item(29, 49)
    bag.add_item(44, 68)
    bag.add_item(53, 60)
    bag.add_item(38, 43)
    bag.add_item(63, 67)
    bag.add_item(85, 84)
    bag.add_item(89, 87)
    bag.add_item(82, 72)
    result = bag.calculate()
    print(result)

