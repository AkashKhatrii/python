from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def cost(self):
        pass

    def description(self):
        pass


class PepperoniPizza(Pizza):
    def cost(self):
        return 5

    def description(self):
        return "plain peperroni pizza"
    

class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

class OlivesDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def cost(self):
        return self.pizza.cost() + 1
    
    def description(self):
        return self.pizza.description() + ", olives"
    
class JalapenoDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    
    def cost(self):
        return self.pizza.cost() + 2
    
    def description(self):
        return self.pizza.description() + ", jalapeno"
    

if __name__ == "__main__":

    pizza = PepperoniPizza()
    print("initial price: ", pizza.cost())

    pizza = OlivesDecorator(pizza)
    print("after olive price: ", pizza.cost())

    pizza = JalapenoDecorator(pizza)
    print("after jalapeno price: ", pizza.cost())

    print(pizza.description())


