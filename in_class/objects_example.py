# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

    def reduce_inventory(self, amount):
        if (self.inventory - amount) <= 0:
            self.needs_restocking = True
        self.inventory -= amount

    def get_inventory_report(self):
        if self.inventory == 0:
            return "There are no bars!"
        return f"There are {self.inventory} bars."


pina_bar = Product("Piña Chocolotta", 7.99,["200 calories", "24 g sugar"])

pina_bar.increase_inventory(1)
Product.increase_inventory(pina_bar,1)  # this is equivalent to the line above

print(pina_bar.get_inventory_report())
print(pina_bar.inventory)

print(hasattr(pina_bar,"needs_restocking"))

pina_bar.reduce_inventory(2)
print(pina_bar.get_inventory_report())

print(hasattr(pina_bar,"needs_restocking"))
print(pina_bar.needs_restocking)

truffle_bar = Product("Trufflapagus", 9.99, ["170 calories", "19 g sugar"])
truffle_bar.increase_inventory(1)
bars = [pina_bar, truffle_bar]   # lists can contain items (or objects) of any type
print(f"truffle_bars = {bars[1].inventory}")
