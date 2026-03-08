from enum import Enum
class OrderStatus(Enum):
    SHIPPED = '3'
    CONFIRMED = 'CONFIRMED'
    PLACED = 'PLACED'
    CANCELLED = 'CANCELLED'
    DELIVERED  = 'DELIVERED'
    
    
# print(OrderStatus)
# print(OrderStatus.CANCELLED.value)

# order = OrderStatus.SHIPPED
# print(order)
# print(order.value)
# print(order.name)
print(OrderStatus['3'])