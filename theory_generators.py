# Turn a regular function into a generator using the yield keyword
# The output is a generator object called odds

def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd 

# The output pauses at each iteration
# To get the next number, g = odds(1,7)
# next(g) repeatedly >> 1 >> 3 >> 5 >> 7 >> stop traceback error
# or use a constructor eg: list(g) >> [1,3,5,7]
# or manually use a for loop


def main():
    # Use FOR loops manually
    odd_list_manual = [odd for odd in odds(3,15)]
    print(odd_list_manual)

    # Use list constructor
    generator1 = odds(1,5)
    odd_list = list(generator1)
    print(odd_list)

    # When a constructor is exhausted, you will have to regenerate it again otherwise it returns empty
    odd_list2 = list(generator1)
    print(odd_list2)

    # Use tuple constructor
    generator2 = odds(7,21) 
    odd_tuple = tuple(generator2)
    print(odd_tuple)

if __name__ == "__main__":
    main()