from lib import lib1
from lib.lib2 import test_f

@lib1.time_dec
def summator(n):
    res = sum([*range(n)])

@lib1.time_dec
def func2(a, b, c, value = 500):
    return a * b + c / value

if __name__ == "__main__":
    lib1.test_f(1, 2, "str", default="String", flag=False)
    summator(10000)
    func2(3, 5, 7)
    func2(3, 5, 7, value = 100)