list_sample = [1, 2, 3, 4, 5, 6, 7]
print(f"Panjang List: {len(list_sample)}")

for index, i in enumerate(list_sample):
    print(f"index ke {index}: {i}")

dictionaries = {
    "Karyawan1": "Zaky",
    "Karyawan2": "Joko"
}

for i in range(20):
    print(i + 1)

# if items == 20 break;

for key, value in dictionaries.items():
    print(f"{key}: {value}")


count = 0
# for j in count == 10:
#     print(j)
#     count += 1

# argument
def print_message(message):
    print(message)

print_message("Hello World")