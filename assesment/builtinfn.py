import math

# my_array = [1, 2, 3, 4, 5] # array
my_str = "apple, grape, jambu, strawberry" # string

print(my_str.lower())
print(my_str.count("apple"))
print(my_str.capitalize())
print(my_str.replace("apple", "pear"))
print(my_str.split(" "))
# print(my_str.)

num1 = 20
num2 = 30

print(sum([num1, num2, 90, 60, 70]))
print(min([20, 80, 90, 60, 40]))
print(max([20, 80, 90, 60, 40]))

pi = math.floor(math.sqrt(4) * math.pi)
print(f"PI CALC {pi}")

my_list1 = [20, 10, 20, 100, 20, 70]
my_list2 = [20, 10, 20, 100, 20, 70]

friendList = ["Joko", "Johan", "Jaka", "Yoga", "Hanum"]

my_list1.extend(my_list2)

print(my_list1.count(20))
print(my_list1)

search_friendlist_name = "johan"

try:
    print(friendList.index(search_friendlist_name))
except:
    print(f"{search_friendlist_name} is not in list")



print("after running friend list searching")

