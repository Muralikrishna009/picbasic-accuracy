"""
Order Entry System
Author: Usama Husain (original)
Date: 10-10-2024
Converted to Python by Claude
"""

import os
import datetime
from dataclasses import dataclass


@dataclass
class Customer:
    """Customer record structure"""
    number: str
    name: str
    date: str
    current_balance: float
    amount_due: float


@dataclass
class Product:
    """Product record structure"""
    number: str
    name: str
    price: float
    quantity: int
    features: str


@dataclass
class Order:
    """Order record structure"""
    number: str
    quantity: int
    price: float
    date: str
    client_number: str
    client_name: str
    company: str
    address: str
    phone_number: str


class OrderEntrySystem:
    def __init__(self):
        self.customer = Customer("", "", "", 0.0, 0.0)
        self.product = Product("", "", 0.0, 0, "")
        self.order = Order("", 0, 0.0, "", "", "", "", "", "")
        self.customer_file = {}  # Simulated database
        self.inventory_file = {}  # Simulated database
        
        # Initialize with sample data
        self.init_sample_data()

    def init_sample_data(self):
        """Initialize with some sample data for testing"""
        # Sample customer data
        self.customer_file["12345"] = ["ACME Corp", "", "", "", "", "", "", "20241010"]
        
        # Sample product data
        self.inventory_file["P1001"] = ["", "", "Widget X1", "High durability, water resistant", "", "100", "29.99"]

    def init_vars(self):
        """Initialize all variables with default values"""
        self.customer = Customer(
            number="##############",
            name="",
            date="DD/MM/YYYY",
            current_balance=0.0,
            amount_due=0.0
        )
        
        self.product = Product(
            number="############",
            name="",
            price=0.0,
            quantity=0,
            features=""
        )
        
        self.order = Order(
            number="############",
            quantity=0,
            price=0.0,
            date="DD/MM/YYYY",
            client_number="############",
            client_name="",
            company="",
            address="",
            phone_number=""
        )

    def display_screen(self):
        """Display the order entry screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('*' * 100)
        print('*' + ' ' * 40 + 'ORDER ENTRY SCREEN' + ' ' * 40 + '*')
        print('*' * 100)
        
        print(f"CUST#: {self.customer.number:<14} CUSTOMER NAME: {self.customer.name:<25} Date: {self.customer.date:<10}")
        print(f"CURR BALANCE: {self.customer.current_balance}")
        print(f"AMT DUE     : {self.customer.amount_due}")
        
        print('*' * 100)
        print(f"PRODUCT: {self.product.number:<38} PRICE: {self.product.price:<29} QUANTITY: {self.product.quantity:<10}")
        print(f"PRODUCT NAME: {self.product.name}")
        print(f"FEATURES    : {self.product.features}")
        
        print('*' * 100)
        print(f"CLIENT NO : {self.order.client_number:<63} NAME: {self.order.client_name:<20}")
        print(f"ORDER     : {self.order.number:<34} QTY: {self.order.quantity:<36} PRICE: {self.order.price:<10}")
        print(f"ORDER DATE: {self.order.date}")
        print(f"COMPANY   : {self.order.company}")
        print(f"ADDRESS   : {self.order.address}")
        print(f"PHONE NO  : {self.order.phone_number}")
        
        print('*' * 100)
        print("OPTIONS: S-Save, X-Exit")
        print('*' * 100)

    def display_error(self):
        """Display error message"""
        print("Invalid Input value")

    def customer_display(self, customer_number):
        """Look up and display customer information"""
        if customer_number in self.customer_file:
            cust_rec = self.customer_file[customer_number]
            self.customer.name = cust_rec[0]
            
            # Convert date format if needed
            try:
                raw_date = cust_rec[7]
                year = raw_date[0:4]
                month = raw_date[4:6]
                day = raw_date[6:8]
                self.customer.date = f"{day}/{month}/{year}"
            except (IndexError, ValueError):
                self.customer.date = "DD/MM/YYYY"
                
            self.customer.current_balance = ""
            self.customer.amount_due = ""
            return True
        else:
            self.display_error()
            return False

    def product_display(self, product_number):
        """Look up and display product information"""
        if product_number in self.inventory_file:
            prod_rec = self.inventory_file[product_number]
            
            self.product.name = prod_rec[2]
            self.product.features = prod_rec[3]
            
            try:
                self.product.quantity = int(prod_rec[5])
            except (IndexError, ValueError):
                self.product.quantity = 0
                
            try:
                self.product.price = float(prod_rec[6])
            except (IndexError, ValueError):
                self.product.price = 0.0
                
            return True
        else:
            self.display_error()
            return False

    def get_user_input(self):
        """Get input from user for customer and product"""
        while True:
            self.customer.number = input("Enter Customer ID: ")
            
            if self.customer.number.upper() == "END":
                return False
                
            if self.customer.number == "":
                self.display_error()
                continue
                
            if self.customer_display(self.customer.number):
                self.display_screen()
                break
        
        while True:
            print("Enter Product ID: ", end="")
            self.product.number = input()
            
            if self.product.number == "":
                self.display_error()
                continue
                
            if self.product_display(self.product.number):
                self.display_screen()
                break
                
        return True

    def save_order(self):
        """Save order to database - not implemented in original code"""
        # Would implement order saving logic here
        print("Order saved successfully!")
        input("Press Enter to continue...")

    def run(self):
        """Main program execution flow"""
        running = True
        while running:
            self.init_vars()
            self.display_screen()
            
            if not self.get_user_input():
                break
                
            # Handle command options
            while True:
                command = input("Enter command (S-Save, X-Exit): ").upper()
                if command == 'X':
                    running = False
                    break
                elif command == 'S':
                    self.save_order()
                    break
                else:
                    self.display_error()
                    
        print("Program terminated.")


if __name__ == "__main__":
    app = OrderEntrySystem()
    app.run()