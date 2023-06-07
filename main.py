import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)]
best_buy = store.Store(product_list)


def start():
  """Shows the menu"""
  print("  Store Menu  ")
  print("  ----------")
  print("1. List all products in store")
  print("2. Show total amount in store")
  print("3. Make an order")
  print("4. Quit")
  user_input = input("Please choose a number: ")

  if user_input == "1":
    products = best_buy.get_all_products()
    for i, product in enumerate(products, start=1):
      print(f"{i}.", end=" ")
      product.show()
    print("-----")
  elif user_input == "2":
    total_amount = best_buy.get_total_quantity()
    print(f"Total of {total_amount} items in store")
    print("-----")
  elif user_input == "3":
    order_list = []
    products = best_buy.get_all_products()
    for i, product in enumerate(products, start=1):
      print(f"{i}.", end=" ")
      product.show()
    print("-----")
    while True:
      print("When you want to finish order, enter empty text.")
      product_num_input = input("Enter the product number (or leave empty to finish): ")
      if not product_num_input:
        break
      try:
        product_num = int(product_num_input)
        if product_num < 1 or product_num > len(best_buy.products):
          print("Invalid product number.")
          continue
        quantity = int(input("What amount do you want? "))
        product = best_buy.products[product_num - 1]
        order_list.append((product, quantity))
        print("Product added to list!")
        print("*****")
      except ValueError:
        print("Invalid input. Please enter a valid product number.")
    total_payment = best_buy.order(order_list)
    print(f"Order made! Total payment: {total_payment}")
  elif user_input == "4":
    print("Exiting...")
    return
  else:
    print("Invalid input. Please try again.")

  #Calling start again for the next iteration
  start()


def main():
    start()


if __name__ == '__main__':
    main()
