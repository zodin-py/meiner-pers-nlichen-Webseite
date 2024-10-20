# available items
pizzas = {"Margherita": 100, "Pepperoni": 120,
"Meat Lovers": 150, "Chicken": 130}
burgers = {"Beef": 100, "Chicken": 80, "Bacon": 120}
drinks = {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30}
soups = {"Chicken Soup": 50, "Beef Soup": 60,
"Mushroom Soup": 40}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60,
"Cheese Cake": 70}

order = []

while True:
  print("Welcome to Zodin Restuarant ")
  # invald all dict to oun dict
  menu = {"Pizzas" : pizzas, "Burgers" : burgers, 
  "Drinks": drinks,"Soups" :   soups, "Desserts": 
  desserts}
  
  # print the items withe numbers
  for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")

# get the user choice if his choice == "" break
  user_choice = input("Pleas, Enter the number of   your choic (Enter to Exit): ")
  if user_choice == "":
    break

  # print the user choice info
  user_choice = int(user_choice)
  user_choice_info = list(menu.values())[user_choice - 
  1]
  for i, (item, price) in enumerate( 
  user_choice_info.items(), 1):
    print(f"{i}. {item}: {price}€")

  # get the order name from the user if he presse 0 continue
  order_nam = int(input("Pleas, Enter the number of the item you want (0 to return to the previous menu): "))
  if order_nam == 0:
     continue
  # get the quantity
  order_quantity = int(input("Pleas, Enter the quantity: "))
  order_price = list(user_choice_info.values())[order_nam - 1] * order_quantity

  # append the info to order
  order.append({"Item": list(user_choice_info.keys())[order_nam - 1], "Quantity": order_quantity, "Price": 
  order_price})    
  print("Order added successfully.")
  
  # print the masseg
  masseg = """1. Add anther item
2. viw the order
3. Cleat the order
4. Exit  
"""
  print(masseg)

  # get the user choice
  choice = input("Pleas, Enter your choice: ")

  # if the user choice == 1 continue
  if choice == "1":
    continue

 # if user choice == 2 viwo the order
  elif choice == "2":
      print("Your order is:")
      total_price = 0  
      for item in order:
          choice_info = list(menu.keys())[user_choice - 1]
          order_message = f"Item: {item['Item']}{choice_info} \nPrice: {item['Price']}\nQuantity: {item['Quantity']}"
          total_item = item["Price"] * item["Quantity"]
          total_price += total_item  
          print("-" * 20)
          print(order_message)
          print("_" * 20)
          print(f"Total item: {total_item:.2f}")
          print("_" * 20)
      print(f"Total price: {total_price:.2f}") 
 # if user choice == 3 dilt avry thing in the order
  elif choice == "3":
    order = []
    print("Order clear...")

  # if user choice == 4 break
  elif choice == "4":
    print("Thank you for Zodin restorant visting")
    break