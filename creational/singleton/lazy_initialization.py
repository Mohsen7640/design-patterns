class LazyInitialization:
    _instance = None

    def __init__(self):
        if not isinstance(LazyInitialization._instance, LazyInitialization):
            print('Object not created')
        else:
            print('Object created')

    @classmethod
    def create_object(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
