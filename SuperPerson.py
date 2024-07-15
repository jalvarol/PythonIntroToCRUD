#This file contains the Person Super Class
#Subclasses Teacher and Student will inherit from this
from SuperOrder import Order

class Person(Order):
    '''
    Here we create a class Person with a superclass of Orders
    A Person is considered an Order
    '''
    def __init__(self):
        super().__init__()
        
    def calculate(self):
        '''
        This method overrides the calculate method from Order SuperClass
        '''
        self._priceBtax = 0
        self._priceAtax = 0
        for key in self._priceDict:
            self._priceBtax += self._orderDict[key] * self._priceDict[key]
            self._priceAtax = self._priceBtax + (self._priceBtax * self._tax)
    def Read(self):
        '''
        This method reviews the order
        '''
        print("\n"+"-"*27+"REVIEWING ORDER"+"-"*28)
        for key in self._orderDict:
            print("%-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %(key,self._orderDict[key],self._priceDict[key],\
                                                                        (self._orderDict[key]*self._priceDict[key])))
            print("-"*70)
        print("\nPrice before tax:", round(self._priceBtax,2))
        print("Price after tax: " , round(self._priceAtax,2))

    def Update(self):
        '''
        Here we update the order. We use 4 while loops. One main outer and 2 nested.
        The 2 Nested ones check for user error. Another nested while loop also checks for user
        error
        '''
        Flag1 = True
        while Flag1:
            print("\nHow would you like to update your order? (Remove Items/Add Missing Items)")
            Flag2 = True
            while Flag2:
                try:
                    UserReply = int(input("Press 1 to update or 2 to exit selection: "))
                    Flag2 = False
                    if UserReply == 2:
                        Flag1 = False
                    elif UserReply > 2 or UserReply < 1:
                        print("Error: Invalid Selection\n")
                        Flag2 = True
                except:
                    print("Error: Please enter a valid number\n")
            Flag3 = True
            while Flag1 and Flag3:
                    ItemUpdate = input("\nPlease enter the item you would like to update(Case Sensitive): \n")
                    if ItemUpdate in self._orderDict:
                        Flag4 = True
                        while Flag4:
                            try:
                                UpdateAmount = int(input("\nEnter how many to remove or add(enter negative number to remove): "))
                                Flag4 = False
                            except:
                                print("Error: Please enter a valid number")
                        if UpdateAmount < 0:
                            print("The Quantity will be set to 0 if the Update Amount is less")
                        self._orderDict[ItemUpdate] += UpdateAmount
                        for key in self._orderDict:
                            if self._orderDict[key] < 0:
                                self._orderDict[key] = 0
                        Flag3 = False
                        print(str(UpdateAmount)+" "+ItemUpdate+"(s) added")
                    else:
                        print("Error: Invalid Item")
                        Flag3 = True

    def Delete(self):
        '''
        Here we determine what the user wants to cancel. Either the whole order, an item,
        or the user can cancel this selection. We use an outer loop to continue canceling
        items. The nested while loops are used to check for user error
        '''
        Flag1 = True
        while Flag1:
            print("\nHow would you like to cancel?")
            Flag2 = True
            while Flag2: 
                try:
                    Choice = int(input("\nEnter 0 to cancel the order\n"\
                                       "Enter 1 to cancel an item\n"\
                                       "Enter 2 to exit selection\n"))
                    Flag2 = False

                    if Choice == 0:
                        Flag1 = False
                        for key in self._orderDict:
                            self._orderDict[key] = 0
                    elif Choice == 1:
                        Flag3 = True
                        while Flag3:
                            ItemUpdate = input("Please enter the item you would like to delete(Case Sensitive): \n")
                            if ItemUpdate in self._orderDict:
                                print(ItemUpdate+" has been deleted")
                                self._orderDict[ItemUpdate] = 0
                                Flag3 = False
                                Flag2 = True
                            else:
                                print("\nError: Item does not exist")
                    elif Choice == 2:
                        Flag1 = False
                    else:
                        print("Please enter a valid number")
                        Flag2 = True
                except:
                    print("Invalid Entry")
    def getTax(self):
        return self._tax
 
