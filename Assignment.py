#1. A function to calculate discount

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    price (float): Original price of the item.
    discount_percent (float): Discount percentage to apply.
    
    Returns:
    float: Final price after applying discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Example usage:
print(calculate_discount(1250, 25))  
print(calculate_discount(1000, 10)) 


#2.Discount function with user input

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or more.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${price:.2f}")
except ValueError:
    print("Please enter valid numeric values.")
