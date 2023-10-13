#!/usr/bin/env python3
"""Turns a str and a num and makes them a tuple"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Takes a str and num, outputs tuple"""
    return (k, float(v*v))
