#A menu-drive program for a Food Court. This program
#will take the users order. Calculate the costs of each individual item
#Then it will calculate the tax dependent if the user is staff or student
#Will show the total before taxes, after taxes, and the costs of each
#item x the quantity "
from BurgerSubClass import *
import time
import datetime
class Order:
    '''
    This class will have 5 functions and 1 constructor
    2 instance variables that will be used everywhere within
    our class; The order class will be the root of all classes within these files
    '''

    _priceDict = dict()
    _orderDict = dict()
    _burgerDict = dict()
    _total = 0

    def __init__(self):      
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0
        self._total = 0
        a1 = DeAnza()
        a2 = BaconCheese()
        a3 = Mushroom()
        a4 = Western()
        a5 = DonCali()
        self._burgerDict = {1:a1.display,2:a2.display,3:a3.display,4:a4.display,5:a5.display}
        self._priceDict = {a1.getName(): a1.getPrice(), a2.getName(): a2.getPrice(),
                      a3.getName(): a3.getPrice(), a4.getName(): a4.getPrice(),
                      a5.getName(): a5.getPrice()}    
        self._orderDict = {a1.getName() : 0 , a2.getName() : 0,
                       a3.getName() : 0, a4.getName() : 0,
                       a5.getName() : 0}

    def displayMenu(self):
        '''
        I took this menu from the example since it was very clean.
        Credit given where credits dues
        This displays the menu used the price Dictionary by going
        through each key. 
        '''
        print("\n----------- De Anza Food Court -----------")
        for key in self._burgerDict:
            function = self._burgerDict.get(key)
            function()
        print("6. Exit")

    def getInputs(self):
        '''
        I brought the same style over from my midterm 1. The key differences here
        are that we are incrementing the values in our Order Dictionary. We still
        use the same While Loops, with the same flags, and error checking. 
        '''
        order = 0
        #This while loop checks for input errors for the order
        #numbers(1-5)
        Flag1 = True
        while Flag1:
            Flag2 = True
            while Flag2:
                try:
                    order = int(input("\nPlease enter a menu selection: "))
                    Flag2 = False
                    if order==6:
                        Flag1 = False
                    elif order <= 0 or order > 5:
                        print("Please enter a valid menu selection")
                        Flag2 = True
                except:
                    print("Error: Please enter a numerical value\n")

            #This while loop continues as long as both flags are true
            #It will be disrupted if order == 6
            Flag3 = True
            while Flag3 and Flag1:
                try:
                    quantity = int(input("Quantity : "))
                    Flag3 = False
                    if quantity < 0:
                         print("Please enter a valid number\n")
                         Flag3 = True
                    elif order == 1:
                         self._orderDict["De Anza Burger"] += quantity
                    elif order == 2:
                        self._orderDict["Bacon Cheese"]    += quantity
                    elif order == 3:
                        self._orderDict["Mushroom Swiss"]  += quantity
                    elif order == 4:
                        self._orderDict["Western Burger"]  += quantity
                    elif order == 5:
                        self._orderDict["Don Cali Burger"] += quantity
                    else:
                        Flag3 = False
                    print("Item added")
                except:
                    print("Error: Please enter a numerical value\n")
    def calculate(self):
        '''
        In this section we prompt the user to tell us if they are a student or
        staff. This will change the tax variable. We will also store the before
        and after taxes total in our 2 variables; _priceBtax and _priceAtax
        '''
        CustomerType = 0
        while CustomerType <= 0 or CustomerType >2:
            try:
                CustomerType = int(input("\nPlease enter 1 if student or 2 if staff: "))
                CorrectInput = False
            except:
                print("Error: Please enter a numerical value")
        if CustomerType == 2:
            self._tax = .09            
        for key in self._priceDict:
            self._priceBtax += self._orderDict[key] * self._priceDict[key]
            self._priceAtax = self._priceBtax + (self._priceBtax * self._tax)
            
    def printBill(self):
        '''
        Here we will call our Order Dictionary, the before tax total, and the
        after tax total to the console. Again, this code was taken from the sample
        given
        '''
        for key in self._orderDict:
            if self._orderDict[key] != 0:
                self._total+= self._orderDict[key]
        Flag1 = True
        while Flag1:
            if self._total == 0:
                print("\nNothing was ordered")
                print("No Receipt Printed nor Bill Issued")
                Flag1 = False
            else:
                print("\nYour bill:")
                print("-"*70)
                for key in self._orderDict:
                    print(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %(key,self._orderDict[key],self._priceDict[key],\
                                                                                (self._orderDict[key]*self._priceDict[key])))
                    print("-"*70)
                print("\nPrice before tax:", round(self._priceBtax,2))
                print("Price after tax:" , round(self._priceAtax,2))
                Flag1 = False
                
    def saveToFile(self):
       '''
       This part basically copies the printBill function but instead of printing
       we will be writing to an outfile.It will include an identical copy along with
       time stamps
       '''
       Flag1 = True
       while Flag1:
           if self._total == 0:
               print("\nThank you! Take Care!")
               Flag1 = False
           else:
               timeStamp = time.time()
               orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
               orderTimeStamp = orderTimeStamp+".txt"
               with open(orderTimeStamp,'w') as fileHandleToSaveTheBill :
                   fileHandleToSaveTheBill.write("Your bill:\n")
                   fileHandleToSaveTheBill.write("-"*70)
                   for key in self._orderDict:
                       fileHandleToSaveTheBill.write("\n %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %(key,self._orderDict[key],self._priceDict[key],\
                                                                            (self._orderDict[key]*self._priceDict[key]))+"\n")
                       fileHandleToSaveTheBill.write("-"*70)

                   fileHandleToSaveTheBill.write("\nPrice before tax: " + str(round(self._priceBtax,2)))
                   fileHandleToSaveTheBill.write("\nPrice after tax: "+str(round(self._priceAtax,2)))
                   Flag1 = False
    def getItemCount(self):
        self._total = 0
        for key in self._orderDict:
            if self._orderDict[key] != 0:
                self._total+= self._orderDict[key]
        return self._total
