# #!/usr/bin/env python3
# Initialization (__init__):
# discount is an optional argument, defaulting to 0.
# total starts at 0, and items is initialized as an empty list.
# last_transaction is used to keep track of the most recent addition for voiding purposes.
# add_item Method:
# Adds the item's cost to the total, considering the optional quantity.
# Updates the items list with the item's name, repeated for the given quantity.
# Records details of the last transaction for potential voiding.
# apply_discount Method:
# Calculates and applies the discount if available, reducing the total.
# Outputs the success message with the updated total if a discount is applied; otherwise, provides an error message.
# void_last_transaction Method:
# Removes the last item's cost from the total.
# Adjusts the items list and resets last_transaction to avoid double-voiding.
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {"title": title, "price": price, "quantity": quantity}

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
            for _ in range(self.last_transaction["quantity"]):
                self.last_transaction = None
