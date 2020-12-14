from datetime import datetime

def time_dec(func):
    print ("RUNTIME DECOR")

    def _handler(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print ("time - {}".format(datetime.now() - start))
        return res
    return _handler

print(__name__)

def test_f(*args, **kwargs):
    print (f"args - {args}")
    print (f"kwargs - {kwargs}")

if __name__ == "__main__":
    print("MAIN")