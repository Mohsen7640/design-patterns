class Singleton:
    class __Singleton:

        def __init__(self):
            pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls.__Singleton)

        return cls._instance


class Singleton:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)

        return cls._instance
