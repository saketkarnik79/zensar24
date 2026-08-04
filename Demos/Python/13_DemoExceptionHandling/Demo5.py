print("BANKING SYSTEM")

try:

    amount = int(
        input("Enter Amount: ")
    )

    result = 10000 / amount

    print("Result:", result)

except ZeroDivisionError:

    print(
        "Amount cannot be zero."
    )

finally:

    print(
        "Transaction Closed."
    )