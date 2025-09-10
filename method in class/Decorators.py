import time
def timing_decorator(func):
    # we add wrapper cuz we dont want to timing_decorator started when we dont call slow_function
    def wrapper():
        start=time.time()
        func()
        endtime=time.time()
        print(f"Execution time: {endtime - start} seconds")
    return wrapper

# we use derecorator for modify function behavior
@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function finished!")

slow_function()