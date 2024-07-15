#This program creates one of either two subclasses
#We continue with C.R.U.D.
#These subclasses also affect the tax  amount

from PersonSubClass import *

if __name__ == "__main__":
    Flag1 = True
    while Flag1:
        Flag2 = True
        while Flag2:
            CustomerType = (input("Please enter if \"Staff\" or \"Student\": "))
            CustomerType = CustomerType.strip()
            if CustomerType == "Staff":
                order = Staff()
                order.Create()
                Flag2 = False
            elif CustomerType == "Student":
                order = Student()
                order.Create()
                Flag2 = False
            else:
                print("Invalid Entry")
                print("Please try again - Case Sensitive\n")
        help(order)
        userInputToContinue = input("Continue for another order(Any keys= Yes, n= No)?")
        if userInputToContinue.lower() == 'n':
            print("The system is shutting down!")
            Flag1 = False

'''
Please enter if "Staff" or "Student": Staff

Would you like to create an order?
Press 1 for yes, 2 for no: 1

----------- De Anza Food Court -----------
1. De Anza Burger       5.25
2. Bacon Cheese         5.75
3. Mushroom Swiss       5.95
4. Western Burger       5.95
5. Don Cali Burger      5.95
6. Exit

Please enter a menu selection: 1
Quantity : 10
Item added

Please enter a menu selection: 6

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: R

---------------------------REVIEWING ORDER----------------------------
De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
----------------------------------------------------------------------
Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
----------------------------------------------------------------------
Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------

Price before tax: 52.5
Price after tax:  57.23

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: u
Error: Invalid Selection

Please try again (Case Sensitive)

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: U

How would you like to update your order? (Remove Items/Add Missing Items)
Press 1 to update or 2 to exit selection: 1

Please enter the item you would like to update(Case Sensitive): 
Mushroom Swiss

Enter how many to remove or add(enter negative number to remove): 5
5 Mushroom Swiss(s) added

How would you like to update your order? (Remove Items/Add Missing Items)
Press 1 to update or 2 to exit selection: 2

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: D

How would you like to cancel?

Enter 0 to cancel the order
Enter 1 to cancel an item
Enter 2 to exit selection
1
Please enter the item you would like to delete(Case Sensitive): 
De Anza Burger
De Anza Burger has been deleted

Enter 0 to cancel the order
Enter 1 to cancel an item
Enter 2 to exit selection
2

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: R

---------------------------REVIEWING ORDER----------------------------
De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
----------------------------------------------------------------------
Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
----------------------------------------------------------------------
Mushroom Swiss       Qty: 5          Price: $5.95       Total: $29.75     
----------------------------------------------------------------------
Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------

Price before tax: 29.75
Price after tax:  32.43

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: 0

Your bill:
----------------------------------------------------------------------
 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
----------------------------------------------------------------------
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
----------------------------------------------------------------------
 Mushroom Swiss       Qty: 5          Price: $5.95       Total: $29.75     
----------------------------------------------------------------------
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------

Price before tax: 29.75
Price after tax: 32.43

Continue for another order(Any keys= Yes, n= No)?Y

NEGATIVE TESTING

Please enter if "Staff" or "Student": Negative
Invalid Entry
Please try again - Case Sensitive

Please enter if "Staff" or "Student": Student

Would you like to create an order?
Press 1 for yes, 2 for no: Negative
Please enter a valid number

Press 1 for yes, 2 for no: 1

----------- De Anza Food Court -----------
1. De Anza Burger       5.25
2. Bacon Cheese         5.75
3. Mushroom Swiss       5.95
4. Western Burger       5.95
5. Don Cali Burger      5.95
6. Exit

Please enter a menu selection: Negative
Error: Please enter a numerical value


Please enter a menu selection: 3
Quantity : Negative
Error: Please enter a numerical value

Quantity : 5
Item added

Please enter a menu selection: 6

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: Negative
Error: Invalid Selection

Please try again (Case Sensitive)

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: R

---------------------------REVIEWING ORDER----------------------------
De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
----------------------------------------------------------------------
Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
----------------------------------------------------------------------
Mushroom Swiss       Qty: 5          Price: $5.95       Total: $29.75     
----------------------------------------------------------------------
Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------

Price before tax: 29.75
Price after tax:  29.75

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: U

How would you like to update your order? (Remove Items/Add Missing Items)
Press 1 to update or 2 to exit selection: Negative
Error: Please enter a valid number

Press 1 to update or 2 to exit selection: 1

Please enter the item you would like to update(Case Sensitive): 
Negative
Error: Invalid Item

Please enter the item you would like to update(Case Sensitive): 
Western Burger

Enter how many to remove or add(enter negative number to remove): Negative
Error: Please enter a valid number

Enter how many to remove or add(enter negative number to remove): 5
5 Western Burger(s) added

How would you like to update your order? (Remove Items/Add Missing Items)
Press 1 to update or 2 to exit selection: 2

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: D

How would you like to cancel?

Enter 0 to cancel the order
Enter 1 to cancel an item
Enter 2 to exit selection
Negative
Invalid Entry

Enter 0 to cancel the order
Enter 1 to cancel an item
Enter 2 to exit selection
1
Please enter the item you would like to delete(Case Sensitive): 
Negative

Error: Item does not exist
Please enter the item you would like to delete(Case Sensitive): 
Mushroom Swiss
Mushroom Swiss has been deleted

Enter 0 to cancel the order
Enter 1 to cancel an item
Enter 2 to exit selection
2

Please enter R to Read the order, U to update the order, D to Delete within the order, or 0 to pay: 0

Your bill:
----------------------------------------------------------------------
 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
----------------------------------------------------------------------
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
----------------------------------------------------------------------
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------
 Western Burger       Qty: 5          Price: $5.95       Total: $29.75     
----------------------------------------------------------------------
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
----------------------------------------------------------------------

Price before tax: 29.75
Price after tax: 29.75

Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!
'''
