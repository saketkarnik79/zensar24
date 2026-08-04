try:

    file = open(
        "Demo1.py",
        "r"
    )

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print(
        "Report file not found."
    )
