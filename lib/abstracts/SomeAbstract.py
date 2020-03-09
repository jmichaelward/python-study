"""
This is an attempt at an abstract class. I'm just making up names for now to get the concepts down.
"""
from abc import ABC, abstractmethod


class SomeAbstract(ABC):
    @abstractmethod
    def print_name(self):
        pass

