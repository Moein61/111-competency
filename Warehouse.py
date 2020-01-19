from menu import print_menu
from item import Item 
import datetime
import pickle
import os

logs = []
items = []
id_count= 1 
items_file = "item.data"
logs_file= "logs.data"

def clear():
    return os.system("cls") 

def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time


def save_items(): 
    writer = open(items_file, "wb")
    pickle.dump(items, writer)
    writer.close()
    print("Data Saved!")

def save_log():
    writer = open(logs_file, "wb")
    pickle.dump(logs, writer)
    writer.close()
    print("Log saved!!")

def read_items():
    global id_count

    try: 
        reader = open(items_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            items.append(item)
        
        last = items[-1]
        id_count = last.id + 1 
        print("Loaded:" + str(len(temp_list)) + "items")
    except:
        print("ERROR: Data could not be loaded")


def read_log(): 
    try:
        reader = open(logs_file, "rb")
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)
        
        print("Loaded: " + srt(len(temp_list)) + "log events")

    except:
        print("Error: Data could not be loaded")

    

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):

    print_header(header_text)
    print("-" * 70)
    print("ID | Item Title  |Category |Price |Stock")
    print("-" * 70)

    for item in items: 
        print(str(item.id).ljust(3) + "|" + item.title.ljust(25) + "|" + item.category.ljust(15) + "|" + str(item.price).rjust(9)+"|" + str(item.stock).rjust(5))




def register_item():

    global id_count

    print_header("register new item")
    title = input("please input the title")
    category = input ("please input the Category: ")
    price = float(input("please input the Price: "))
    stock = int(input("please input the stock: "))


    new_item = Item()
    new_item.id = id_count
    new_item.title = title 
    new_item.category = category
    new_item.price = price
    new_item.stock= stock

    id_count += 1
    items.append(new_item)
    print("Item Created!") 

def update_stock():
    print_all ("Choos an Item from the list ")
    id = input("\nSelect an ID to update its stock: ")
    found = False
    for item in items : 
        if(str(item.id) == id) :
            stock = input("please input new stock value: ")
            item.stock = int(stock)
            found = True

            log_line = get_time() + " | update |" + id
            logs.append(log_line)
            save_log()
    if(not found) : 
        print("** error: ID doesn't exist, try again ")       

def remove_item():
    print_all("Chose and Item to Remove")
    id = input("\nSelect and ID to remove it: ")

    for item in items : 
        if(str(item.id) == id):
            items.remove(item)
            print(" Item has been removed!")
    
def list_no_stock() :
    print_header("Items with no stock")
    for item in items:
        if(item.stock == 0):
            print(item.title)

def print_categories() : 
    temp_list = []

    for item in items:
        if(item.category not in temp_list):
            temp_list.append(item.category)
    print(temp_list)

def register_purchase():

    print_all("Choose an Item that yo purchased")
    id = input("\nSelect an ID to update its stock: ")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many items: ")
            item.stock += int(stock)
            found = True

    if(not found):
        print("** Error: ID doesn't exist, try again") 

def register_sell():

    print_all("Choose an item that you sold")
    id = input("\nSelect an ID to update its stock: ")
    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many items: ")
            item.stock -= int(stock)
            found = True

    if(not found):
        print("** Error: ID doesn't exist, try again")

def print_stock_value() : 
    total = 0.0
    for item in items: 
        total += (item.price * float(item.stock))

    print("Total Stock Value: " + str(total))
read_items()
read_log()

opc = ''

while(opc != 'x'): 
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        print_all("List of all Items")
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "5"):
        remove_item()
        save_items()
    
    elif(opc == "6"):
        print_categories()
    elif(opc == "7"):
        print_stock_value()
    elif(opc == "8"):
        register_purchase()
    elif(opc == "9"):
        register_sell()
    elif(opc == "10"):
        read_log()

    if(opc != "x"):
        input("\n\nPress Enter to continue...")

