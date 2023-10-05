"""2 -

Створіть ітератор, який приймає послідовність і може перебирати значення в заданому діапазоні. \
    CustomIterator(послідовність, початковий_індекс, кінцевий_індекс)

Create an iterator that accepts a sequence and can iterate over values in a given range. \
     CustomIterator(sequence, start_index, end_index)

"""


class NewIterator:
    def __init__(self, sequence, start_i, end_i):
        self.sequence = sequence
        self.start_i = start_i
        self.end_i = end_i

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_i < len(self.sequence) and self.start_i <= self.end_i:
            result = self.sequence[self.start_i]
            self.start_i += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    my_list = [10, 45, 11, 1, 7]
    my_iter = NewIterator(my_list, 1, 5)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
