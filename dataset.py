from typing import List

from abc import ABC, abstractmethod


class _IntDataset(ABC):
    """ Abstract Base Class for IntDatasets """

    @abstractmethod
    def __len__(self) -> int:
        """ returns length of dataset """

    @abstractmethod
    def __getitem__(self, index: int | slice) -> int | List[int]:
        """ return data at index """

# TODO: implement EvenDataset
class EvenDataset(_IntDataset):
    """
    EvenDataset returns even numbers from interval [a, b)
    if a or b is not even raise an error
    """
    def __init__(self, a, b):
        """
        Initialize EvenDataset
        Args:
            a: starting value of interval from which to draw, inclusive
            b: ending value of interval from which to draw, exclusive

        if a or b is not even, raise an error
        """
        #Prevent invalid data
        if a % 2 != 0:
            raise ValueError("a is not an even number. a and b must both be even numbers.")
        if b % 2 != 0:
            raise ValueError("b is not an even number. a and b must both be even numbers.")
        #Initialize data range
        self.a = a
        self.b = b

        #Create list of even numbers in the range of a and b
        self.dataset = list(range(a, b, 2)) #0.1417 secs
        #self.dataset = list(map(lambda x: x * 2, range(a // 2, b // 2))) #0.8769 secs
        #self.dataset = [x for x in range(a, b) if x % 2 == 0] #1.2385 secs

    def __len__(self):
        #Returns the length of the dataset.
        return len(self.dataset)

    def __getitem__(self, index: int | slice) -> int | List[int]:
        #Returns the value at index from dataset
        return self.dataset[index]
