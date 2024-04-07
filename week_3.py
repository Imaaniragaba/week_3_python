# defining the function

def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        discounted_price = price * (1 - discount_percent)
        return discounted_price
    else:
        return price


#prompting the user for feedback

price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percent e.g 0.2: "))

final_price = calculate_discount(price, discount_percent)
print(f"The final price is ${final_price}.")
    