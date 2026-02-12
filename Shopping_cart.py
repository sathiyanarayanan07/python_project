cart =[]

total = 0

while True:
    item = input("enter item (or done):")
    if item =="done":
        break
    price = float(input("price:"))
    cart.append(item)
    total =total+price

    print("items:",cart)
    print("total:",total)