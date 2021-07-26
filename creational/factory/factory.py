# Factory Method in python

from abc import ABC, abstractmethod
from random import choice


class PlayerBase(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def choice(self):
        pass


class HumanPlayer(PlayerBase):

    def choice(self):
        user_choice = input('Please your choice[r, p, s]: ')
        return f'Human choice: {user_choice}'


class SystemPlayer(PlayerBase):

    def choice(self):
        return f'System choice: {choice(self.choices)}'


class Game:
    """Factory"""
    @staticmethod
    def run():
        game_type = input(
            'Please choice game type("s" single or "m" multiply player): '
        )

        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print('Invalid input')
            return Game.run()

        return p1, p2


if __name__ == '__main__':
    """Client"""
    player_1, player_2 = Game.run()

    for player in [player_1, player_2]:
        print(player.choice())
