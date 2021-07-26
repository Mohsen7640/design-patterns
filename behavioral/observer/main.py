from behavioral.observer.shop import Product, Purchase

if __name__ == '__main__':
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()

    products = [p1, p2, p3, p4]
    purchase = Purchase(products_list=products)

    purchase.checkout()

    purchase.cancel()
