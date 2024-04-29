def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1
    return generator

def double(x):
    return x * 2

def fib(x):
    if x < 2:
        return 1
    return fib(x - 1) + fib(x - 2)

if __name__ == "__main__":
    gen_d = make_generator(double)
    gen_f = make_generator(fib)

    generator_d = gen_d()
    generator_f = gen_f()

    for _ in range(10):
        print(next(generator_d))

    for _ in range(10):
        print(next(generator_f))