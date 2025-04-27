# trying range()
for i in range(10, 20, 5):
    print(i)

# Trying Len()
names = ["Ohee", "Oree", "Jobayer", "Junayed"]
print("The langht is: ",len(names))

# Trying enumerate()
for index,name in enumerate(names):
    print(f"{index} : {name}")

# Trying List comprehention 
numbers = [i for i in range(10)]
even_numbers = [i for i in range(10) if i % 2 == 0 ]
print(numbers)
print(even_numbers)

# Function with multiple variable
def add_numbers(a, b):
    return a + b

def reduce_numbers (a,b):
    if a>= b  : return a-b
    else: return "Your Values are incorrect"
print(add_numbers(20, 20))
print(reduce_numbers(20, 5))