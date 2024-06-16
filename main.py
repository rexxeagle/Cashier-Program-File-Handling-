from file_handling import read_invoice, write_invoice
print("Welcome to Eagle Tech Mart. Happy Shopping:)")

items_price = {
    "Laptop": 10000000,
    "Smartphone": 5000000,
    "Tablet": 3000000
}

def menus():
    print("Here's the available menus:")
    print("1. Laptop (Rp. 10.000.000)")
    print("2. Smartphone (Rp. 5.000.000)")
    print("3. Tablet (Rp. 3.000.000)")
    print("4. Exit")
    print()

    paid_items = []
    total_price = 0

    sum_items = int(input("How many items do you want to buy? (type 4 for exit) "))
    if sum_items == 4:
        print("Thanks for coming")
        exit()
    elif sum_items < 1:
        print("Invalid Input")
        is_repeat_program()
    elif sum_items > 3:
        print("You can only buy up to 3 items")
        is_repeat_program()
    else:
        for i in range(sum_items):
            choice = int(input("What do you want to buy (1-3)? (Type 4 for exit): "))
            if choice < 1 or choice > 4:
                print("Invalid choice")
                is_repeat_program()
            else:
                if choice == 1:
                    print(f"You want to buy Laptop with price Rp. {items_price['Laptop']:,.2f}")
                    qty = int(input("How many QTY do you want to buy?: "))
                    print()
                    if qty < 1:
                        print("Invalid QTY")
                        is_repeat_program()
                    else:
                        paid_items.append(("Laptop", items_price['Laptop'], qty))
                elif choice == 2:
                    print(f"You want to buy Smartphone with price Rp. {items_price['Smartphone']:,.2f}")
                    qty = int(input("How many QTY do you want to buy?: "))
                    print()
                    if qty < 1:
                        print("Invalid QTY")
                        is_repeat_program()
                    else:
                        paid_items.append(("Smartphone", items_price['Smartphone'], qty))
                elif choice == 3:
                    print(f"You want to buy Tablet with price Rp. {items_price['Tablet']:,.2f}")
                    qty = int(input("How many QTY do you want to buy?: "))
                    print()
                    if qty < 1:
                        print("Invalid QTY")
                        is_repeat_program()
                    else:
                        paid_items.append(("Tablet", items_price['Tablet'], qty))
                else:
                    print("Thanks for coming")
                    exit()
        for item in paid_items:
            item, item_price, item_qty = item
            totals = item_price * item_qty
            total_price += totals
        print(f"Total Price: Rp. {total_price:,.2f}")
        cus_money = int(input("Input your money: Rp. "))
        if cus_money < total_price:
            print("Your money is not enough")
            exit()
        else:
            write_invoice.write(paid_items, cus_money)
            print("Thank you for shopping with us!")
            print()
            input("Press Enter to print the invoice")
            read_invoice.read()

def is_repeat_program():
    repeat = input("Do you want to repeat the program? (y/n): ")
    if repeat == "y":
        menus()
    elif repeat == "n":
        print("Thanks for coming")
        exit()
    else:
        print("Invalid input")
        is_repeat_program()
menus()