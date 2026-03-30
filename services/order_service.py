from services.inventory_service import reserve_stock, release_stock
from services.payment_service import process_payment
from services.coupon_service import apply_coupon
from core.logger import log
from core.failure_injection import should_fail
from core.utils import calculate_total

orders = {}
order_counter = 1

def place_order(user, cart, products, coupon=None):
    global order_counter

    if not cart:
        print("Cart empty")
        return

    total = calculate_total(cart, products)

    if coupon:
        total = apply_coupon(total, coupon)

    # Failure injection (order creation)
    if should_fail():
        print("Order creation failed!")
        return

    # Reserve stock
    if not reserve_stock(products, cart):
        print("Stock insufficient")
        return

    log("Stock reserved")

    # Payment
    if not process_payment():
        print("Payment failed → rollback")
        release_stock(products, cart)
        log("Rollback completed")
        return

    # Success
    orders[order_counter] = {
        "user": user,
        "items": cart.copy(),
        "total": total,
        "status": "PLACED"
    }

    log(f"Order {order_counter} placed")

    order_counter += 1
    cart.clear()

def view_orders():
    for oid, val in orders.items():
        print(oid, val)

def cancel_order(order_id, products):
    if order_id not in orders:
        print("Invalid order")
        return

    order = orders[order_id]

    if order["status"] == "CANCELLED":
        print("Already cancelled")
        return

    release_stock(products, order["items"])
    order["status"] = "CANCELLED"
    log(f"Order {order_id} cancelled")