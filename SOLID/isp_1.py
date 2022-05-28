import numpy as np
from abc import ABC, abstractmethod


class Mammals(ABC):
    @abstractmethod
    def swim(self) -> None:
        print("Can Swim")

    @abstractmethod
    def walk(self) -> None:
        print("Can Walk")


class Human(Mammals):
    def swim(self):
        return print("Humans can swim")

    def walk(self):
        return print("Humans can walk")


class Whale(Mammals):
    def swim(self):
        return print("Whales can swim")


if __name__ == "__main__":
    Human().swim()
    Human().walk()

    Whale().swim()
    # Whale().walk()
