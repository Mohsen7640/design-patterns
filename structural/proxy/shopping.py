from abc import ABC, abstractmethod


class DoPayment(ABC):

    @abstractmethod
    def do_payment(self):
        pass


class Bank(DoPayment):

    def __init__(self):
        self.card = None

    def set_card(self, card):
        self.card = card

    def inventory(self):
        print('Inventory is sufficient')
        return True

    def do_payment(self):
        if self.inventory():
            print('Do payment')
            return True
        else:
            print("Don't payment")
            return False


class Card(DoPayment):
    """Proxy"""

    def __init__(self):
        self.bank = Bank()

    def do_payment(self):
        card = '6037-1112-1211-1011'
        self.bank.set_card(card)
        return self.bank.do_payment()


class Purchase:
    """Client"""

    def __init__(self):
        self.card = Card()
        self.is_purchased = None

    def purchased(self):
        self.is_purchased = self.card.do_payment()

    def __del__(self):
        if self.is_purchased:
            print('Purchased Done.')
        else:
            print('Purchased Failed.')


if __name__ == '__main__':
    purchase = Purchase()
    purchase.purchased()
