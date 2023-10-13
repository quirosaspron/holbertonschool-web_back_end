#!/usr/bin/env python3
"""Turns a str and a num and makes them a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a str and num, outputs tuple"""
    return (k, float(v*v))
