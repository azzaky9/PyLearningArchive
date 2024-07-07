
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

compare_first = int(input(f"masukkan angka pertama: "))
compare_second = int(input(f"masukkan angka kedua: "))

# for i in arr:
#     print(f"item {i}")
# == is
# != is not

# Works in general
if "abc" != "dca":
    print("same value")

# keyword
if compare_first is compare_second:
    print("same value")
else:
    print("value is not same")

if 10 >= 10 and 10 <= 15:
    print("value greater than 10 but not greater than 15")

for index, item in enumerate(arr):
    print(f"calculation {item} % 2 = {item % 2}")
    result_moduled = item % 2
    if result_moduled == 0:
        print(f"this item {item} is genap")
    else:
        print(f"this item {item} is ganjil")


# for i in range(10):
#     print(f"item {i + 1}")
