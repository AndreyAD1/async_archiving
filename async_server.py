import asyncio
from datetime import datetime


async def archive():
    command = 'zip -r - test_data'
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE
    )
    while True:
        archived_data = await process.stdout.read(100 * 1024)
        if not archived_data:
            break
        with open('archive.zip', 'ab') as archive_file:
            archive_file.write(archived_data)
    await process.wait()


async def main():
    task_1 = asyncio.create_task(archive())
    print('Start', datetime.now())

    await task_1

    print('Finish', datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
