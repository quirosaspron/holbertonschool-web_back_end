#!/usr/bin/env python3
""" Pagination """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns tuple of size two containing a start index and an end index """
    if page < 1 or page_size < 1:
        return None

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return (start_index, end_index)
