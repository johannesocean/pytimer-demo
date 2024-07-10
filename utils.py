import time
from functools import wraps


def timer(func):
    """Decorator that times the execution of a function."""

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{func.__name__}: {total_time:.6f} s')
        return result
    return timeit_wrapper


def time_all_class_methods(cls):
    """A class decorator that times the execution of all class methods."""

    class Cls:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattribute__(self, attribute_name):
            try:
                attribute = super().__getattribute__(attribute_name)
            except AttributeError:
                pass
            else:
                return attribute

            attribute = self.instance.__getattribute__(attribute_name)
            if callable(attribute):
                return Timer(attribute)
            else:
                return attribute
    return Cls


class Timer:
    """Decorator that times the execution of functions.

    Reports the stats of all the decorated functions."""

    stats = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = self.func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            Timer.stats.setdefault(self.name, {'counter': 0, 'total_time': 0, 'avg_time': 0})
            Timer.stats[self.name]['counter'] += 1
            Timer.stats[self.name]['total_time'] += elapsed_time
            Timer.stats[self.name]['avg_time'] = (
                Timer.stats[self.name]['total_time'] / Timer.stats[self.name]['counter']
            )
        return result

    @property
    def name(self):
        return self.func.__name__

    @classmethod
    def report(cls):
        """Prints the stats of all the decorated functions.

        Can be extended to write to a file or replace the print statement with a logging statement.
        """
        for key, value in cls.stats.items():
            print(f"Function: {key}")
            print(f"Number of Calls: {value['counter']}")
            print(f"Total Time: {value['total_time']:.6f}s")
            print(f"Average Time: {value['avg_time']:.6f}s")
            print("-" * 50)

    @classmethod
    def reset_stats(cls):
        cls.stats = {}


class TimerV1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = self.func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"{self.func.__name__}: elapsed time: {elapsed_time:.6f} s")
        return result
