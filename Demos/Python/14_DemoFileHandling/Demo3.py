# append_log.py

file = open("activity_log.txt", "a")

activity = input("Enter Activity: ")

file.write(activity + "\n")

file.close()

print("Activity Saved Successfully")