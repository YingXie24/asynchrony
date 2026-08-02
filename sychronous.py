# Synchronous function

import time

def count():
    print("One")
    time.sleep(1)

    print("Two")
    time.sleep(1)

def main():
    for i in range(3): #Run count function 3 times
        count()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"The file executed in {elapsed} seconds.")


# One
# Two
# One
# Two
# One
# Two
# The file executed in 6.020585744001437 seconds.