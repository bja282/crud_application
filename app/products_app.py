# Checkpoint I - User Inputs
#
# 1. Print a menu which contains a greeting message and a hard-coded number of products and a list of available operations.

# 2.  Using the aforementioned menu, prompt the user to choose one of the available operations, and print the name of the chosen operation.

# 3. Implement a single "handler" function to recognize the chosen operation and invoke one of a handful of new operation-specific
#functions to perform the chosen operation. For example, if the user chooses "Create", have your "handler" function invoke a function
#called create_product() to print the name of the chosen operation.

# 4. Handle invalid operation inputs by displaying a helpful message like "Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'."

def list_products():
    print("This is a list of all the products!")

def show_products():
    print("This is showing all the products!")

def create_products():
    print("Wow, you made a new product.")

def update_products():
    print("Woahhhhh, Updates?!")

def destroy_products():
    print("You are a destroyer of worlds.")

def handler(input):
    if input.lower()=="list":
        return list_products()
    elif input.lower()=="show":
        return show_products()
    elif input.lower()=="create":
        return create_products()
    elif input.lower()=="update":
        return update_products()
    elif input.lower()=="destroy":
        return destroy_products()
    else:
        print("Well that doesn't seem right. You sure?")

directions = ('''There are 20 products in the database. Please select an operation:

operation | description
--------- | -----------
'List'    | Display a list of product identifiers and namesself.
'Show'    | Show information about a productself.
'Create'  | Add a new product.
'Update'  | Edit an existing product.
'Destroy' | Delete an existing product.''')

input = input(directions +  "\n\nPlease select an operation: ")
handler(input)
