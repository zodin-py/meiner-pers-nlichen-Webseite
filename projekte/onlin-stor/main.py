# dictionary of available items with their prices and quantity
items = {
'iPhone 13': {'price': 1000, 'quantity': 10},
'MacBook Pro': {'price': 2000, 'quantity': 5},
'AirPods Pro': {'price': 250, 'quantity': 2},
'iPad Pro': {'price': 800, 'quantity': 15},
'Apple Watch Series 7': {'price': 600, 'quantity': 3},
}
cart = []
# 1. mein 
def mein():
  print("Welcome to codetilla Store!")
  while True:
  # a) print a massege
    masseg ='''Available options:
1. View Acalilable Items
2. View Cart
3. Total Cart price
4. Clear Cart
5. Quit
'''
    print(masseg)
  # b) get a input choice
    choice = input("Enter the number of your choice: ")
  # c) if choice == "1":
    if choice == "1":
      view_available_items(items)
  # d) elif choice == "2":
    elif choice == "2":
      view_cart(cart)
  # e) elif choice == "3":
    elif choice == "3":
      total_cart_price(cart)
  # f) elif choice == "4":
    elif choice == "4":
       clear_cart(cart)
  # g) elif choice == "5":
    elif choice == "5":
      print("Thank you fo shopping at Codetilla Store!")
      view_cart(cart)
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
      
def view_available_items(items):
    # Display available items
    for i, (item_name, item_details) in enumerate(items.items(), 1):
      item_quantity = items[item_name]['quantity']
      if item_quantity == 0:
        print(f"{i}. {item_name}: {item_details['price']}€ (Not Available)")
      print(f"{i}. {item_name}: {item_details['price']}€")
    # Get the item number
    while True:
        try:
            item_num = int(input("Number of the item to purchase (Enter 0 to return to previous menu): "))
            if item_num == 0:
                return
            elif item_num < 1 or item_num > len(items):
                print("Invalid item number!")
            else:
                break
        except ValueError:
            print("Please enter a anumber.")

    item_name = list(items.keys())[item_num - 1]
    item_quantity = items[item_name]['quantity']

    if item_quantity < 1:
        print("Sorry, this item is not available.")
        return

    print(f"Available items: {item_quantity}")
    order_quantity = int(input("Please enter the quantity: "))

    if order_quantity > item_quantity:
        print(f"Sorry, we only have {item_quantity} of this item.")
        return

    # Subtract the ordered quantity from the available quantity
    items[item_name]['quantity'] -= order_quantity

    # Construct order information
    order_price = items[item_name]['price']
    order_info = {"Item name": item_name, "Item price": order_price, "Quantity": order_quantity}
    cart.append(order_info)
    print(f"{item_name} has been added to the cart successfully.")
   
# 3. view cart
def view_cart(cart):
  if cart:
    print("Cart:")
    print("-" * 30)
    for item in cart:
        item_nam = item["Item name"]
        pric = item["Item price"]
        quantity = item["Quantity"]
        total_price = pric * quantity
        print(f"{item_nam}: {pric}€ x {quantity} = {total_price:,.2f}")
    print("-" * 30)
    total_cart_price(cart)
  else:
    print("No items have been bught.")

# 4. view total cart
def total_cart_price(cart):
  total_price = sum(item['Item price'] * item['Quantity'] for item in cart)
  print("-" * 30)
  print(f"Total Cart Price: {total_price:.2f}€")
  
# 5. clear cart price
def clear_cart(cart):
  print("Items in the cart befor your clearing it:")
  view_cart(cart)
  sur_input = input("Are you sure you want to clear the cart? (y/n):")
  if sur_input == "y":
    cart.clear()
    print("cart has been clered.")
  elif sur_input == "n":
    return
  else:
    print("Invald input please enter (y/n).")
    return sur_input
mein()


