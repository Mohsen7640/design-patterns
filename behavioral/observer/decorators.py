def notify_observer(message=''):
    def decorated_method(function):
        def wrapper(obj, *args, **kwargs):
            result = function(obj, *args, **kwargs)
            for observer in obj.observers:
                observer.send(message)

            return result

        return wrapper

    return decorated_method
