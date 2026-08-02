def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        yield a

        next_b = a + b
        a = b
        b = next_b

def main():

    # Use list constructor
    fib = fibonacci(8)
    fibonacci_list = list(fib)
    print(fibonacci_list)


if __name__ == "__main__":
    main()