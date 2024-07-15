#This file contains the Western Burger Subclass
from SuperBurger import Burger

class Western(Burger):
    def __init__(self):
        super().__init__("Western Burger",5.95)
    def display(self):
        print("4. {b:15s} {c:9.2f}".format(b = self.name,c=self.price))
