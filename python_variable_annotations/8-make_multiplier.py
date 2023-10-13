#!/usr/bin/env python3
"""Multiplies a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
