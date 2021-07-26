from behavioral.observer.notification import (EmailNotification,
                                              MobileNotification,
                                              PushNotification)

from behavioral.observer.decorators import notify_observer


class Product:
    pass


class Payment:
    observers = [EmailNotification, PushNotification]

    @notify_observer(message='Purchase paid')
    def checkout(self):
        pass


class Purchase:
    observers = [EmailNotification, MobileNotification, PushNotification]

    def __init__(self, products_list):
        self.products = products_list
        self.payment = Payment()

    def checkout(self):
        self.payment.checkout()

    @notify_observer(message='Purchase canceled')
    def cancel(self):
        pass
