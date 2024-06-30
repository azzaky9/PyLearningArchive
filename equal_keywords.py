db_id = "uuid12"
request_id = "uuid12"

number_1: int = 10
number_2 = int(input("input your number: ")) # str

# is = sama dengan
if number_1 is number_2:
    print("value same")
else:
    print("value not same")

if request_id is db_id:
    print("user exist")
else:
    print("user does not exist, and not found please double check your request id")


# is not
# apakah tidak sama dengan
if number_1 is not number_2:
    print("number 1 and input value is not same")
else:
    print("number 1 and input value is same")
