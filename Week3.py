def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        price=price-price*(discount_percent/100)
        print(f"Applied a discount of : {price*(discount_percent/100)}.\n")
    else:
        price=price
        print('No discount was applied.\n')
    return price

user_price=float(input('Enter the priceof the product: '))
discount_percent=float(input('Enter the discount Percentage e.g 20: '))
final_price=calculate_discount(user_price,discount_percent)
print(f'The final price is: {final_price}')