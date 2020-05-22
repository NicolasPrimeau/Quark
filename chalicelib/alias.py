import string
from abc import ABCMeta, abstractmethod
import random
from typing import List


def get_acceptable_characters() -> List[str]:
    chars = list()
    chars.extend(string.ascii_letters)
    chars.extend(string.digits)
    return chars


class AliasGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate_alias(self, length: int) -> str:
        pass


class RandomAliasGenerator(AliasGenerator):

    def __init__(self):
        self._choice = get_acceptable_characters()

    def generate_alias(self, length: int) -> str:
        return ''.join(random.choices(self._choice, k=length))
