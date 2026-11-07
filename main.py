# NovaCode Studio — Python 3.12 WebAssembly Engine
def calculate_order_total(cart, tax_rate=0.08):
    subtotal = 0.0
    for item in cart:
        name = item["name"]
        price = item["price"] * item["qty"]
        subtotal += price
        print(f"Added {item['qty']}x {name}: ${price:.2f}")
    
    discount = 15.0 if subtotal >= 100 else 0.0
    taxed_total = round((subtotal - discount) * (1 + tax_rate), 2)
    return {"subtotal": subtotal, "discount": discount, "total": taxed_total}

shopping_cart = [
    {"name": "Mechanical Keyboard", "price": 75.0, "qty": 1},
    {"name": "USB-C Hub", "price": 35.0, "qty": 2}
]

summary = calculate_order_total(shopping_cart)
print("Final Summary:", summary)