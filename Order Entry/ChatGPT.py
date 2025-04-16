# Author: Usama Husain
# Date  : 10-10-2024
# Ticket: --

# ========== INITIALIZATION ==========
def open_files():
    # TODO: Implement file opening if needed
    return

def init_vars():
    global cust_no, cust_name, cust_date, curr_bal, amt_due
    global prod_no, prod_price, prod_qty, prod_name, prod_features
    global client_no, client_name, order_no, order_qty, order_price, order_date
    global company, address, phone_no

    cust_no = "##############"
    cust_name = ""
    cust_date = "DD/MM/YYYY"
    curr_bal = ""
    amt_due = ""
    prod_no = "############"
    prod_price = ""
    prod_qty = ""
    prod_name = ""
    prod_features = ""
    client_no = "############"
    client_name = ""
    order_no = "############"
    order_qty = ""
    order_price = ""
    order_date = "DD/MM/YYYY"
    company = ""
    address = ""
    phone_no = ""

# ========== DISPLAY SCREEN ==========
def display_scr():
    print("*" * 100)
    print("*" + " " * 40 + "ORDER ENTRY SCREEN" + " " * 40 + "*")
    print("*" * 100)
    print(f"CUST#: {cust_no:<40} CUSTOMER NAME: {cust_name:<25} Date: {cust_date:<10}")
    print(f"CURR BALANCE: {curr_bal}")
    print(f"AMT DUE     : {amt_due}")
    print("*" * 100)
    print(f"PRODUCT: {prod_no:<38} PRICE: {prod_price:<29} QUANTITY: {prod_qty:<10}")
    print(f"PRODUCT NAME: {prod_name}")
    print(f"FEATURES    : {prod_features}")
    print("*" * 100)
    print(f"CLIENT NO : {client_no:<63} NAME: {client_name:<20}")
    print(f"ORDER     : {order_no:<34} QTY: {order_qty:<36} PRICE: {order_price:<10}")
    print(f"ORDER DATE: {order_date}")
    print(f"COMPANY   :  {company}")
    print(f"ADDRESS   :  {address}")
    print(f"PHONE NO  :  {phone_no}")
    print("*" * 100)
    print("OPTIONS: F-Save, X-Exit")
    print("*" * 100)

# ========== ERROR HANDLING ==========
def display_error():
    print("Invalid Input value")

# ========== CUSTOMER DISPLAY ==========
def cust_display():
    global cust_name, cust_date, curr_bal, amt_due

    try:
        # Simulate file access
        # Example: open file and read by cust_no key
        with open("CUSTOMER.txt", "r") as f:
            # TODO: Parse file for record matching cust_no
            pass
        # Example fields:
        # cust_name = record[0]
        # cust_date = convert_date(record[7])
        curr_bal = ""
        amt_due = ""
        display_scr()
    except Exception:
        display_error()
        get_user_input()

# ========== PRODUCT DISPLAY ==========
def prod_display():
    global prod_price, prod_qty, prod_name, prod_features

    try:
        # Simulate file access
        # Example: open file and read by prod_no key
        with open("INVENTORY.txt", "r") as f:
            # TODO: Parse file for record matching prod_no
            pass
        # Example assignments:
        # prod_price = record[6]
        # prod_qty = record[5]
        # prod_name = record[2]
        # prod_features = record[3]

        print(f"{prod_no:<38} {prod_price:<29} {prod_qty:<10}")
        print(prod_name)
        print(prod_features)
        # Optionally refresh screen:
        # display_scr()
    except Exception:
        display_error()
        get_user_input()

# ========== INPUT ROUTINE ==========
def get_user_input():
    global cust_no, prod_no

    while True:
        try:
            cust_no = input("Enter Customer ID: ").strip()
            if cust_no.upper() == "END":
                return
            if cust_no == "":
                display_error()
                continue
            cust_display()
            break
        except Exception:
            display_error()

    while True:
        try:
            prod_no = input("Enter Product ID: ").strip()
            if prod_no == "":
                display_error()
                continue
            prod_display()
            break
        except Exception:
            display_error()

# ========== MAIN ==========
def main():
    init_vars()
    display_scr()
    get_user_input()
    # Optionally: save_order()

main()
