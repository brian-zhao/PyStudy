from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(
                    *args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    # We'll use this property to prove that our Singleton really works.
    value = None

    def __init__(self, value):
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        pass
        # print('Singleton Pattern')


def test_singleton(value):
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
