db_id = "uuid12"
request_id = "uuid12"

number_1: int = 10
number_2 = int(input("input your number: ")) # str

if number_1 == number_2:
    print("value same")
else:
    print("value not same")

if request_id == db_id:
    print("user exist")
else:
    print("user does not exist, and not found please double check your request id")

if request_id != db_id:
    print("user does not exist, and not found please double check your request id")
