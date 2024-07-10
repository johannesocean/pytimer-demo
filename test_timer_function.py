import time
import random

from utils import timer


@timer
def timer_func_test_func_1():
    # sleep for a random time between 0 and 1 seconds
    time.sleep(random.uniform(0, 1))


@timer
def timer_func_test_func_2():
    # sleep for a random time between 1 and 2 seconds
    time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    timer_func_test_func_1()
    timer_func_test_func_2()

    timer_func_test_func_1()
    timer_func_test_func_2()
