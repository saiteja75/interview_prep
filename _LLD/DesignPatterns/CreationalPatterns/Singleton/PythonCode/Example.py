class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Logger(metaclass=SingletonMeta):
    count_debug = 0
    
    def __init__(self) -> None:
        print('entered')

    
    def debug(self,data):
        self.count_debug+=0
        print('DEBUG',data)

    def error(self,data):
        print('ERROR',data)


log = Logger()
log_1 = Logger()
log.debug('Hello World')
log_1.debug('Testing')
print(log.count_debug)
print(log_1.count_debug)
