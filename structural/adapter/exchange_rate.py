from creational.factory.abstract_factory import Rugs, Mobile


class AdapterExchange:

    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product.price


if __name__ == '__main__':
    r1 = Rugs('persian rugs', 60, 'Car transport')
    r2 = Rugs('nain rugs', 75, 'Shipping transport')

    m1 = Mobile('Samsung', 'A51', 400, 'Motor transport')
    m2 = Mobile('Apple', 'X12 Pro', 900, 'Car transport')

    adapter = AdapterExchange(rate=23)

    products = [r1, r2, m1, m2]

    for product in products:
        print(
            f'{product.get_detail.show()} - Price: {adapter.exchange(product)}'
        )
