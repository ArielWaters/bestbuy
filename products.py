class Product:
  """Product in the store, encapsulates its name, price
  keeps track of the total quantity of items, when purchased it gets modified"""

  def __init__(self, name, price, quantity):
    """If sg is invalid, it displays an error"""
    self.name = name
    self.price = price
    self.quantity = quantity

  def get_quantity(self):
    """Returns the quantity of a product (float)"""
    return self.quantity

  def set_quantity(self, new_quantity):
    """Sets the quantity of a product. If it reaches 0, it deactivates the product"""
    self.quantity = new_quantity

  def is_active(self):
    """Returns True if the product is active, otherwise False"""
    if self.quantity > 0:
      return True
    else:
      return False

  def activate(self):
    """Activates the product"""
    self.is_active = True

  def deactivate(self):
    """Deactivates the product"""
    self.is_active = False

  def show(self):
    """Returns a string that represents the product (name, price, quantity)"""
    print (f"Product name: {self.name}, Product price: {self.price}, Product quantity: {self.quantity}.")

  def buy(self, quantity):
    """Buys a given quantity,
    Returns the total price of the purchase,
    Updates the quantity of the product,
    In case of a problem, raises an exception"""
    if quantity <= 0:
      raise ValueError("Quantity must be greater than 0.")

    if self.quantity < quantity:
      raise ValueError("Quantity unavailable.")

    total_price = self.price * quantity
    self.quantity -= quantity
    return total_price