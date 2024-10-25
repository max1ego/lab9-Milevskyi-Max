students_height = {
    "Shevchuk": 165,
    "Ivanenko": 170,
    "Petryshyn": 160,
    "Kovalchuk": 175,
    "Bondar": 168,
    "Tkachenko": 172,
    "Sydorchuk": 169,
    "Kravets": 166,
    "Boychuk": 163,
    "Hrytsenko": 171
}

students_age = {}

for name in students_height.keys():
    age = int(input(f"Введіть вік учня {name}: "))
    students_age[name] = age

print(students_age)