from payment import Payment, Credit, Check
from order import Order

class Customer:
    def __init__(self, full_name, address, orders = None):
        self.full_name = full_name
        self.address = address
        if orders is None:
            self.orders = []
        else:
            self.orders = orders

    def place_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f'{"="*20}\nFull Name: {self.full_name}\nAddress: {self.address}' \
               f'\nOrders:\n{(["-" + str(order) for order in self.orders])}\n' \
               f'Total Credit: {sum(o.payment.total for o in self.orders)}$\n{"="*20}'


p1 = Payment(300)
p2 = Credit(200, 250020213123, '09/25')
p3 = Check(100, 2314890, '32323214')
o1 = Order('20220107', p1)
o2 = Order('20223006', p2)
o3 = Order('20222706', p3)
orders_list = [o1, o2, o3]
joe = Customer('Joe Doe', 'Arachosias 8', orders_list)
print(joe)