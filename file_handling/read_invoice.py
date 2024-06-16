def read():
    with open("invoices_output/invoice.txt", "r") as file:
        print(file.read())