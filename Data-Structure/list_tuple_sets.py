
# >> Lists Data Types for keep many data can access with index.
my_list = [1, 2, 3, 4, 4, 5, 5, 3, 3]
my_list.insert(1, 5)
print(my_list[0])

# >> Tuples Similiar like a Lists but its constant

my_tuples = (1, 2, 3, 4, 5, 6)
# my_tuples.
print(my_tuples[0])

# >> Dictionary Key-values pairs data keeper
my_dictionary = {}
my_dictionary["Grape"] = 20000
my_dictionary["Strawberry"] = 10000

print(f"Dictionary {my_dictionary}")
print(f"Grape Price {my_dictionary["Grape"]}")

for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# >> Set keep your data Unique and Convert your duplicates data on another data types e.g List/Tuples
print(f"Sebelum menggunakan Set {my_list}")
my_sets = set(my_list)
print(f"Sesudah menggunakan Set {my_sets}")
