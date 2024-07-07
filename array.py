arr = ["1", 1, 2, 3, 4, 5, 6]
trash_array = [2, 47, 3, 1, 2, 99, 100, 59]

last_array = arr[-2]
first_array = arr[2]

print(f"array at first position is: {first_array}")
print(f"array at last position is: {last_array}")

print(f"previouse array is: {arr}")

arr.append(7)
print(f"array after append is: {arr}")

arr.insert(1, "A")
print(f"array after insert is: {arr}")

arr.remove('A')
print(f"array after remove is: {arr}")

print(f"previouse trash array is: {trash_array}")

trash_array.sort()
print(f"previouse trash array after sorted. is: {trash_array}")

print(f"panjang array is: {len(arr)}")
