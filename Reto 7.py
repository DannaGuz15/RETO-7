class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity):
        return self.price * quantity

class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Appetizer(MenuItem):
    pass

class MainCourse(MenuItem):
    pass

class OrderItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def get_total_price(self):
        return self.item.calculate_total_price(self.quantity)

class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item, quantity=1):
        self._items.append(OrderItem(item, quantity))

    def remove_item(self, item):
        for order_item in self._items:
            if order_item.item == item:
                self._items.remove(order_item)
                return
        raise ValueError("Item not found in order")

    def calculate_total_price(self):
        total_price = 0
        for item in self._items:
            total_price += item.get_total_price()
        return total_price

    def __iter__(self):
        return iter(self._items)
# Menu
water = Beverage("Agua", 2.5, "large")
coke = Beverage ("Sprite", 2.7, "large")
coke2 = Beverage("CocaCola", 3.0, "large")
vino = Beverage("Vino Tinto", 60.0, "large")
vino2 = Beverage("Vino Blanco", 55.0, "large")

wings = Appetizer("Alitas BBQ", 14.0)
wings2 = Appetizer("Alitas bufalo", 15.5)
wings3 = Appetizer("Alitas rellenas", 18.2)
wings4 = Appetizer("Alitas Ranch", 12.5)

pasta = MainCourse("Pasta Carbonara", 25.2)
pasta2 = MainCourse("Pasta Pesto", 24.0)
pasta3 = MainCourse("Pasta Boloñesa", 25.5)
pasta4 = MainCourse("Pasta con camarones", 26.0)  

# Ejemplo de uso
my_order = Order()
coke2 = Beverage("CocaCola", 3.0, "large")

my_order = Order()
my_order.add_item(coke2, 2)
my_order.add_item(coke, 1)
my_order.add_item(wings, 3)
my_order.add_item(pasta, 1)
my_order.add_item(pasta3, 2)

for item in my_order:
    print(f"Cantidad: {item.quantity}")
    print(f"Producto: {item.item.name}")
    if isinstance(item.item, Beverage):
        print(f"Tamaño: {item.item.size}")
    print(f"Precio total del item: ${item.get_total_price():.2f}")
    print("-" * 20)  # Separador visual

total_amount = my_order.calculate_total_price()
print(f"\nTotal de la orden: ${total_amount:.2f}")
