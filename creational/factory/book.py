# Simple Factory in python

from abc import ABC, abstractmethod


class Book(ABC):

    @abstractmethod
    def number_of_pages(self):
        pass


class HeadFirstPython(Book):

    def number_of_pages(self):
        return 500


class CleanCode(Book):

    def number_of_pages(self):
        return 800


class PublicationFactory:

    @staticmethod
    def book_public(obj):
        return eval(obj)().number_of_pages()


if __name__ == '__main__':
    print(PublicationFactory.book_public('CleanCode'))
    print(PublicationFactory.book_public('HeadFirstPython'))
