# Modernized Order Entry Program in Python

# Author: Usama Husain
# Date: 2025-04-16
# Ticket: --

class OrderEntryData:
    def __init__(self):
        self.cust_no = "##############"
        self.cust_name = ""
        self.cust_date = "DD/MM/YYYY"
        self.curr_bal = ""
        self.amt_due = ""
        self.prod_no = "############"
        self.prod_price = ""
        self.prod_qty = ""
        self.prod_name = ""
        self.prod_features = ""
        self.client_no = "############"
        self.client_name = ""
        self.order_no = "############"
        self.order_qty = ""
        self.order_price = ""
        self.order_date = "DD/MM/YYYY"
        self.company = ""
        self.address = ""
        self.phone_no = ""

def initialize_variables(data: OrderEntryData):
    data.cust_no = "##############"
    data.cust_name = ""
    data.cust_date = "DD/MM/YYYY"
    data.curr_bal = ""
    data.amt_due = ""
    data.prod_no = "############"
    data.prod_price = ""
    data.prod_qty = ""
    data.prod_name = ""
    data.prod_features = ""
    data.client_no = "############"
    data.client_name = ""
    data.order_no = "############"
    data.order_qty = ""
    data.order_price = ""
    data.order_date = "DD/MM/YYYY"
    data.company = ""
    data.address = ""
    data.phone_no = ""

def display_screen(data: OrderEntryData):
    print("\033[H\033[J", end="")  # Clear screen (simulated)
    print("-" * 100)
    print(f"* {'ORDER ENTRY SCREEN':^98} *")
    print("-" * 100)
    print(f"CUST#: {data.cust_no:<40} CUSTOMER NAME: {data.cust_name:<25} Date: {data.cust_date:<10}")
    print(f"CURR BALANCE: {data.curr_bal}")
    print(f"AMT DUE        : {data.amt_due}")
    print("-" * 100)
    print(f"PRODUCT: {data.prod_no:<38} PRICE: {data.prod_price:<29} QUANTITY: {data.prod_qty:<10}")
    print(f"PRODUCT NAME: {data.prod_name}")
    print(f"FEATURES     : {data.prod_features}")
    print("-" * 100)
    print(f"CLIENT NO : {data.client_no:<63} NAME: {data.client_name:<20}")
    print(f"ORDER     : {data.order_no:<34} QTY: {data.order_qty:<36} PRICE: {data.order_price:<10}")
    print(f"ORDER DATE: {data.order_date}")
    print(f"COMPANY   :  {data.company}")
    print(f"ADDRESS   :  {data.address}")
    print(f"PHONE NO  :  {data.phone_no}")
    print("-" * 100)
    print("OPTIONS: F-Save, X-Exit")
    print("-" * 100)

def get_user_input(data: OrderEntryData):
    while True:
        data.cust_no = input("Enter Customer Number: ").strip()
        if data.cust_no.upper() == "END":
            return False
        if not data.cust_no:
            display_error("Invalid Input value")
            continue
        display_customer(data, data.cust_no)
        break  # Proceed after (simulated) customer display

    while True:
        data.prod_no = input("Enter Product ID: ").strip()
        if not data.prod_no:
            display_error("Invalid Input value")
            continue
        display_product(data, data.prod_no)
        break  # Proceed after (simulated) product display
    return True

def display_error(message: str):
    print(f"Error: {message}")

def display_customer(data: OrderEntryData, customer_id: str):
    # Simulate file open and read
    # In a real embedded system, this would involve actual file/database access
    customer_record = get_customer_record(customer_id)
    if customer_record:
        data.cust_name = customer_record[0]
        data.cust_date = format_date(customer_record[7])
        data.curr_bal = ""  # Not directly available in the simulated record
        data.amt_due = ""    # Not directly available in the simulated record
        display_screen(data)
    else:
        display_error(f"Customer with ID '{customer_id}' not found.")
        get_user_input(data) # Go back to input

def get_customer_record(customer_id: str):
    # This is a placeholder for actual data retrieval
    # In a real system, this would read from a file or database
    if customer_id == "12345678901234":
        return ["John Doe", "", "", "", "", "", "", "20241010"]
    return None

def format_date(date_str: str):
    if len(date_str) == 8 and date_str.isdigit():
        return f"{date_str[6:]}/{date_str[4:6]}/{date_str[:4]}"
    return "DD/MM/YYYY"

def display_product(data: OrderEntryData, product_id: str):
    # Simulate file open and read
    # In a real embedded system, this would involve actual file/database access
    product_record = get_product_record(product_id)
    if product_record:
        data.prod_price = product_record[6]
        data.prod_qty = product_record[5]
        data.prod_name = product_record[2]
        data.prod_features = product_record[3]
        print(f"Product ID: {data.prod_no:<38} Price: {data.prod_price:<29} Quantity: {data.prod_qty:<10}")
        print(f"Product Name: {data.prod_name}")
        print(f"Features    : {data.prod_features}")
    else:
        display_error(f"Product with ID '{product_id}' not found.")
        get_user_input(data) # Go back to input

def get_product_record(product_id: str):
    # This is a placeholder for actual data retrieval
    # In a real system, this would read from a file or database
    if product_id == "ABC1234567890":
        return ["", "", "Awesome Product", "Great Features", "", "10", "25.99"]
    return None

if __name__ == "__main__":
    order_data = OrderEntryData()
    initialize_variables(order_data)
    display_screen(order_data)
    get_user_input(order_data)
    # The "SAVE.ORDER" functionality would be implemented here
    # based on the collected data in the 'order_data' object.