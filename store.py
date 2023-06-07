class Store:
  """Contains a list of products that exists in the store"""

  def __init__(self, products=None):
    """Initializes the store with an empty list of products or the provided list"""
    self.products = [] if products is None else products

  def add_product(self, product):
    """Adds a product from the store"""
    self.products.append(product)

  def remove_product(self, product):
    """Removes a product from the store"""
    if product in self.products:
      self.products.remove(product)

  def get_total_quantity(self):
    """Returns how many items are in the store in total (int)"""
    total_quantity = 0
    for product in self.products:
      total_quantity += product.get_quantity()
    return total_quantity

  def get_all_products(self):
    """Returns all products in the store that are active (list)"""
    return self.products

  def order(self, shopping_list):
    """Gets a list of tuples where each tuple has 2 items:
    Product (class) and quantity (int),
    Buys the products and returns the total price of the order"""
    total_price = 0
    for product, quantity in shopping_list:
      try:
        price = product.buy(quantity)
        total_price += price
      except ValueError as e:
        print(f"Error: {str(e)}")
    return total_price
