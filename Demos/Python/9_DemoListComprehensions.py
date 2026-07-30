# Without list comprehension
# numbers = [10, 20, 30, 40, 50];
# squares = [];
# for num in numbers:
#     squares.append(num ** 2);
# print(squares);

# Using list comprehension
# numbers = [10, 20, 30, 40, 50];
# squares = [num ** 2 for num in numbers];
# print(squares);

# names = ["john", "alice", "bob"];
# upper_names = [name.upper() for name in names];
# print(upper_names);

 
# numbers = range(1, 11);
# evens = [n for n in numbers if n % 2 == 0];
# print(evens);

# numbers = range(1, 11);
# odds = [n for n in numbers if n % 2 != 0];
# print(odds);

# numbers = [1, 2, 3, 4, 5]
# result = [f"Even: {n}" if n % 2 == 0 else f"Odd: {n}" for n in numbers]
# print(result)

# numbers = [10, -5, 20, -8, 30];
# result = [n if n >= 0 else 0 for n in numbers];
# print(result);

# pairs = [];
# x = ["A", "B", "C"];
# y = [1, 2, 3];
# pairs = [(i, j) for i in x for j in y];
# print (pairs);

# word = "Python";
# chars = [ch for ch in word];
# print(chars);

# word = "Programming";
# vowels = [ch for ch in word if ch.lower() in "aeiou"];
# print(vowels);

# files = ["report.pdf", "image.jpg", "data.xlsx", "notes.pdf"];
# pdf_files = [file for file in files if file.endswith(".pdf")];
# print(pdf_files);

students = [
    {"name": "Amit", "marks": 92},
    {"name": "Riya", "marks": 78},
    {"name": "Karan", "marks": 35},
    {"name": "Neha", "marks": 65}
];

results = [
    f"{student['name']} - Pass"
    if student["marks"] >= 40
    else f"{student['name']} - Fail"
    for student in students
];

print(results);