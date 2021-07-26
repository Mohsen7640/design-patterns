class Logger:
    class __Singleton:

        def __init__(self):
            self.file_name = 'logger.txt'

        def _logger(self, msg, level):
            with open(file=self.file_name, mode='a') as file_handler:
                file_handler.write(f'[{level}] {msg}. \n')

        def critical(self, msg):
            self._logger(msg, level='Critical')

        def error(self, msg):
            self._logger(msg, level='Error')

        def warning(self, msg):
            self._logger(msg, level='Warning')

        def info(self, msg):
            self._logger(msg, level='Info')

        def debug(self, msg):
            self._logger(msg, level='Debug')

    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls.__Singleton):
            cls._instance = cls.__Singleton()

        return cls._instance
