class Customer(object):
    def __init__(self, name, age, gender, orders):
        self.name = name
        self.age = age
        self.gender = gender
        self.orders = orders

    def display_info(self):
        print(f"Name {self.name} - Age {self.age} - Gender {self.gender}")

    def get_age(self):
        print(f"Age {self.age}")

    def check_order(self, value):
        try:
            found_value = self.orders.index(value)
            print(f"Value found at index {found_value}")
            return found_value
        except:
            print("Value not found")
            return -1

    def get_order_by_index(self, index):
        print(f"values: {self.orders[index]}")

    def get_all_orders(self):
        print(self.orders)

    def add_new_order(self, new_value):
        self.insert(0, new_value)
#
# class Animal(object):
#     def  __int__(self, ):


customer = Customer("Joko", 12, "L", [])
customer.add_new_order("ID127")
customer.add_new_order("ID128")
customer.add_new_order("ID129")
customer.get_all_orders()

order_index =  customer.check_order("GAADA") # 0

if order_index > -1:
    customer.get_order_by_index(order_index)