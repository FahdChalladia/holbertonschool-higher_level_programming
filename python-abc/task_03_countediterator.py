# task_03_countediterator.py

class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self._iterator)  # may raise StopIteration
        self._count += 1
        return value

    def get_count(self):
        return self._count
