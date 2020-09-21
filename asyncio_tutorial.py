import asyncio
from datetime import datetime


async def sleep(delay, message):
    print(message)
    await asyncio.sleep(delay)


async def main():
    task_1 = asyncio.create_task(sleep(1, 'Hello'))
    task_2 = asyncio.create_task(sleep(2, 'World'))
    print('Start', datetime.now())

    await task_1
    await task_2

    print('Finish', datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
