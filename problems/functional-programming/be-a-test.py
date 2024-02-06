def gen_fn(c):
        def fn(x):
            return x % c == 0
        return fn

print("Result:")
print(list(filter(gen_fn(10), map(lambda x: x * 2, [10, 25, -10, 18, -9]))))
print(list(map(lambda x: x * 2, filter(gen_fn(5), [10, 25, -10, 100, -9]))))