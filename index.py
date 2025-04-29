# Trying default value
def greetings(name="Boy"):
    print(f"hay {name}, Welcome to python")

greetings()
greetings("Ohee")

#keyboard arguments
def name_age(name, age):
    print(f'Hi, my name is {name} and I am {age} years old')
name_age(age= 23, name="Ohee")

#exceptional Handeling
try:
    num = int(input("Enter a valid number more then 0"))
    result = 10 / num
    print(f"Your result is {result}")
except ZeroDivisionError:
    print("I told you give me more then 0, didnt I?")
except ValueError:
    print("You are stupid")


#File Handeling

# Writing FIle:
with open("my_note.txt", "w") as file:
    file.write("Ohee made this file with python.")

# Reading file:
with open("my_note.txt", "r") as file:
    content = file.read()
    print(content)

#Appending file:
with open("my_note.txt", "a") as file:
    file.write("\nOhee will make an AI one day.")

#reading file again:

with open("my_note.txt", "r") as file:
    content = file.read()
    print(content)

# function and file interaction:
def log_message(message):
    with open("loge_file.txt", "a") as file:
        file.write(message + "\n")

log_message("Ohee made this file with python Function")
log_message("Ohee is a genious.")

# reading all log:

def read_log():
    with open("loge_file.txt", "r") as file:
        content = file.read()
        print("Here is all the logs:")
        print(content)
read_log()