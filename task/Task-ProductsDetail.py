products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

quantities = {}
gift_wrapping = {}

for product in products:
    quantities[product] = int(input(f"Enter the quantity of {product}: "))
    gift_wrapping[product] = input(f"Wrap {product} as a gift? (yes/no): ").lower() == "yes"

product_totals = {}
for product in products:
    product_totals[product] = quantities[product] * products[product]

subtotal = sum(product_totals.values())

discount_name = ""
discount_amount = 0

if sum(quantities.values()) > 30 and any(quantity > 15 for quantity in quantities.values()) and "tiered_50_discount" in discount_rules:
    discount_name = "tiered_50_discount"
    discount_amount = subtotal * (discount_rules["tiered_50_discount"] / 100)
elif sum(quantities.values()) > 20 and "bulk_10_discount" in discount_rules:
    discount_name = "bulk_10_discount"
    discount_amount = subtotal * (discount_rules["bulk_10_discount"] / 100)
elif any(quantity > 10 for quantity in quantities.values()) and "bulk_5_discount" in discount_rules:
    discount_name = "bulk_5_discount"
    discount_amount = product_total * (discount_rules["bulk_5_discount"] / 100)
elif subtotal > 200 and "flat_10_discount" in discount_rules:
    discount_name = "flat_10_discount"
    discount_amount = discount_rules["flat_10_discount"]

gift_wrap_fee = sum(1 * quantities[product] for product in products if gift_wrapping[product])
shipping_fee = sum(quantities.values()) * 0.5
total = subtotal - discount_amount + gift_wrap_fee + shipping_fee

print("\nProduct Details:")
for product in products:
    print(f"{product} - Quantity: {quantities[product]}, Total: ${product_totals[product]}")

print(f"\nSubtotal: ${subtotal}")

if discount_name:
    print(f"Discount Name: {discount_name} & Discount Amount: ${discount_amount}")

print(f"Shipping Fee: ${shipping_fee} & Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${total}")