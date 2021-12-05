class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total(self, how_much):
        result = self.price * how_much
        return result

class Cart:
    def __init__(self):
        self.list = list()

    def add(self, product, how_much):

        total_count = product.price * how_much
        self.list.append(total_count)


    def get_total(self):
        summa = sum(self.list)
        return summa

# Add products to our class "Product"
banana = Product("Banana", 15)
tomato = Product("Tomato", 14)
peach = Product("Peach", 27)




print("We count the amount of products: ")
print("Banana cost: ", banana.get_total(2), "UAH.")
print("Tomato cost: ", tomato.get_total(6), "UAH.")
print("Peach cost: ", peach.get_total(4), "UAH.")

cart = Cart() # create our cart

# Add products to our cart
cart.add(banana, 2)
cart.add(peach, 4)
cart.add(tomato, 6)

# We calculate the cost of our basket of goods
print("The cost of all products: ", cart.get_total())



