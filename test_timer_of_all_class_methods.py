import time
import random

from utils import Timer, time_all_class_methods


@time_all_class_methods
class TimerClassTest:

    def test_method_1(self):
        time.sleep(random.uniform(0, 1))

    def test_method_2(self):
        time.sleep(random.uniform(0, 1))

    def test_method_3(self):
        time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    timer_class_methods_test = TimerClassTest()

    timer_class_methods_test.test_method_1()

    timer_class_methods_test.test_method_2()
    timer_class_methods_test.test_method_2()

    timer_class_methods_test.test_method_3()

    Timer.report()
