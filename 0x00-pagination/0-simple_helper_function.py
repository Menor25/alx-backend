#!/usr/bin/env python3
"""Defining a function called index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple containing a start index and an end index"""
    end = page * page_size
    start = end - page_size
    return(start, end)