# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product.
# Input
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
# Output
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00
# Input
# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy
# Output
# Beer -> 660.00
# Water -> 250.00
# IceTea -> 110.00

d_products = {}
while True:
    command_1 = input()
    if command_1 == "buy":
        break
    command = command_1.split(" ")
    product_name = command[0]
    product_price = float(command[1])
    product_quantity = int(command[2])
    if product_name not in d_products.keys():
        d_products[product_name] = [product_price, product_quantity]
    elif product_name in d_products.keys():
        values = d_products[product_name]
        values[1] += product_quantity
        if values[0] != product_price:
            values[0] = product_price

for item, [price, quantity] in d_products.items():
    total = price * quantity
    print(f"{item} -> {total:.2f}")
