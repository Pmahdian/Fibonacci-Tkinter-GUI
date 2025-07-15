# fibo_utils.py

def generate_fibonacci(n):
    if n <= 0:
        raise ValueError("Number must be positive")

    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
