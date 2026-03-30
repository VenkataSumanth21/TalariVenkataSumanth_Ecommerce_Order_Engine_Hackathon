def reserve_stock(products, cart):
    for pid, qty in cart.items():
        if products[pid]["stock"] < qty:
            return False
    for pid, qty in cart.items():
        products[pid]["stock"] -= qty
    return True

def release_stock(products, cart):
    for pid, qty in cart.items():
        products[pid]["stock"] += qty