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

