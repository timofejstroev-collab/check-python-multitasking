import asyncio
import time

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

def factorial_worker(n, results, index):
    results[index] = factorial_sync(n)

def factorial_without_gil(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        time.sleep(0.0001)  # Спим, отдаём GIL другим потокам
    return result


n = int(input())

print(factorial_sync(n))
print(asyncio.run(factorial_async(n)))
print(factorial_without_gil(n))