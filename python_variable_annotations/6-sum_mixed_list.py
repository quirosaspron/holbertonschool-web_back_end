#!/usr/bin/env python3
"""Takes a list of numbers and sums them"""
from typing import List, Union


def sum_mixed_list(lista: List[Union[int, float]]) -> float:
    """Takes the list and outputs the sum"""
    return float(sum(lista))
