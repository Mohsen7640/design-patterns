from time import sleep


class LazyLoader:

    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __getattr__(self, item):
        if self.instance is None:
            self.instance = self.cls()

        return getattr(self.instance, item)


class MySQLHandler:
    def __init__(self):
        sleep(3)

    def get(self):
        return 'Hello From MySQL'


class MongoHandler:
    def __init__(self):
        sleep(4)

    def get(self):
        return 'Hello From Mongo'


class NotificationCenterHandler:
    def __init__(self):
        sleep(4)

    def get(self):
        return 'Hello From Notification'


if __name__ == '__main__':
    mysql = LazyLoader(MySQLHandler)
    mongo = LazyLoader(MongoHandler)
    notification = LazyLoader(NotificationCenterHandler)

    print(mysql.get())
    print(notification.get())
