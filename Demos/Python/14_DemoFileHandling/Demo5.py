try:

    file = open("employees.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("Employees file does not exist.")

finally:

    print("File operation completed.")