def check_age(age):
    if age >= 18:
        print("Valid age")

    raise NotImplementedError("Age is invalid, user is not greater than 18")


try:
    check_age(10)
except:
    print("Invalid age")

print("BOTTOM PRINT..")