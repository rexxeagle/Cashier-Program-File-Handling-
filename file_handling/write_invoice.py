from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print(current_time)

# def write(item, price, qty, cus_money):
#     text = f'''
#                  Eagle Tech Mart
# -------------------------------------------------
# Order Time: {current_time}   INV{now.strftime("%Y%S")}ETM
# -------------------------------------------------
# Item: {item}    Qty: {qty}    Price: Rp. {price:,.2f}
#                    ------------------------------
#                    Total Price: Rp. {price * qty:,.2f}
#                 Customer Money: Rp. {cus_money:,.2f}
#                         Change: Rp. {cus_money - (price * qty):,.2f}
# -------------------------------------------------
#           Thanks for shopping with us!
#              Made by Rendy Elang
# '''

#     with open("invoices_output/invoice.txt", 'w') as invoice_file:
#         invoice_file.write(text)

def write(paid_items, cus_money):
    total_price = 0
    loops = f""
    for item in paid_items:
        item_name, item_price, item_qty = item
        totals = item_price * item_qty
        total_price += totals
        loop_item = f"Item: {item_name}    Price: Rp. {item_price:,.2f}    QTY: {item_qty}"
        loops += loop_item + "\n"
    text = f'''
                 Eagle Tech Mart
-------------------------------------------------
Order Time: {current_time}   INV{now.strftime("%Y%S")}ETM
-------------------------------------------------
{loops}
                   ------------------------------
                   Total Price: Rp. {total_price:,.2f}
                Customer Money: Rp. {cus_money:,.2f}
                        Change: Rp. {cus_money - total_price:,.2f}
-------------------------------------------------
          Thanks for shopping with us!
             Made by Rendy Elang
'''
    with open("invoices_output/invoice.txt", 'w') as invoice_file:
        invoice_file.write(text)