contacts = [
("Mohamed Gouda", "+1-555-555-5555",
"mohamedgouda@example.com"),
("Amira Abdelrahman", "+1-555-555-5556",
"amiraabdelrahman@example.com"),
("Abdullah Othman", "+1-555-555-5557",
"abdullahothman@example.com"),
("Ahmed Saeed", "+1-555-555-5558",
"ahmedsaeed@example.com"),
("Saleh Abdelhamid", "+1-555-555-5559",
"salehabdelhamid@example.com"),
("Fatima Ali", "+1-555-555-5560", "fatimaali@example.com"),
("Omar Hasan", "+1-555-555-5561", "omarhasan@example.com"),
("Aisha Ahmed", "+1-555-555-5562",
"aishaahmed@example.com"),
("Karim Hassan", "+1-555-555-5563",
"karimhassan@example.com")
]
while True:
  print("welcom to the phonbook application!")
  print("1. Add a contact")
  print("2. Updat a contact")
  print("3. Sarch for a contact ")
  print("4. Quit ")

  choise = int(input("Enter your choise: "))

  if choise == 1:
    nam = input("Enter name: ")
    phon = input("Enter phon number: ")
    email = input("Enter email: ")
    contacts.append((nam, phon, email))
    print("Contact added successfully")

  elif choise == 2:
    nam = input("Enter name of the contact you want to update: ")
    for i in range(len(contacts)):
      if contacts[i][0].lower() == nam.lower():
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[i] = (nam, phon, email)
        print("Contact updated successfully.")
        break
    else:
        print("Contact not found.")

  elif choise == 3:
    name = input("Enter name of the contact you want to search: ")
    for contact in contacts:
      if contact[0].lower() == name.lower():
        print(f"Name: {contact[0]}")
        print(f"Phone number: {contact[1]}")
        print(f"Email: {contact[2]}")
        break

    else:
        print("Contact not found.")


  elif choise == 4:
    break

  else:
    print("Invalid choice.")

  print("-"*20)