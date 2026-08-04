orders = [
    "Laptop",
    "Mobile",
    "Printer"
]

try:

    index = int(
        input("Enter Order Position: ")
    )

    print(
        "Order:",
        orders[index]
    )

except IndexError:

    print(
        "Order position does not exist."
    )