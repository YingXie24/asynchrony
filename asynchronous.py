import asyncio

async def count(): # Use async keyword to turn count() function into a coroutine function
    print("One")
    await asyncio.sleep(1) # Use await keyword to await the execution of asyncio.sleep(). This gives control to the event loop
    print("Two")
    await asyncio.sleep(1)

async def main(): # Use async keyword to turn main() into another coroutine function
    await asyncio.gather(count(), count(), count()) # asyncio.gather() runs the 3 instances of count() concurrrently

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    asyncio.run(main()) # Use asyncio.run() to launch the event loop and execute main()
    elapsed = time.perf_counter() - start
    print(f"The file executed in {elapsed} seconds.")

# One
# One
# One
# Two
# Two
# Two
# The file executed in 2.002697490999708 seconds.