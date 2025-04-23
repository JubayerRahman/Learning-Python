name = "Ohee"
age= 18
married= False
Height= 5.9
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
count = 0

people = [
    {"name": "Alice", "age": 25, "married": False},
    {"name": "Bob", "age": 30, "married": True},
    {"name": "Charlie", "age": 22, "married": False}
]

print(name)
print(age)
print(married)
print(Height)

if age >= 18:
    print("You are an adult")

else:
    print("You are a Minor")

# Tyring on my own
if not married and age > 20:
    print("Get marryied soon")
else:
    print("Why bor why?")

# trying for
for nam in names :
    print(nam)

# trying while
while count< 5:
    print(f"count is {count}")
    count +=1

# Nested loops
for name in names:
    for age in ages:
        print(f"{name} is {age} years old")

# trying loop in object
for person in people:
    print(f"{person['name']} is {person['age']} years old and married: {person["married"]}")

# trying Function

def sayHello(name):
    print(f"Hello, {name}")

sayHello("Jobayer Rahman Ohee")