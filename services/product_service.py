products = {}

def add_product(pid, name, price, stock):
    if pid in products:
        print("Duplicate product ID!")
        return
    products[pid] = {"name": name, "price": price, "stock": stock}
    print("Product added")

def view_products():
    for k, v in products.items():
        print(k, v)

def update_stock(pid, qty):
    if pid in products:
        products[pid]["stock"] += qty