class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    
    
    def __iter__(self):
        self.main_list = 0
        self.new_main_list = 0
        return self

    def __next__(self):
        if self.main_list == len(self.list_of_list):
             raise StopIteration
        item_main = self.list_of_list[self.main_list]
        item = item_main[self.new_main_list]
        self.new_main_list += 1
        if self.new_main_list == len(item_main):
            self.new_main_list = 0
            self.main_list += 1
        print(item)
        return item
            

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
      