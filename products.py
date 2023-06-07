from abc import ABC, abstractmethod


class Product:
  """Product in the store"""

  def __init__(self, name, price, quantity):
    if not name:
      raise ValueError("Name cannot be empty.")
    if price < 0:
      raise ValueError("Price cannot be negative.")

    self.name = name
    self.price = price
    self.quantity = quantity
    self.promotion = None

  def get_quantity(self):
    """Returns the quantity of a product"""
    return self.quantity

  def set_quantity(self, new_quantity):
    """Sets the quantity of a product"""
    self.quantity = new_quantity

  def is_active(self):
    """Returns True if the product is active, otherwise False"""
    return self.quantity > 0

  def activate(self):
    """Activates the product"""
    self.is_active = True

  def deactivate(self):
    """Deactivates the product"""
    self.is_active = False

  def show(self):
    """Displays the product information"""
    promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
    print(f"Product name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}.")

  def set_promotion(self, promotion):
    """Sets the promotion for the product"""
    self.promotion = promotion

  def remove_promotion(self):
    """Removes the promotion from the product"""
    self.promotion = None

  def buy(self, quantity):
    """Buys a given quantity of the product"""
    if quantity <= 0:
      raise ValueError("Quantity must be greater than 0.")

    if self.quantity < quantity:
      raise ValueError("Quantity unavailable.")

    if self.promotion:
      total_price = self.promotion.apply_promotion(self, quantity)
    else:
      total_price = self.price * quantity

    self.quantity -= quantity
    return total_price


class NonStockedProduct(Product):
    """Non-stocked product that does not require quantity tracking"""

    def __init__(self, name, price):
      super().__init__(name, price, 0)

    def show(self):
      """Returns a string that represents the non-stocked product"""
      print(f"{self.name}, Price: ${self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    """Limited product that has a maximum quantity limit"""

    def __init__(self, name, price, quantity, maximum):
      super().__init__(name, price, quantity)
      self.maximum = maximum

    def show(self):
      """Returns a string that represents the product (name, price, quantity, maximum)"""
      print(f"Product name: {self.name}, Product price: {self.price}, Product quantity: {self.quantity}, Maximum quantity: {self.maximum}.")


class Promotion(ABC):
  """Abstract base class for promotions"""

  def __init__(self, name):
    self.name = name

  @abstractmethod
  def apply_promotion(self, product, quantity):
    """Abstract method to apply the promotion"""
    pass


class PercentDiscount(Promotion):
  """Promotion class for percentage discount"""

  def __init__(self, name, percent):
    super().__init__(name)
    self.percent = percent

  def apply_promotion(self, product, quantity):
    """Applies percentage discount to the product's price"""
    discounted_price = product.price * (1 - self.percent / 100)
    return discounted_price * quantity


class SecondHalfPrice(Promotion):
  """Promotion class for second item at half price"""

  def __init__(self, name):
    super().__init__(name)

  def apply_promotion(self, product, quantity):
    """Applies half price to every second item"""
    full_price_quantity = quantity // 2
    half_price_quantity = quantity % 2
    discounted_price = (full_price_quantity * product.price) + (half_price_quantity * product.price / 2)
    return discounted_price


class ThirdOneFree(Promotion):
  """Promotion class for buy 2, get 1 free"""

  def __init__(self, name):
    super().__init__(name)

  def apply_promotion(self, product, quantity):
    """Applies buy 2, get 1 free promotion"""
    full_price_quantity = (quantity // 3) * 2
    free_quantity = quantity % 3
    discounted_price = full_price_quantity * product.price
    return discounted_price
