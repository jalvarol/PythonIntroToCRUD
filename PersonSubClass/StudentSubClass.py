#This class contains the Student Subclass - extends Person SuperClass

import time
import datetime
import os
from os import path
from SuperPerson import Person

class Student(Person):
    
    '''
    This subclass Student is-a Person. This subclass will change the tax rate
    and a little line of code for the output file
    '''
    def __init__(self):
        '''
        We override the method from Person since we know this class is a Student,
        therefore the tax variable is set to 0
        '''
        super().__init__()
        self._tax = 0
                             
    def saveToFile(self):
        '''
        This part basically copies the printBill function but instead of printing
        we will be writing to an outfile.It will include an identical copy along with
        time stamps; small change - output file will state "Student Bill"
        '''
        Flag1 = True
        while Flag1:
            if self._total == 0:
                print("\nThank you! Take Care!")
                Flag1 = False
            else:
                Directory = os.getcwd()  
                if path.isdir("Student Receipts"):
                    print("Receipt Added to Student Receipt Folder")
                else:
                    os.chdir(Directory)
                    os.mkdir("Student Receipts")
                Directory = os.path.join(Directory,"Student Receipts")
                timeStamp = time.time()
                orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
                orderTimeStamp = orderTimeStamp+".txt"
                orderTimeStamp = os.path.join(Directory,orderTimeStamp)
                with open(orderTimeStamp,'w') as fileHandleToSaveTheBill :
                    fileHandleToSaveTheBill.write("Student Bill:\n")
                    fileHandleToSaveTheBill.write("-"*70)
                    for key in self._orderDict:
                        fileHandleToSaveTheBill.write("\n %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %(key,self._orderDict[key],self._priceDict[key],\
                                                                                (self._orderDict[key]*self._priceDict[key]))+"\n")
                        fileHandleToSaveTheBill.write("-"*70)
                    fileHandleToSaveTheBill.write("\nPrice before tax: " + str(round(self._priceBtax,2)))
                    fileHandleToSaveTheBill.write("\nPrice after tax: "+str(round(self._priceAtax,2)))
                    Flag1 = False
    def Create(self):
        '''
        Here we determine if the user wants to create an order
        '''
        print("\nWould you like to create an order?")
        Flag1 = True
        while Flag1:
                choice = input("Press 1 for yes, 2 for no: ")
                if choice == "2":
                    Flag1 = False
                elif choice == "1":
                    Flag1 = False
                    order = Student()
                    order.displayMenu()
                    order.getInputs()
                    Flag1 = True
                    while Flag1:
                        order.calculate()
                        choice = input("\nPlease enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: ")
                        if choice == "R":
                            order.Read()
                        elif choice == "U":
                            order.Update()
                        elif choice == "D":
                            order.Delete()
                        elif choice == "0":
                            Flag1 = False
                        else:
                            print("Error: Invalid Selection\n")
                            print("Please try again (Case Sensitive)")
                    order.printBill()
                    order.saveToFile()
                else:
                    print("Please enter a valid number\n")
