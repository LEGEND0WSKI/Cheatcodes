import time
"""
    Decorator function to measure the execution time of the input function.
"""
def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"{func.__name__} took {t2} seconds")
    return wrapper

@tictoc
def do_this():
    print("do this")
    time.sleep(1.3)

@tictoc
def do_that():
    print("do that")
    time.sleep(0.5) 

do_this()
do_that()
print("Done")

