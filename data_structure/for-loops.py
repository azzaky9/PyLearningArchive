
# for i in range(10):
#     print(f"print position {i + 1}")


# range(start, stop, step)

# for i in range(1, 20, 3):
#     print(f"Print step 3 {i}")
#
# list_sample = ["Buah", "Buah", "Buah", "Buah", "Buah"]
# for buah in list_sample:
#     print(buah)
#
# fruits = ["Avocado", "Strawberry", "Grape", "Orange", "Delima"]
# for fruit in fruits:
#     print(fruit)

customers = {
    "id1": 'Joko',
    "id2": "Jaka"
}

customers["id3"] = "John"
customers["id4"] = "Joe"

print(f"id 4 is {customers.get("id4")}")
customers.pop("id2")
customers.clear()

# for customer in customers.keys():
#     print(customer)
#     # print(f"id {id} memiliki value {value}")

print(customers)