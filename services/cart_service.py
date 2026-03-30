carts = {}

def get_cart(user):
    if user not in carts:
        carts[user] = {}
    return carts[user]

def add_to_cart(user, pid, qty, products):
    cart = get_cart(user)

    if pid not in products:
        print("Invalid product")
        return

    if products[pid]["stock"] < qty:
        print("Not enough stock")
        return

    cart[pid] = cart.get(pid, 0) + qty
    print("Added to cart")

def remove_from_cart(user, pid):
    cart = get_cart(user)
    cart.pop(pid, None)

def view_cart(user, products):
    cart = get_cart(user)
    total = 0
    for pid, qty in cart.items():
        price = products[pid]["price"]
        total += price * qty
        print(pid, qty, price)
    print("Total:", total)