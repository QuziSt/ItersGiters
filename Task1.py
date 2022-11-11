# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их
# плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list
        self.parts = []
        self.new_list = self.extract_parts()

    def __iter__(self):

        return self

    def __next__(self):
        for item in self.new_list:
            return item

    def extract_parts(self):
        for part in self.lists:
            for piece in part:
                self.parts.append(piece)
        return self.parts


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
        yield flat_iterator_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
