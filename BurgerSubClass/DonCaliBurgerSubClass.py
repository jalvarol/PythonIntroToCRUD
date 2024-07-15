#This file contains the Don Cali Burger Subclass

from SuperBurger import Burger

class DonCali(Burger):
    def __init__(self):
        super().__init__("Don Cali Burger",5.95)
    def display(self):
        print("5. {b:15s} {c:9.2f}".format(b = self.name,c=self.price))
