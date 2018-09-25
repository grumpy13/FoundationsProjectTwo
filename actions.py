# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.VIBES.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for s in stores:
        print ("* " + s.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for s in stores:
        if s.name == store_name:
            return s
        
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    choice = input("Pick a store by typing its name or type 'checkout' to pay your bill: \n")

    while choice != "checkout":

        for s in stores:
            if choice.lower() == s.name.lower():
                return s
            
        print ("No store with that name. Please try again.")
        
        choice = input()

    return choice


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print ()
    print (picked_store.name + ": ")
    print ()
    picked_store.print_products()

    choice = input("Pick an item by typing its name exactly as its shown above or type 'back' to go back to the main menu: \n")

    while choice != "back":

        for p in picked_store.products:

            if choice.lower() == p.name.lower():
                cart.add_to_cart(p)
                
        choice = input()
            
            

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    s = pick_store()
    while s != "checkout":
        pick_products(cart, s)
        s = pick_store()
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
