from abc import ABC, abstractmethod


class ProductBase(ABC):

    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_transport(self):
        pass


class DetailBase(ABC):

    @abstractmethod
    def show(self):
        pass


class PriceBase(ABC):

    @abstractmethod
    def show(self):
        pass


class TransportBase(ABC):

    @abstractmethod
    def show(self):
        pass


class RugsDetail(DetailBase):

    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f'Rugs name: {self.rugs.name}'


class RugsPrice(PriceBase):

    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f'Rugs price: {self.rugs.price}$'


class RugsTransport(TransportBase):

    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f'Rugs transport: {self.rugs.transport}'


class MobileDetail(DetailBase):

    def __init__(self, mobile):
        self.mobile = mobile

    def show(self):
        return f'Mobile brand: {self.mobile.brand},' \
               f' Mobile model: {self.mobile.model}'


class MobilePrice(PriceBase):

    def __init__(self, mobile):
        self.mobile = mobile

    def show(self):
        return f'Mobile price: {self.mobile.price}$'


class MobileTransport(TransportBase):

    def __init__(self, mobile):
        self.mobile = mobile

    def show(self):
        return f'Mobile transport: {self.mobile.transport}'


class GiftCardDetail(DetailBase):

    def __init__(self, gift_card):
        self.gift_card = gift_card

    def show(self):
        return f'Gift Card company: {self.gift_card.company}'


class GiftCardPrice(PriceBase):

    def __init__(self, gift_card):
        self.gift_card = gift_card

    def show(self):
        return f'Gift Card min price: {self.gift_card.min_price}$, ' \
               f'max price: {self.gift_card.max_price}$'


class GiftCardTransport(TransportBase):

    def __init__(self, gift_card):
        self.gift_card = gift_card

    def show(self):
        return f'Gift Card transport: {self.gift_card.transport}'


class Rugs(ProductBase):

    def __init__(self, name, price, transport):
        self.name = name
        self.price = price
        self.transport = transport

    @property
    def get_detail(self):
        return RugsDetail(self)

    @property
    def get_price(self):
        return RugsPrice(self)

    @property
    def get_transport(self):
        return RugsTransport(self)


class Mobile(ProductBase):

    def __init__(self, brand, model, price, transport):
        self.brand = brand
        self.model = model
        self.price = price
        self.transport = transport

    @property
    def get_detail(self):
        return MobileDetail(self)

    @property
    def get_price(self):
        return MobilePrice(self)

    @property
    def get_transport(self):
        return MobileTransport(self)


class GiftCard(ProductBase):

    def __init__(self, company, min_price, max_price, transport):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
        self.transport = transport

    @property
    def get_detail(self):
        return GiftCardDetail(self)

    @property
    def get_price(self):
        return GiftCardPrice(self)

    @property
    def get_transport(self):
        return GiftCardTransport(self)


if __name__ == '__main__':
    r1 = Rugs('persian rugs', 300, 'Car transport')
    r2 = Rugs('nain rugs', 600, 'Shipping transport')

    m1 = Mobile('Samsung', 'A51', 1200, 'Motor transport')
    m2 = Mobile('Apple', 'X12 Pro', 1500, 'Car transport')

    g1 = GiftCard('google', 50, 100, 'SMS')
    g2 = GiftCard('apple', 100, 220, 'Motor transport')

    products = [r1, r2, m1, m2, g1, g2]

    for product in products:
        print(product.get_detail.show())
        print(product.get_price.show())
        print(product.get_transport.show())
        print('#' * 30)
