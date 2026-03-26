orders = [
    {"order_id": 1, "price": 50, "quantity": 23},
    {"order_id": 2, "price": -10, "quantity": 1},
    {"order_id": 3, "price": 30, "quantity": 0},
    {"order_id": 4, "price": 20, "quantity": 3}
]

def is_valid_order(order):
    return order.get("price", 0) > 0 and order.get("quantity", 0) > 0

valid_orders = list(filter(is_valid_order, orders))


for order in valid_orders:
    order["total_value"] = order["price"] * order["quantity"]
    print(
        f"Order Id: {order['order_id']}, "
        f"Price: {order['price']}, "
        f"Quantity: {order['quantity']}, "
        f"Total Value: {order['total_value']}"
    )
