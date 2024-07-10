import time
import random

from utils import Timer


@Timer
def timer_class_test_func_1():
    # sleep for a random time between 0 and 1 seconds
    time.sleep(random.uniform(0, 1))


@Timer
def timer_class_test_func_2():
    # sleep for a random time between 1 and 2 seconds
    time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    timer_class_test_func_1()
    timer_class_test_func_2()

    timer_class_test_func_1()
    timer_class_test_func_2()

    Timer.report()
