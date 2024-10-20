# print treatment information
inventory = {"Paracetamol": {"price":25, "quantity":10},
"Aspirin": {"price":15, "quantity":20},
"Ibuprofen": {"price":20, "quantity":15},
"Cough Syrup": {"price":30, "quantity":5},
"Augmentin": {"price":100, "quantity":7},
"Amoxicillin": {"price":80, "quantity":8},
"Panadol": {"price":25, "quantity":10},
"Zinc": {"price":15, "quantity":20},
"Vitamin C": {"price":20, "quantity":15},
"Fucidin": {"price":30, "quantity":5},
"Kolanog": {"price":100, "quantity":2},
}

# dictionary to store items
neu_invintory = {}

# options
options ="""1. Add neu items
2. Remove items
3. Update items
4. chik Avalibale quantity
5. print treatment information
6. Exit
"""
# get items from the user
while True:
  
# print the options
  print(options)

# get the user choice
  choice = input("Enter your choice: ")

# if the user choose to add new items
  if choice == "1":
    
    # get items from the user
     while True:
       print("---Entering new item---")
       item = input("Enter item name (press Enter to Exit): ").title()
       if item == "":
          break
       price = float(input("Enter item price: "))
       quantity = input("Enter item quantity: ")
       neu_invintory[item] = {"price": price, "quantity": quantity }
       
# add new items to the inventory
     inventory = {**inventory, **neu_invintory}

# if the user choose to remove items
  elif choice == "2":
    
# get items from the user
    while True:
      print("---Deleting item---")
      item = input("Enter item name to be deleted (press Enter to Exit): ").title()
      if item == "":
        break
      sure = input("Are you sure you want to delete Panadol? (y/n): ")
      if sure == "y":
        inventory.pop(item)
        print(f"{item} has been deleted")
      else:
        continue

# if the user choose to update items
  elif choice == "3":
    
# get items from the user
    while True:
      print("___Updating item___")
      item = input("Enter item name to be deleted (press Enter to Exit): ").title()
      
      if item == "":
        break
      if item in inventory:
        price = float(input("Enter item price: "))
        quantity = input("Enter item quantity: ")
        neu_invintory[item] = {"price": price, "quantity": quantity }
        inventory.update(neu_invintory)
        print(f"{item} has been updated")
      else:
        print("Item not fuond")

# if the user choose to check the quantity of items
  elif choice == "4":
    while True:
      print("---Checking item quantity---")
      item = input("Enter item name to be deleted (press Enter to Exit): ").title()
      if item == "":
        break
      
# if the item is in the inventory, print the quantity
      if item in inventory:
       print(f"We have {inventory[item]['quantity']} {item} units")
      else:
        print("Item not fuond")
# if the user choose to print treatment information
  elif choice == "5":
    while True:
      print("---Printing treatment information---")
# get items from the user
      item = input("Enter item name to be deleted (press Enter to Exit): ").title()
      if item == "":
       break
      if item in inventory:
        item_info =f"""Item: {item}
price: {inventory[item]['price']}$
quantity: {inventory[item]['quantity']} units
"""
        print(item_info)
      
# if the user choose to exit
  elif choice == "6":
    break
# if the user choose an invalid option
  else:
    print("Invalid option")
# print message to the user
print("Have a nice day! ")