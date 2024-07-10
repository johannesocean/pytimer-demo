import time
import random

from utils import Timer, time_all_class_methods


@Timer
def timer_class_test_func_1():
    # sleep for a random time between 0 and 1 seconds
    time.sleep(random.uniform(0, 1))


@Timer
def timer_class_test_func_2():
    # sleep for a random time between 1 and 2 seconds
    time.sleep(random.uniform(1, 2))


@time_all_class_methods
class TimerClassTest:
    def __init__(self, name):
        self.name = name

    def test_method(self, *args, **kwargs):
        time.sleep(random.uniform(0, 1))

    def test_method_2(self, *args, **kwargs):
        time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    # timer_class_test_func_1()
    # timer_class_test_func_2()
    #
    # timer_class_test_func_1()
    # timer_class_test_func_2()

    timer_class_test = TimerClassTest('timer_class_test')
    timer_class_test.test_method_2()
    timer_class_test.test_method()
    Timer.report()
