COUNTRIES = ['Iran', 'UAE']
VAT = {'Iran': 9, 'UAE': 15}


def check_permission(function):
    def wrapper(obj, user):
        if obj.user == user:
            return function(obj)

        return 'You are not allowed to checkout'

    return wrapper


class User:
    pass


class Address:

    def __init__(self, country):
        self.country = country


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:

    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = list()

    def add_products(self, products_list):
        if not isinstance(products_list, list):
            products_list = [products_list]

        self.products_list.extend(products_list)

    def total_price(self):
        total_price_products = 0

        for product in self.products_list:
            total_price_products += product.price

        return total_price_products

    @check_permission
    def checkout(self):
        return 'Checkout Done!'


def show_total_price(purchase):
    return purchase.total_price()


def calculate_vat(function):
    def wrapper(purchase):
        vat = VAT[purchase.address.country]
        total_price = function(purchase)
        return total_price + (total_price * (vat / 100))

    return wrapper


@calculate_vat
def show_vat_plus_price(purchase):
    return purchase.total_price()


if __name__ == '__main__':
    customer = User()
    address_iran = Address(country=COUNTRIES[0])
    address_uae = Address(country=COUNTRIES[1])

    p1 = Product(name='Persian rugs', price=300)
    p2 = Product(name='Nain rugs', price=450)
    p3 = Product(name='Samsung A51', price=200)

    purchase_iran = Purchase(user=customer, address=address_iran)
    purchase_uae = Purchase(user=customer, address=address_uae)

    # print('Price:', show_total_price(purchase_iran))
    # print('Price plus vat:', show_vat_plus_price(purchase_iran))

    purchase_iran.add_products(p1)
    purchase_iran.add_products([p2, p3])

    # print('Price:', show_total_price(purchase_iran))
    # print('Price plus vat:', show_vat_plus_price(purchase_iran))
    #
    # print('Price:', show_total_price(purchase_uae))
    # print('Price plus vat:', show_vat_plus_price(purchase_uae))

    purchase_uae.add_products(p1)
    purchase_uae.add_products([p2, p3])

    # print('Price:', show_total_price(purchase_uae))
    # print('Price plus vat:', show_vat_plus_price(purchase_uae))

    print(purchase_iran.checkout(user=customer))
    print(purchase_uae.checkout(user=User()))
