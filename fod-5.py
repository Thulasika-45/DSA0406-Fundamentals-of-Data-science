# Given data
item_prices = [25, 30, 15, 40]  # Example item prices
item_quantities = [3, 2, 4, 1]  # Example item quantities
discount_rate = 10  # 10% discount
tax_rate = 5  # 5% tax

# Calculate the total cost before discounts and taxes
subtotal = sum(item_price * item_quantity for item_price, item_quantity in zip(item_prices, item_quantities))

# Apply the discount
discount = (discount_rate / 100) * subtotal
discounted_total = subtotal - discount

# Calculate the tax amount
tax = (tax_rate / 100) * discounted_total

# Calculate the final total cost
total_cost = discounted_total + tax

print("Subtotal: $", subtotal)
print("Discount: $", discount)
print("Tax: $", tax)
print("Total Cost: $", total_cost)
