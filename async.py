import asyncio

async def say_after(delay, what):
    # print("what is this")
    await asyncio.sleep(delay)
    print(what)

async def main():
    print('Started')

    await say_after(1, 'Hello')
    
    await say_after(2, 'World')

    print('Finished')

asyncio.run(main())
