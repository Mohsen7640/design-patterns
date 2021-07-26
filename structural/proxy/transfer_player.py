class Player:

    def __init__(self):
        self.has_contract = False

    def occupied(self):
        self.has_contract = True
        print('Player occupied')

    def available(self):
        self.has_contract = False
        print('Player available')

    def get_status(self):
        return self.has_contract


class Agent:

    def __init__(self):
        self.player = None

    def work(self):
        self.player = Player()

        if self.player.get_status():
            self.player.occupied()
        else:
            self.player.available()


if __name__ == '__main__':
    agent = Agent()
    agent.work()
