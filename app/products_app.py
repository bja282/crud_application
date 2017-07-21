import csv
import code
csv_file_path = "../data/products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])

# The List operation should print information (identifiers and names at least) about each product
# in the inventory.
def list_products():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            print(row["id"],row["name"],row["aisle"],row["department"],row["price"])

# The Show operation should prompt the user for a product identifier. If the product
# identifier matches the identifier of an existing product in the inventory, the program
# should print all available information about that product.
def show_products():
    product_key = input("Please enter the id of the product you would like to view: ")
    if int(product_key) <= len(products):
        first_q = input("You selected \"{0}".format(products[int(product_key)-1]["name"]) + "\". Is that correct? (Enter yes or no) ")
        if first_q.lower() == "yes":
            print("\n")
            for key, value in products[int(product_key)-1].items():
                print(str(key)+":"+str(value))
        else: pass
    else:
        print("Sorry, that product key appears incorrect.")

# The Create operation should prompt the user to input a new product's "name", "department", "aisle"
# and "price", and should automatically determine the new product's "id" by adding 1 to the greatest
# identifier currently in the inventory. Then the program should save the new product's information by
# adding a new row at the bottom of the CSV file.
def create_products():
    new_product = dict.fromkeys(["id", "name", "aisle", "department", "price"])
    new_id = len(products)+1
    new_product["id"]=new_id
    new_name = input("Please enter a product name: ")
    new_product["name"]=new_name
    new_aisle = input("Which aisle is the product in? ")
    new_product["aisle"]=new_aisle
    new_dept = input("Which department is the product in? ")
    new_product["department"]=new_dept
    new_price = input("What is the price of the item? ")
    new_product["price"]=new_price

    print(new_product)

    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)
        writer.writerow(new_product)

    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        products.append(new_product)

# The Update operation should prompt the user for a product identifier.
# If the product identifier matches the identifier of an existing product in the inventory,
# the program should prompt the user to input new values for that product's "name", "department",
# "aisle" and "price" attributes, and overwrite that product's corresponding row in the CSV file.
def update_products():
    product_key = input("Please enter the id of the product you would like to change: ")
    if int(product_key) <= len(products):
        first_q = input("You selected \"{0}".format(products[int(product_key)-1]["name"]) + "\". Is that correct? (Enter yes or no) ")
        if first_q.lower() == "yes":
            new_name = input("Please enter a product name: ")
            new_aisle = input("Which aisle is the product in? ")
            new_dept = input("Which department is the product in? ")
            new_price = input("What is the price of the item? ")
            products[int(product_key)-1]={
            'id': product_key,
            "department": new_dept,
            "aisle": new_aisle,
            "name": new_name,
            "price": new_price}
            print("Thank you,",new_name,"has been updated.")

    else:
        print('Sorry, that product key doesn\'t appear correct.')

# The Destroy operation should prompt the user for a product identifier.
# If the product identifier matches the identifier of an existing product in the inventory,
# the program should display a helpful message and remove that product's corresponding row from the CSV file.
def destroy_products():
    product_key = input("Please enter the id of the product you would like to delete: ")
    if int(product_key) <= len(products):
        first_q = input("You selected \"{0}".format(products[int(product_key)-1]["name"]) + "\". Is that correct? (Enter yes or no) ")
        if first_q.lower() == "yes":
            print("Thank you,",products[int(product_key)-1]["name"],"has been deleted.")
            del products[int(product_key)-1]
    else:
        print('Sorry, that product key doesn\'t appear correct.')

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
'Destroy' | Delete an existing product.\n
You may exit the program at any time by entering "done."''').format(len(products))

print(directions)

x=0
while x == 0:
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for product in products:
            writer.writerow(product)
    user_input = input("\n\nPlease select an operation: ")
    user_input = user_input.lower()
    try:
        if user_input.lower() == "done":
            break
        elif user_input != "done":
            handler(user_input)
    except ValueError:
        print("Sorry, that input doesn't seem correct. Try again!")
