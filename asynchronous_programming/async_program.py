import asyncio

async def say_hello():
    print("Aksh")
    await asyncio.sleep(2)  # Simulating an I/O-bound task
    print("Patel")

async def birthday_wish():
    print("Happy")
    # await asyncio.sleep(0.1)  # Simulating an I/O-bound task
    print("Birthday!")

async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(birthday_wish())

    # Running both tasks concurrently
    await task1
    await task2

# Running the main function using the event loop
asyncio.run(main())
