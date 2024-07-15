#This file contains the Mushroom Burger Subclass
from SuperBurger import Burger

class Mushroom(Burger):
    def __init__(self):
        super().__init__("Mushroom Swiss",5.95)
    def display(self):
        print("3. {b:15s} {c:9.2f}".format(b = self.name,c=self.price))
