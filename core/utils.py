def calculate_total(cart, products):
    total = 0
    for pid, qty in cart.items():
        total += products[pid]["price"] * qty
    return total