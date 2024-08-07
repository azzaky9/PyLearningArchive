def check_age(age):
    if age >= 18:
       return "Valid age"
    else:
       raise NotImplementedError("Age is invalid, user is not greater than 18")

try:
  print(check_age(20))
except: 
  print("invalid ages")

print("last execution")