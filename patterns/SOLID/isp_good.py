from abc import ABC, abstractmethod


class Walker(ABC):
    @abstractmethod
    def walk(self) -> None:
        return print("Can Walk")


class Swimmer(ABC):
    @abstractmethod
    def swim(self) -> None:
        return print("Can Swim")


class Human(Walker, Swimmer):
    def walk(self):
        return print("Humans can walk")

    def swim(self):
        return print("Humans can swim")


class Whale(Swimmer):
    def swim(self):
        return print("Whales can swim")


if __name__ == "__main__":
    Human().walk()
    Human().swim()

    Whale().swim()
    # Whale().walk()
