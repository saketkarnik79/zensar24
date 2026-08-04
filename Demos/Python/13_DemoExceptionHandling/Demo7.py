try:

    number = int(
        input("Enter Number: ")
    )

    values = [10, 20, 30]

    position = int(
        input("Enter Position: ")
    )

    print(values[position])

except ValueError:

    print(
        "Invalid Numeric Input."
    )

except IndexError:

    print(
        "Position Not Available."
    )

except Exception:

    print(
        "Unexpected Error Occurred."
    )
finally:
    
    print(
        "Execution Completed."
    )