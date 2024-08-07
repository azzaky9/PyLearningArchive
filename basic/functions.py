# initialize function

def sum(num1, num2):
    result = num1 + num2
    return result

hasil1 = sum(10, 20)
hasil2 = sum(90, 20)
hasil3 = sum(120, 20)

# print(f"hasilnya adalah: {hasil1}")
# print(f"hasilnya adalah: {hasil2}")
# print(f"hasilnya adalah: {hasil3}")

DB_EMAIL = "dummy@gmail.com"
DB_PASSWORD = "admin123"

def login():
    email = input("Please input your email: ")
    password = input("Please input your password: ")
    age = int(input("Please input your age must be greater than >18: "))

    if age >= 18:
        if email == DB_EMAIL and password == DB_PASSWORD:
            return "Logged in"
        else:
            return "Wrong password and Email"
    else:
        return "Your age not able to use this app."

#
# login_message = login()
# print(f"Messsage: {login_message}")



def check_name_inside_list(names,  name_to_check):
    for name in names:
        if (name.lower() == name_to_check.lower()):
            return f"{name_to_check} is exist inside names list"

found_name = check_name_inside_list(["Joko", "Jaka", "Julia", "Indah"], "jaka")
print(found_name)

def default_argument(name="joe"):
    print(f"Hello {name}")

default_argument()