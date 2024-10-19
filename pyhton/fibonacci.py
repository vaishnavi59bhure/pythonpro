def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter number:\t"))
fibonacci_series = [fibonacci(n) for n in range(num)]
print(fibonacci_series)