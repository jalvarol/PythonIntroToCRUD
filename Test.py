import unittest
from BurgerSubClass import *
from PersonSubClass import *

class TestOrder(unittest.TestCase):
    #Testing Burger SubClass getName()
    def test_getName(self):
        
        a1 = DeAnza()
        self.assertNotEqual(a1.getName(),"Burger")
        self.assertEqual(a1.getName(), "De Anza Burger")
        
        a1 = BaconCheese()
        self.assertNotEqual(a1.getName(),"Burger")
        self.assertEqual(a1.getName(), "Bacon Cheese")

        a1 = Mushroom()
        self.assertNotEqual(a1.getName(),"Burger")
        self.assertEqual(a1.getName(), "Mushroom Swiss")

        a1 = Western()
        self.assertNotEqual(a1.getName(),"Burger")
        self.assertEqual(a1.getName(), "Western Burger")

        a1 = DonCali()
        self.assertNotEqual(a1.getName(),"Burger")
        self.assertEqual(a1.getName(), "Don Cali Burger")

        
    #Testing Burger Subclass getPrice()
    def test_getPrice(self):
         
        a1 = DeAnza()
        self.assertNotEqual(a1.getPrice(),5)
        self.assertEqual(a1.getPrice(),5.25)
        
        a1 = BaconCheese()
        self.assertNotEqual(a1.getPrice(),5)
        self.assertEqual(a1.getPrice(),5.75)
        
        a1 = Mushroom()
        self.assertNotEqual(a1.getPrice(),5)
        self.assertEqual(a1.getPrice(),5.95)
        
        a1 = Western()
        self.assertNotEqual(a1.getPrice(),5)
        self.assertEqual(a1.getPrice(),5.95)
        
        a1 = DonCali()
        self.assertNotEqual(a1.getPrice(),5)
        self.assertEqual(a1.getPrice(),5.95)
        
    #Testing PersonSubClass getTax()
    def test_getTax(self):
        a1 = Staff()
        self.assertEqual(a1.getTax(),0.09)
        self.assertNotEqual(a1.getTax(),0)
        
        a1 = Student()
        self.assertEqual(a1.getTax(),0)
        self.assertNotEqual(a1.getTax(),0.09)
    #Testing getInputs()
    def test_Input(self):
        a1 = Staff()
        a1.displayMenu()
        a1.getInputs()
        total = 0
        for key in a1._orderDict:
            total += a1._orderDict[key]
        self.assertEqual(a1.getItemCount(),total)
        
    #Testing Delete()
    def test_Delete(self):
        a1 = Staff()
        a1.displayMenu()
        a1.getInputs()
        a1.Delete()
        total = 0
        for key in a1._orderDict:
            total += a1._orderDict[key]
        self.assertEqual(a1.getItemCount(),total)

    

if __name__== "__main__":
    unittest.main()
