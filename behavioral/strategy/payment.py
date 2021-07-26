class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Gateway:

    def __init__(self, name):
        self.name = name


class Payment:
    gateway = (Gateway('G1'), Gateway('G2'))

    def __init__(self, purchase):
        self.purchase = purchase

    def gate_way(self):
        """Strategy"""
        """If payment amount is less than 100,
        use G1 gateway otherwise use G2"""
        return Payment.gateway[0] if self.purchase.total_price() < 100 else \
            Payment.gateway[1]

    def pay(self):
        gateway = self.gate_way()
        print(f'Payment is begin paid through: {gateway.name}')


class Purchase:

    def __init__(self):
        self.products_list = list()
        self.payment = Payment(self)

    def add_product(self, product):
        self.products_list.append(product)

    def total_price(self):
        return sum([product.price for product in self.products_list])

    def checkout(self):
        self.payment.pay()


if __name__ == '__main__':
    p1 = Product('Book', 40)
    p2 = Product('Mobile', 30)
    p3 = Product('Gift card', 60)

    purchased = Purchase()

    purchased.add_product(p1)
    print(purchased.total_price())
    purchased.checkout()

    purchased.add_product(p2)
    print(purchased.total_price())
    purchased.checkout()

    purchased.add_product(p3)
    print(purchased.total_price())
    purchased.checkout()
