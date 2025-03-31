#!/usr/bin/env python3

import pprint

print("\nSimple Inventory Management System\n")

inventory = {}

while True:
    print("\nOptions:")
    print("1. View items")
    print("2. Add item")
    print("3. Update quantity")
    print("4. Calculate total inventory value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print('\nInventory:')
        pprint.pprint(inventory)

    elif choice == '2':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        
        inventory[name] = {'price': price, 'quantity': quantity}
        print(f"{quantity} {name}(s) added to inventory")

    elif choice == '3':
        name = input("Enter item name to update: ")
        if name in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[name]['quantity'] = quantity
            print(f"{name} quantity updated to {quantity}")
        else:
            print("Item not found in inventory")

    elif choice == '4':
        total_value = sum(item['price'] * item['quantity'] for item in inventory.values())
        print(f"Total inventory value: ${total_value:.2f}")

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")

print("\nFinal Inventory:")
for name, details in inventory.items():
    print(f"{name}: ${details['price']} x {details['quantity']}")
    
total_value = sum(item['price'] * item['quantity'] for item in inventory.values())
print(f"Total value: ${total_value:.2f}")
