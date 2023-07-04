#!/usr/bin/env python3

class SimpleIterator:
    def __init__(self, counter):
        self.counter = counter


    def __iter__(self):
        self.init_value = 0
        return self


    def __next__(self) -> int:
        if self.init_value < self.counter:
            self.init_value += 1
            return self.init_value
        raise StopIteration


if __name__ == "__main__":
    test_iter = SimpleIterator(10)
    print(list(test_iter))
    print(list(test_iter))
    for x in test_iter:
        print(x)
