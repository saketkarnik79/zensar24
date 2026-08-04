file = open("attendance.txt", "r")

print("Attendance Records")

for line in file:
    print(line.strip())

file.close()