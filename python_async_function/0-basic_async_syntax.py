#!/usr/bin/env python3
"""Takes and int waits, and then returns it"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """Generates a random number waits and returns max_delay"""
    random_number = random.uniform(0.0, upper_bound)
    await asyncio.sleep(random_number)
    return max_delay
