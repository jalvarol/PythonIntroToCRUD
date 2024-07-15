#This file contains the De Anza Burger Subclass
from SuperBurger import Burger

class DeAnza(Burger):
    def __init__(self):
        super().__init__("De Anza Burger",5.25)
    def display(self):
        print("1. {b:15s} {c:9.2f}".format(b = self.name,c=self.price))
