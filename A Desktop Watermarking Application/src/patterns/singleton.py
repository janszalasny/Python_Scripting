# src/patterns/singleton.py

import threading

class SingletonMeta(type):
    """
    A thread-safe metaclass for creating Singleton classes.
    This ensures that only one instance of a class exists throughout the
    application's lifecycle.
    """
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # The lock ensures that the instance is created only once in a
        # multi-threaded environment.
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]