import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.limit = 0


    def __iter__(self):
        self.cursor = -1
        self.cursor_count = 0
        self.item = []
        return self


    def __next__(self):
        self.limit = len(self.list_of_list[self.cursor_count])


        if self.cursor >= self.limit - 1:
            self.cursor_count += 1
            self.cursor = 0
        elif self.cursor < self.limit - 1:
            self.cursor += 1

        if self.cursor_count == len(self.list_of_list):
            raise StopIteration


        self.item = self.list_of_list[self.cursor_count]

        return self.item[self.cursor]


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

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


