import time


class RawCalculator:
    def fib(self, n):
        if n < 2:
            return 1


def memoize(fn):
    __cache = {}

    def memoized(*args):
        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]

        __cache[key] = fn(*args)
        return __cache[key]

    return memoized


class CalculatorProxy:
    def __init__(self, target) -> None:
        self.target = target

        fib = getattr(self.target, "fib")
        setattr(self.target, "fib", memoize(fib))

    def __getattr__(self, name):
        return getattr(self.target, name)


if __name__ == "__main__":
    calculator = CalculatorProxy(RawCalculator())

    start_time = time.time()
    fib_sequence = [calculator.fib(x) for x in range(0, 80)]
    end_time = time.time()

    print(
        f"Calculating the list of {len(fib_sequence)} Fibonacci numbers took {end_time - start_time} seconds"
    )
