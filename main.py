from services.product_service import *
from services.cart_service import *
from services.order_service import *
from core.logger import show_logs
from core.failure_injection import enable_failure, disable_failure

def main():
    user = "USER1"

    while True:
        print("\n===== MENU =====")
        print("1 Add Product")
        print("2 View Products")
        print("3 Add to Cart")
        print("4 Remove from Cart")
        print("5 View Cart")
        print("6 Apply Coupon + Place Order")
        print("7 View Orders")
        print("8 Cancel Order")
        print("9 View Logs")
        print("10 Enable Failure Mode")
        print("11 Disable Failure Mode")
        print("0 Exit")

        ch = input("Choice: ")

        if ch == "1":
            pid = input("ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            add_product(pid, name, price, stock)

        elif ch == "2":
            view_products()

        elif ch == "3":
            pid = input("Product ID: ")
            qty = int(input("Qty: "))
            add_to_cart(user, pid, qty, products)

        elif ch == "4":
            pid = input("Product ID: ")
            remove_from_cart(user, pid)

        elif ch == "5":
            view_cart(user, products)

        elif ch == "6":
            coupon = input("Enter coupon (or press Enter): ")
            place_order(user, get_cart(user), products, coupon)

        elif ch == "7":
            view_orders()

        elif ch == "8":
            oid = int(input("Order ID: "))
            cancel_order(oid, products)

        elif ch == "9":
            show_logs()

        elif ch == "10":
            enable_failure()
            print("Failure mode ON")

        elif ch == "11":
            disable_failure()
            print("Failure mode OFF")

        elif ch == "0":
            break

        else:
            print("Invalid")

if __name__ == "__main__":
    main()