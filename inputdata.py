# fullname = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(fullname)
# print(age+5)

user = input("Enter username: ")
pwd = input("Enter password: ")

set_user = "admin"
set_pass = "1234"

if user == "admin" and pwd == set_pass:
    print("Yah! Login success")
else:
    print("Oop! Login fail!!")
