from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.__nome = nome


def get_nome(self):
    return self.__nome

@abstractmethod
def fazer_som(self):
    pass