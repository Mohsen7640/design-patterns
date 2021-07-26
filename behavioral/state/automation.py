from abc import ABC, abstractmethod


class Message:

    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_user):
        """State"""
        if to_user.__class__ not in self.current.allowed:
            print(f'{self.current.__class__} is not allowed to '
                  f'send message to {to_user.__class__}')
        else:
            print(f'{self.current.__class__} is allowed to '
                  f'send message to {to_user.__class__}')
            self.flow.append(to_user)


class User(ABC):

    @property
    @abstractmethod
    def allowed(self):
        pass


class ManagingDirector(User):
    allowed = []


class InternalManager(User):
    allowed = [ManagingDirector]


class Supervisor(User):
    allowed = [InternalManager]


class Operator(User):
    allowed = [Supervisor]


class Client(User):
    allowed = [Operator]


if __name__ == '__main__':
    managing_director = ManagingDirector()
    internal_manager = InternalManager()
    supervisor = Supervisor()
    operator = Operator()

    client = Client()

    message = Message(
        subject='Issue #0032',
        body='Description Issue',
        sender=client
    )

    message.send(operator)
    message.send(internal_manager)
    message.send(supervisor)
    message.send(internal_manager)
    message.send(supervisor)
    message.send(managing_director)
