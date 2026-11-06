# Write ANY real Python code here and click "Run Code" or "Start Debug"!
def calculate_invoice(items, tax_rate=0.18):
    subtotal = 0
    for name, price in items:
        subtotal += price
        print(f"Added {name}: ${price}")

    discount = 15 if subtotal >= 100 else 0
    taxed_total = round((subtotal - discount) * (1 + tax_rate), 2)
    return {"subtotal": subtotal, "discount": discount, "total": taxed_total}

cart = [("Cloud IDE Pro", 60), ("Debugger Addon", 50), ("Domain", 15)]
result = calculate_invoice(cart)
print("Final Invoice Summary:", result)