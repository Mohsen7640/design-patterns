from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Observer):

    @staticmethod
    def send(message=''):
        print(f'Sending Email Notification message: {message}')


class MobileNotification(Observer):

    @staticmethod
    def send(message=''):
        print(f'Sending Mobile Notification message: {message}')


class PushNotification(Observer):

    @staticmethod
    def send(message=''):
        print(f'Sending Push Notification message: {message}')
