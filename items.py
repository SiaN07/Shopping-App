import sys

def main():
    while True:
        print()
        print(''' ### PLEASE SELECT ANY OF THE FOLLOWING ### 
        1. Place an Order
        2. Cancel the Order
        3. View Cart
        4. View Orders
        5. Exit
        ''')

        option = input('Please choose option: ')

        # Place an order
        if option == "1":
            displayCatalog()
            addItem()
            viewCart()
        elif option == "2":
            viewCart()
            removeItem()
        elif option == "3":
            viewCart()
        elif option == "4":
            viewOrder()
        elif option == "5":
            sys.exit()
        else:
            print('You did not make a valid selection')

catalog_list = {
    "Kabras Sugar": 10,
    "Ajab Flour"   : 10,
    "Kimbo Oil"    : 8,
    "Ketepa "    : 14,
    "Nescafe"    : 28,
    "Dawat Rice"    : 10,
    "Chocolate"    : 16,
    "Onions"    : 33,
    "Tomatoes"    : 29,
    "Royco Cubes"    :55,

}
shopping_cart = {

}
order_list = {

}

def displayCatalog():
    totalItems = len(catalog_list)
    count=0
    lessItems = False
    for item in catalog_list:
        count += 1
        if totalItems >= 7:
            print( f"{count}. Item: {item} \t  Qty : {catalog_list[item]}" )
        else:
            lessItems = True
    if lessItems:
        print("Sorry, there are no enough items in the catalog to place an order")       
        sys.exit()
    return totalItems

def addItem():
    optionItem = int(input("What would you like to Order? : "))
    optionValue = optionItem-1
    totalItems = len(catalog_list)
    
    if optionValue<=totalItems:
        selectedItem = list(catalog_list.keys())[optionValue]
    else:
        print("You have not made a valid selection")
        return

    if selectedItem in shopping_cart:
        print("Item already in cart")
        qty = int(input("How many items of " + selectedItem +" would you like to order? : "))
        if qty > catalog_list[selectedItem]:
             print(f"That quantity is greater that the available stock of {catalog_list[selectedItem]}  {selectedItem}")
             return             
        else:
           shopping_cart[selectedItem] =shopping_cart[selectedItem] + qty   
    else:
        qty = int(input("How many items of " + selectedItem +" would you like to order? : "))
        if qty > catalog_list[selectedItem]:
             print(f"That quantity is greater than the available stock of {catalog_list[selectedItem]}  {selectedItem}")
             return             
        else:
            shopping_cart[selectedItem] = qty
   
    catalog_list[selectedItem] =catalog_list[selectedItem] -qty
    print(f"{qty} {selectedItem} has been ordered")

    

def removeItem():
    optionItem = int(input("What item would you like to remove? : "))
    optionValue =optionItem-1
    totalItems = len(shopping_cart)
    if optionValue <= totalItems:
        selectedItem = list(shopping_cart.keys())[optionValue]
    else:
        print("You have not made a valid selection") 
        return

    if selectedItem in shopping_cart:
        qty = int(input("How many items of " + selectedItem +" would you like to remove? : "))
        if shopping_cart[selectedItem] < qty:
            print("That quantity is greater that the one in the cart")
        else:
            shopping_cart[selectedItem] = shopping_cart[selectedItem] - qty 
            print("You have removed " + selectedItem + " from your cart") 
            
    catalog_list[selectedItem] =catalog_list[selectedItem] + qty
    print(f"{qty} {selectedItem} has been removed")
    
def viewCart():
    if len(shopping_cart) > 0:
        count = 0
        print("Your cart has been updated ")
        for item in shopping_cart:
            count += 1
            if shopping_cart[item] == 0 and len(shopping_cart) == 0 :
                print("You have removed " + item + " from the cart")
            else:
                print( f"{count}. Item: {item} \t  Qty : {shopping_cart[item]}" )
    else: 
        print("Your cart is empty. Please place an order")

    return len(shopping_cart)
         
def viewOrder():
    order_list = shopping_cart.copy()
    if len(order_list) > 0:
        count = 0
        print("This is your order")
        for item in order_list:
            count += 1
            print( f"{count}. Item: {item} \t  Qty : {order_list[item]}" )
            
        print("To confirm your order, press 1")
        option = input()
        
        if option == "1":
            print("Your order has been placed. The delivery will be done within 2 days. Payment will be made on delivery")
            sys.exit()
        else:
            print("Your order has not been placed.")
            
            
    else: 
        print("Your order is empty. Please place an order")


        
main()

