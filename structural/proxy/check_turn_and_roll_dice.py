import random


def check_turn_and_roll_dice(function):
    def wrapper(obj, player):
        if obj.turn == player:
            obj.change_turn()
            return function(obj)
        return "It's not your turn"

    return wrapper


class Player:
    pass


class Dice:

    @staticmethod
    def roll():
        return random.randint(1, 6)


class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = player_1
        self.dice = Dice

    def change_turn(self):
        self.turn = player2 if self.turn == self.player_1 else self.player_1

    @check_turn_and_roll_dice
    def roll_dice(self):
        return self.dice.roll()


if __name__ == '__main__':
    player1 = Player()
    player2 = Player()

    game = Game(player1, player2)

    print(game.roll_dice(player2))
    print(game.roll_dice(player1))
    print(game.roll_dice(player1))
    print(game.roll_dice(player2))
    print(game.roll_dice(player2))
    print(game.roll_dice(player1))
    print(game.roll_dice(player2))
