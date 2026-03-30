# 🛒 Distributed E-Commerce Order Engine (CLI)

## 📌 Project Overview

This project is a CLI-based backend simulation of a distributed e-commerce order processing system. It is designed to mimic real-world backend challenges such as inventory conflicts, payment failures, transaction rollbacks, and order lifecycle management.

The system follows a modular, service-based architecture and demonstrates key backend engineering concepts like consistency, fault tolerance, and failure handling.

---

## 🚀 Key Features

### 🛍️ Product Management

* Add new products
* Update product stock
* Prevent duplicate product entries

### 🧺 Cart System

* User-specific carts
* Add/remove items
* Quantity management
* Cart total calculation

### 📦 Order Processing Engine

* Validates cart before order placement
* Calculates total cost
* Supports coupon-based discounts
* Handles order creation flow

### 💳 Payment Simulation

* Simulates real-world payment scenarios
* Random success/failure handling
* Integrated with failure injection system

### 🔒 Inventory Management

* Stock reservation before payment
* Prevents overselling
* Automatic stock restoration on failure

### 🔁 Transaction Rollback System

* Restores inventory if payment fails
* Ensures system consistency
* Handles partial failures gracefully

### 🎟️ Coupon System

* `SAVE10` → 10% discount
* `FLAT200` → ₹200 discount
* Applied during order placement

### 📄 Order Lifecycle Management

* Order states:

  * CREATED
  * PLACED
  * CANCELLED
* Supports order cancellation and refund simulation

### 🧾 Logging System

* Tracks all major operations:

  * Order creation
  * Payment status
  * Rollback actions
  * Cancellation
* Provides system transparency

### ⚠️ Failure Injection Mode

* Simulates system failures
* Helps test robustness of order flow
* Can be toggled ON/OFF

---

## 🏗️ System Architecture

The system follows a **modular microservices-inspired design**:

### Services:

* Product Service
* Cart Service
* Order Service
* Payment Service
* Inventory Service
* Coupon Service

### Core Modules:

* Logger
* Failure Injection
* Event Processing
* Utility Functions

Each module is loosely coupled, making the system easy to maintain and extend.

---

## 🔄 Order Processing Flow

1. Add product to system
2. Add items to cart
3. Apply coupon (optional)
4. Place order
5. Reserve inventory
6. Process payment

### ✔ If Payment Success:

* Order is confirmed
* Cart is cleared

### ❌ If Payment Fails:

* Inventory is restored
* Order is rolled back

---

## ⚙️ Assumptions

* In-memory data storage (no database)
* Single-user CLI simulation
* Concurrency handled logically (no threading)
* Randomized failure simulation
* No external APIs used

---

## ▶️ How to Run the Project

### Step 1: Clone or download the repository

### Step 2: Navigate to project folder

```bash
cd Ecommerce_Order_Engine
```

### Step 3: Run the application

```bash
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
* Modular Architecture
* Backend System Design

---

## 🔮 Future Enhancements

* REST API using Django/Flask
* Database integration (MySQL/PostgreSQL)
* Multi-user concurrency (threading)
* Authentication system
* UI (React/Flutter)

---

## 👨‍💻 Author

**Talari Venkata Sumanth**

---

## 🏁 Conclusion

This project demonstrates how real-world e-commerce platforms handle:

* Order processing
* Failures and recovery
* Inventory synchronization
* System reliability

It showcases strong backend engineering fundamentals and practical system design thinking.
