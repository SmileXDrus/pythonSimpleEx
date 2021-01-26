from typing import List
from dataclasses import dataclass, field


class PositiveValueError(ValueError):
    def __init__(self, value, *args):
        self.value = value
        for item in args:
            print(item)

    def __str__(self):
        return f'Ваше число {self.value} отрицательно. А возраст не может быть меньше 0'


@dataclass  # Docs: https://docs.python.org/3/library/dataclasses.html
class Food:  # Датаклассы сразу реализуют полезные методы: сравнение, вывод, экземпляр
    # init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False
    name: str
    food_type: str


@dataclass
class Animal:
    name: str
    age: int
    type_animal: str
    food: Food

    def __post_init__(self):
        if self.age < 0:
            raise PositiveValueError(self.age)


@dataclass(frozen=True)  # неизменяемые у класса атрибуты
class Zoo:
    animals: List[Animal] = field(default_factory=list)


food = Food('Honey', 'sweet')
food1 = Food('Honey', 'sweet')
bear = Animal('Faust', 5, 'bear', food)
zoo = Zoo([])

print('Сравнение:', food == food1)
zoo.animals.append(bear)
print(zoo)
