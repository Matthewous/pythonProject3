class FlatIterator:

    def __init__(self, list_of_list):
        self.start = 0
        self.list_num = 0
        self.item = 0
        self.list_finish = list(len(nested_list) for nested_list in list_of_list)
        self.finish = len(list_of_list)
        self.all = list_of_list

    def __iter__(self):
        return self

       
    def __next__(self):
        if self.item < self.list_finish[self.list_num]:
            item = self.all[self.list_num][self.item]
            self.item += 1
            return item
        else:
            self.item = 0
            self.list_num += 1
            if self.list_num < self.finish:
                item = self.all[self.list_num][self.item]
                self.item += 1
                return item
            else:
                raise StopIteration


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

def print_result():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    print(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()
    print_result()