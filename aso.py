import asyncio


async def func():
    print("In the function")
    await func2()
    print('xdx')

async def func2():
    print("2nd func")
    await asyncio.sleep(5)
    print('xd')

async def test():
    task = asyncio.create_task(func2())
    print("Smtg else")
    await task
    print("Done")


async def main():
    await func()
    await asyncio.gather(
        func(),
        test()
    )

asyncio.run(main())
