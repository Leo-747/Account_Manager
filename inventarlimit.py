import json
Account = {
    "Inventory": [],
    "Coins": 1000
}

def items(selection):
    if len(Account["Inventory"]) < 5:
        if selection == "star":
            if Account["Coins"] < 50:
                print(f"Not enough coins! You need {50 - Account['Coins']} more.")
            else:
                price = 50
                Account["Inventory"].append(selection)
                Account["Coins"] -= price
                print(f"Successfully bought! Current balance: {Account['Coins']} coins.")
        elif selection == "shell":
            if Account["Coins"] < 30:
                print(f"Not enough coins! You need {30 - Account['Coins']} more.")
            else:
                price = 30
                Account["Inventory"].append(selection)
                Account["Coins"] -= price
                print(f"Successfully bought! Current balance: {Account['Coins']} coins.")
        elif selection == "block":
            if Account["Coins"] < 10:
                print(f"Not enough coins! You need {10 - Account['Coins']} more.")
            else:
                price = 10
                Account["Inventory"].append(selection)
                Account["Coins"] -= price
                print(f"Successfully bought! Current balance: {Account['Coins']} coins.")
        else:
            print("Item not in stock.")
    elif len(Account["Inventory"]) == 5:
        print("Your inventory is full!")

def sell(item_to_sell):
    if item_to_sell == "star":
        if item_to_sell in Account["Inventory"]:
            Account["Inventory"].remove(item_to_sell)
            Account["Coins"] += 40
            print(f"Star sold! Current balance: {Account['Coins']} coins.")
    elif item_to_sell == "shell":
        if item_to_sell in Account["Inventory"]:
            Account["Inventory"].remove(item_to_sell)
            Account["Coins"] += 20
            print(f"Shell sold! Current balance: {Account['Coins']} coins.")
    elif item_to_sell == "block":
        if item_to_sell in Account["Inventory"]:
            Account["Inventory"].remove(item_to_sell)
            Account["Coins"] += 5
            print(f"Block sold! Current balance: {Account['Coins']} coins.")
    else:
        print("You don't have this item.")

while True:
    print("\nActions: buy | sell | status | save")
    choice = input("What do you want to do? ").lower()
    
    if choice == "buy":
        item_name = input("Which item? (star: 50 | shell: 30 | block: 10): ").lower()
        items(item_name)
    elif choice == "sell":
        item_name = input("Which item? (star: 40 | shell: 20 | block: 5): ").lower()
        sell(item_name)
    elif choice == "status":
        print(Account)
    elif choice == "save":
        print(Account)
        confirm = input("Save game? (y/n): ").lower()
        if confirm == "y":
            with open("savegame.json", "w") as file:
                json.dump(Account, file)
            print("Game saved successfully!")
            break
        else:
            print("Returning to menu...")
    else:
        print("Invalid input. Please choose from the options above.")
