# Import libraries for abstract base classes, JSON file handling, and operating system operations
from abc import ABC, abstractmethod
import json
import os


# Abstract base class defining the interface for different payment methods
# This ensures all payment implementations follow the same contract (have a pay method)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        # Abstract method that must be implemented by subclasses
        pass


# Concrete implementation: Credit Card payment method
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        # Process payment using credit card
        print(f"Paid ₹{amount} using Credit Card")


# Concrete implementation: UPI (Unified Payments Interface) payment method
class UPIPayment(PaymentMethod):
    def pay(self, amount: float):
        # Process payment using UPI
        print(f"Paid ₹{amount} using UPI")


# Concrete implementation: Wallet payment method
class WalletPayment(PaymentMethod):
    def pay(self, amount: float):
        # Process payment using wallet
        print(f"Paid ₹{amount} using Wallet")


# Abstract base class defining the interface for different notification methods
# This ensures all notification implementations follow the same contract
class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        # Abstract method that must be implemented by subclasses
        pass


# Concrete implementation: Send notifications via Email
class EmailNotification(NotificationService):
    def send(self, message: str):
        # Send order confirmation email to customer
        print(f"Email sent: {message}")


# Concrete implementation: Send notifications via SMS
class SMSNotification(NotificationService):
    def send(self, message: str):
        # Send order confirmation SMS to customer
        print(f"SMS sent: {message}")


# Concrete implementation: Send notifications via Push notifications
class PushNotification(NotificationService):
    def send(self, message: str):
        # Send order confirmation as push notification to customer's app
        print(f"Push notification: {message}")


# Abstract base class defining the interface for data persistence/storage
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        # Abstract method for saving orders to storage
        pass


# Concrete implementation: Store orders in a JSON file
class JSONFileRepository(OrderRepository):
    # Constructor that sets the JSON file name for storing orders
    def _init_(self, filename="orders.json"):
        self.filename = filename

    def save(self, order):
        # Initialize empty list to hold order data
        data = []

        # Check if JSON file already exists
        if os.path.exists(self.filename):
            # If file exists, read existing orders
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                except:
                    # If file is corrupted or empty, start with empty list
                    data = []

        # Create a dictionary with order details
        order_data = {
            "order_id": order.order_id,
            "amount": order.amount,
            "final_amount": order.get_final_amount(),  # Final amount after discounts/fees
            "type": order._class.name_  # Get the order type (Regular, Discounted, Priority)
        }

        # Add the new order to the data list
        data.append(order_data)

        # Write all orders (existing + new) back to the JSON file
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)  # Pretty print with indentation

        # Print confirmation message
        print(f"Order {order.order_id} saved to JSON file")


# Abstract base class defining the interface for different order types
class Order(ABC):
    def _init_(self, order_id: int, amount: float):
        self.order_id = order_id  # Unique order identifier
        self.amount = amount  # Original order amount

    @abstractmethod
    def get_final_amount(self) -> float:
        # Abstract method to calculate final amount (may have discounts/fees)
        pass


# Order type 1: Regular order with no discount or extra fees
class RegularOrder(Order):
    def get_final_amount(self) -> float:
        # Final amount is same as original amount
        return self.amount


# Order type 2: Discounted order where customer gets a discount
class DiscountedOrder(Order):
    def _init_(self, order_id: int, amount: float, discount: float):
        super()._init_(order_id, amount)
        self.discount = discount  # Discount amount to subtract

    def get_final_amount(self) -> float:
        # Final amount is original amount minus discount
        return self.amount - self.discount


# Order type 3: Priority order that includes delivery charge/priority fee
class PriorityOrder(Order):
    def get_final_amount(self) -> float:
        # Final amount is original amount plus 50 rupees priority fee
        return self.amount + 50


# Main service class that orchestrates the entire order placement process
# It uses dependency injection to accept payment, notification, and repository implementations
class OrderService:
    def _init_(self, payment: PaymentMethod,
                 notifier: NotificationService,
                 repository: OrderRepository):
        # Store the payment method instance
        self.payment = payment
        # Store the notification service instance
        self.notifier = notifier
        # Store the repository instance for data persistence
        self.repository = repository

    def place_order(self, order: Order):
        # Calculate the final amount for the order (may include discounts/fees)
        final_amount = order.get_final_amount()
        # Process payment using the injected payment method
        self.payment.pay(final_amount)
        # Save the order to persistent storage using the injected repository
        self.repository.save(order)
        # Send notification to customer using the injected notification service
        self.notifier.send(
            f"Order {order.order_id} placed successfully! Amount: ₹{final_amount}"
        )


# Main execution block - runs when script is executed directly
if _name_ == "_main_":

    # Get order details from user
    order_id = int(input("Enter Order ID: "))
    amount = float(input("Enter Amount: "))

    # Display order type options and get user choice
    print("\nSelect Order Type:")
    print("1. Regular")
    print("2. Discounted")
    print("3. Priority")
    order_type = int(input("Choice: "))

    # Create appropriate order object based on user choice
    if order_type == 2:
        # For discounted order, also ask for discount amount
        discount = float(input("Enter Discount: "))
        order = DiscountedOrder(order_id, amount, discount)
    elif order_type == 3:
        # For priority order, no additional input needed
        order = PriorityOrder(order_id, amount)
    else:
        # Default to regular order
        order = RegularOrder(order_id, amount)

    # Display payment method options and get user choice
    print("\nSelect Payment Method:")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Wallet")
    p = int(input("Choice: "))

    # Create appropriate payment method object based on user choice
    if p == 1:
        payment = CreditCardPayment()
    elif p == 2:
        payment = UPIPayment()
    else:
        payment = WalletPayment()

    # Display notification type options and get user choice
    print("\nSelect Notification Type:")
    print("1. Email")
    print("2. SMS")
    print("3. Push")
    n = int(input("Choice: "))

    # Create appropriate notification service object based on user choice
    if n == 1:
        notifier = EmailNotification()
    elif n == 2:
        notifier = SMSNotification()
    else:
        notifier = PushNotification()

    # Create repository instance for storing orders in JSON file
    repository = JSONFileRepository()

    # Create order service with all dependencies (payment, notification, repository)
    service = OrderService(payment, notifier, repository)
         # Process the order (pay, save, and notify)
    service.place_order(order)