# Abstract Factory in python
from abc import ABC, abstractmethod


class CoffeeStore(ABC):

    @abstractmethod
    def coffee_with_milk(self):
        pass

    @abstractmethod
    def coffee_without_milk(self):
        pass


class CoffeeWithMilk(ABC):

    @abstractmethod
    def serve(self, coffee_without_milk):
        pass


class CoffeeWithOutMilk(ABC):

    @abstractmethod
    def serve(self, coffee_without_milk):
        pass


class ItalianEspressoCoffee(CoffeeWithOutMilk):

    def serve(self, coffee_without_milk=CoffeeWithOutMilk):
        return f'Italian Espresso Coffee served, {self}, {coffee_without_milk}'


class ItalianCappuccinoCoffee(CoffeeWithMilk):

    def serve(self, coffee_without_milk=CoffeeWithMilk):
        return f'Italian Cappuccino Coffee served, {self}, {coffee_without_milk}'


class FrenchEspressoCoffee(CoffeeWithOutMilk):

    def serve(self, coffee_without_milk=CoffeeWithOutMilk):
        return f'French Espresso Coffee served, {self}, {coffee_without_milk}'


class FrenchCappuccinoCoffee(CoffeeWithMilk):

    def serve(self, coffee_without_milk=CoffeeWithMilk):
        return f'French Cappuccino Coffee served, {self}, {coffee_without_milk}'


class ItalianCoffee(CoffeeStore):

    @property
    def coffee_with_milk(self):
        return ItalianCappuccinoCoffee()

    @property
    def coffee_without_milk(self):
        return ItalianEspressoCoffee()


class FrenchCoffee(CoffeeStore):

    @property
    def coffee_with_milk(self):
        return FrenchCappuccinoCoffee()

    @property
    def coffee_without_milk(self):
        return FrenchEspressoCoffee()


if __name__ == '__main__':
    italian_coffee = ItalianCoffee()
    french_coffee = FrenchCoffee()

    coffees = [italian_coffee, french_coffee]

    for coffee in coffees:
        print(coffee.coffee_with_milk.serve())
        print('#' * 30)
        print(coffee.coffee_without_milk.serve())
        print('#' * 30)
