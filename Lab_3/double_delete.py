# Итератор для удаления дубликатов
class Unique(object):
    def init(self, items, ignore_case=False):

        self.index = -1  # Текущий индекс
        current = items[0]  # Последний уникальный элемент
        self.items = [current]  # Набор уникальных элементов

        for i in range(1, len(items)):
            if ((ignore_case == True or type(items[i]) != str) and items[i] not in self.items):
                self.items.append(items[i])
            if (ignore_case == False and type(items[i]) == str):
                add_flag = True
                for j in self.items:
                    if (type(j) == str and j.upper() == items[i].upper()):
                        add_flag = False
                        break
                if (add_flag):
                    self.items.append(items[i])
        self.len = len(self.items)  # Длина набора уникальных элементов


def next(self):
    if self.index == self.len - 1:
        raise StopIteration
    self.index += 1
    return self.items[self.index]


def iter(self):
    return self


# data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
# Uniq = Unique(data)

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
Uniq = Unique(data)

for i in Uniq:
    print(i)