class Database:
    def work(self):
        print('you are admin so you can work with database...')


class Proxy:
    admin_password = 'secret'

    def check_admin(self, password):
        if password == self.admin_password:
            database = Database()
            database.work()
        else:
            print('You are not admin so you cant work with database...')


proxy = Proxy()
proxy.check_admin('secret')
