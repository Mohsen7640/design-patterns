from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_transport(self):
        pass


class Rugs(Product):

    def __init__(self, name, price, transport):
        self.name = name
        self.price = price
        self.transport = transport

    @property
    def get_detail(self):
        return f'Rugs name: {self.name}'

    @property
    def get_price(self):
        return f'Rugs price: {self.price}$'

    @property
    def get_transport(self):
        return f'Rugs transport: {self.transport}'


class Mobile(Product):

    def __init__(self, brand, model, price, transport):
        self.brand = brand
        self.model = model
        self.price = price
        self.transport = transport

    @property
    def get_detail(self):
        return f'Mobile brand: {self.brand},' \
               f' Mobile model: {self.model}'

    @property
    def get_price(self):
        return f'Mobile price: {self.price}$'

    @property
    def get_transport(self):
        return f'Mobile transport: {self.transport}'


class GiftCard(Product):

    def __init__(self, company, min_price, max_price, transport):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
        self.transport = transport

    @property
    def get_detail(self):
        return f'Gift Card company: {self.company}'

    @property
    def get_price(self):
        return f'Gift Card min price: {self.min_price}$, ' \
               f'max price: {self.max_price}$'

    @property
    def get_transport(self):
        return f'Gift Card transport: {self.transport}'


if __name__ == '__main__':
    r1 = Rugs('persian rugs', 300, 'Car transport')
    r2 = Rugs('nain rugs', 600, 'Shipping transport')

    m1 = Mobile('Samsung', 'A51', 1200, 'Motor transport')
    m2 = Mobile('Apple', 'X12 Pro', 1500, 'Car transport')

    g1 = GiftCard('google', 50, 100, 'SMS')
    g2 = GiftCard('apple', 100, 220, 'Motor transport')

    products = [r1, r2, m1, m2, g1, g2]

    for product in products:
        print(product.get_detail)
        print(product.get_price)
        print(product.get_transport)
        print('#' * 30)
