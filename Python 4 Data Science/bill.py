# Prepare a Bill system of a Shoping Mall

items = int(input("Enter No of items Purchase : "))
total_amt = 0

for i in range(items) :
    price_item = float(input("Enter The Price of Item : "))
    total_amt = total_amt + price_item
    i = i+1

    if total_amt >= 1000 :
        discount = 0.10 * total_amt
        print(f"Total Amount of Purchase is {discount}")
    elif total_amt >= 5000 :
        discount = 0.20 * total_amt
        print(f"Total Amount of Purchase is {discount}")
    else :
        discount = 0
        print(f"Total Amount of Purchase is {discount}")

    total_price = total_amt - discount
    print(f"Subtotal Amount is {total_price}")
