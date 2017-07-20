import csv
import code
csv_file_path = "../data/products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

def list_products():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            print(row["id"],row["name"],row["aisle"],row["department"],row["price"])

def show_products():
    print('''This is showing all the products!
    \n
    ---------------------------
    \n''')

def create_products():
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)

def update_products():
    print('''Woahhhhh, Updates?!
    \n
    ---------------------------
    \n''')

def destroy_products():
    print('''You are a destroyer of worlds.
    \n
    ---------------------------
    \n''')

def handler(selection):
    if selection=="list":
        return list_products()
    elif selection=="show":
        return show_products()
    elif selection=="create":
        return create_products()
    elif selection=="update":
        return update_products()
    elif selection=="destroy":
        return destroy_products()
    else:
        print("Well that doesn't seem right. You sure?\n\n")

directions = ('''There are {0} products in the database. Please select an operation:

operation | description
--------- | -----------
'List'    | Display a list of product identifiers and names.
'Show'    | Show information about a products.
'Create'  | Add a new product.
'Update'  | Edit an existing product.
'Destroy' | Delete an existing product.''').format(len(products))

print(directions)

x=0
while x == 0:
    user_input = input("\n\nPlease select an operation: ")
    user_input = user_input.lower()
    try:
        if user_input.lower() == "done":
            break
        elif user_input != "done":
            handler(user_input)
    except ValueError:
        print("Sorry, that input doesn't seem correct. Try again!")


#code.interact(local=locals())
