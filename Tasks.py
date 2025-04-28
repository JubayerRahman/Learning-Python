# Task 1:
def get_city_and_country():
    city= "Chandpur"
    country = "Bangladesh"
    return city, country

main_city, main_country = get_city_and_country()

print(main_city)
print(main_country)

#Task 2:
numbers = [2, -4, 7, -1, 0]

for num in numbers:
    if num >0 : print(f'{num} is a positive number')
    else: print(f'{num} is negative number')

#Task 3:

My_fav_foods = ["Fish", "Rice"]

My_fav_foods.append("Tea")
My_fav_foods.append("Chocolate")
print(My_fav_foods)

My_fav_foods.pop()
print(My_fav_foods)

#Task 4:

hobbies = ["Coding", "Sleeping", "Traveling"]
hobbies.remove("Sleeping")
print(hobbies)

#Task 5:

num= 0

while num<21 :
    if num % 2 != 0 : print(f"{num} is a odd number")
    num +=1