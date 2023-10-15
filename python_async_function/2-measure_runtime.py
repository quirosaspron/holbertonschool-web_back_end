#!/usr/bin/env python3
"""Measures the time it takes to execute a corutine"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the time it takes to run wait_n n times"""
    start_time = time.time()
    #asyncio.run(wait_n(n, max_delay))
    await asyncio.gather(*[wait_n(1, max_delay) for _ in range(n)])
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
