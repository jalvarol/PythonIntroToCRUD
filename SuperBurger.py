#This file contains the Burger Class SuperClass
class Burger:
    name  = ""
    price = 0.0
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display(self):
        print("{b:15s} {c:8.2f}".format(b = self.name,c=self.price))
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name


