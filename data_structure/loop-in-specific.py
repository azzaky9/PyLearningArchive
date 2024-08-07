
list_sample = ["Anggur", "Apple", "Avocado"]

appended_list = ["Strawberry", "Jeruk"]

j = 0
while j < len(appended_list):
    list_sample.append(appended_list[j])
    j += 1

i = 0
while i <= 10:
    print(f"while loop at position: {i}")
    i += 1
#
# while True:
#     print(f"infinite loops")

print(list_sample)
