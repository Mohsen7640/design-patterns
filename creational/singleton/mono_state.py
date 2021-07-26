class MonoState:
    """
    Same state object
    """
    state = {}

    @classmethod
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__ = cls.state

        return instance


class MonoState:
    """
    Same state object
    """
    state = {}

    def __init__(self):
        self.__dict__ = self.state
