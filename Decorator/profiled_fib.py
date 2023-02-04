import time
from functools import wraps


def profile(f):
    @wraps(f)
    def wrap_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"time elapsed = {elapsed_time}")

        return result

    return wrap_f


@profile
def fib(n):
    if n < 2:
        return

    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev

    return fib


if __name__ == "__main__":
    n = 20
    print(f"fib20 = {fib(20)}")
