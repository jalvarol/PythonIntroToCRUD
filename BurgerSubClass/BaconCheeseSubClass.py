#This file contains the Bacon Cheese Subclass

from SuperBurger import Burger

class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 5.75)
    def display(self):
        print("2. {b:15s} {c:9.2f}".format(b = self.name,c=self.price))
