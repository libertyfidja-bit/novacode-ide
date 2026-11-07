# NovaCode Studio — Real Python 3.12 WebAssembly & Line-by-Line Debugger
def calculate_order_total(items, tax_rate=0.08):
    subtotal = 0
    for name, price in items:
        subtotal += price
        print(f"Added {name}: ${price:.2f} (Running Subtotal: ${subtotal:.2f})")
    
    discount = 15.0 if subtotal >= 100 else 0.0
    taxed_total = round((subtotal - discount) * (1 + tax_rate), 2)
    return taxed_total

cart = [("Mechanical Keyboard", 85.0), ("USB-C Hub", 45.0), ("Mousepad", 20.0)]
final_bill = calculate_order_total(cart)
print(f"Final Order Total: ${final_bill}")