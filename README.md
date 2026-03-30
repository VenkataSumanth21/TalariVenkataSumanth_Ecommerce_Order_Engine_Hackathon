# 🛒 Distributed E-Commerce Order Engine (CLI)

## 📌 Project Overview

This project is a **CLI-based backend simulation** of a distributed e-commerce order processing system.
It is designed to mimic real-world backend challenges such as inventory conflicts, payment failures, transaction rollback, and order lifecycle management.

The system demonstrates strong backend engineering concepts like **data consistency, fault tolerance, and modular architecture**.

---

## 🚀 Features

### 🛍️ Product Management

* Add new products
* Prevent duplicate product IDs
* Update stock

### 🧺 Cart System

* Separate cart for each user
* Add/remove items
* Update item quantities
* Calculate cart total

### 📦 Order Placement Engine

* Validate cart before order
* Calculate total price
* Apply coupon discounts
* Create order

### 💳 Payment Simulation

* Simulates real-world payment success/failure
* Randomized outcomes
* Integrated failure handling

### 🔒 Inventory Management

* Reserve stock before payment
* Prevent overselling
* Restore stock on failure

### 🔁 Transaction Rollback

* If payment fails:

  * Restore inventory
  * Cancel order safely

### 🎟️ Coupon System

* `SAVE10` → 10% discount
* `FLAT200` → ₹200 discount

### 📄 Order Management

* View all orders
* Cancel order
* Prevent duplicate cancellation

### 🧾 Logging System

* Tracks system actions:

  * Order creation
  * Payment status
  * Rollback events
  * Cancellation
* Helps in debugging and auditing

### ⚠️ Failure Injection System

* Simulates failures in:

  * Payment
  * Order creation
* Helps test system reliability

---

## 🏗️ Architecture

The system follows a **modular, service-based architecture**:

### 🔹 Services

* Product Service
* Cart Service
* Order Service
* Payment Service
* Inventory Service
* Coupon Service

### 🔹 Core Modules

* Logger
* Failure Injection
* Utility Functions

👉 This design ensures:

* Loose coupling
* Clean separation of concerns
* Easy scalability

---

## 🔄 Order Processing Flow

Add Product → Add to Cart → Place Order
→ Reserve Stock → Process Payment

### ✔ If Payment Success:

* Order is placed
* Cart is cleared

### ❌ If Payment Fails:

* Inventory is restored
* Transaction is rolled back

---

## ⚙️ Assumptions

* In-memory data storage (no database)
* CLI-based single-user simulation
* Logical concurrency handling
* Random failure simulation
* No external APIs used

---

## ▶️ How to Run

### Step 1: Navigate to project folder

```bash id="run1"
cd Ecommerce_Order_Engine
```

### Step 2: Run the application

```bash id="run2"
python main.py
```

---

## 🧪 Sample Test Flow

1. Add products
2. Add items to cart
3. View cart
4. Place order
5. Enable failure mode
6. Retry order → observe rollback
7. Cancel order
8. View logs

---

## 💡 Concepts Demonstrated

* Transaction Management
* Rollback Mechanisms
* Fault Tolerance
* Inventory Consistency
* Modular System Design
* Backend Engineering Principles

---

## 🔮 Future Enhancements

* REST API (Django/Flask)
* Database integration (MySQL/PostgreSQL)
* Multi-user concurrency (threading)
* Authentication system
* Frontend UI (React/Flutter)

---

## 👨‍💻 Author

**Talari Venkata Sumanth**

---

## 🏁 Conclusion

This project demonstrates how real-world e-commerce systems handle:

* Order processing
* Failures and recovery
* Inventory synchronization
* System reliability

It reflects strong problem-solving skills and backend system design understanding.
