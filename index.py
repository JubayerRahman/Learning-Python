#trying tuple
my_tuple = (10, 20, 30)
print(my_tuple[0])

# tyring set
my_set ={1,2,3,4,5,5,6,6,6,9,9,9}
print(my_set)

#trying Dictionaries
person = {
    'name':"Ohee",
    "age":"23",
    "Bike":"classic 350"
}
print(person["Bike"])

# multiple Value returning Function
def name_and_age ():
    name = "Ohee"
    age = 23
    return name, age

person_name, person_age = name_and_age()

print(person_name)
print(person_age)

#conditions in loop
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0 : print(f"{num} is even")
    else: print(f'{num} is odd')

#trying some list mehtods
fruits = ["apple", "banana", "cherry"]
fruits.append("date")

print(fruits)

fruits.pop()
print(fruits)

fruits.remove("banana")
print(fruits)