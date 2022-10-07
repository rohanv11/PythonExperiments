import asyncio

async def bar():
    print("Rohan")
    task = asyncio.create_task(foo("Danish"))
    await asyncio.sleep(2)
    print("Finish")

async def foo(name):
    print(name)
    await asyncio.sleep(10)

asyncio.run(bar())

