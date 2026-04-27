import asyncio

def factorial_sync(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

async def factorial_async(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        await asyncio.sleep(0)
    return result

n = int(input())

print(factorial_sync(n))
print(asyncio.run(factorial_async(n)))