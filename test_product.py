import unittest
from products import Product


class TestProduct(unittest.TestCase):

    def test_create_product(self):
        """Test that creating a normal product works"""
        product = Product("MacBook Air M2", price=1450, quantity=100)
        self.assertEqual(product.name, "MacBook Air M2")
        self.assertEqual(product.price, 1450)
        self.assertEqual(product.quantity, 100)

    def test_create_prod_invalid_details(self):
        """"Test that creating a product with invalid details (empty name, negative price) invokes an exception"""
        # Test empty name
        with self.assertRaises(ValueError):
            Product("", price=100, quantity=10)

        # Test negative price
        with self.assertRaises(ValueError):
            Product("Product A", price=-100, quantity=10)

    def test_prod_becomes_inactive(self):
        """Test that when a product reaches 0 quantity, it becomes inactive."""
        product = Product("Product A", price=100, quantity=0)
        self.assertFalse(product.is_active())

    def test_buy_modifies_quantity(self):
        """Test that product purchase modifies the quantity and returns the right output."""
        product = Product("Product A", price=100, quantity=10)
        total_price = product.buy(3)
        self.assertEqual(product.quantity, 7)
        self.assertEqual(total_price, 300)

    def test_buy_too_much(self):
        """Test that buying a larger quantity than exists invokes exception."""
        product = Product("Product A", price=100, quantity=10)
        with self.assertRaises(ValueError):
            product.buy(15)


if __name__ == '__main__':
    unittest.main()
