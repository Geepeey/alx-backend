#!/usr/bin/env python3
"""
A method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""
    start = 0
    stop = 0

    for i in range(1, page + 1):
        if i == page:
            start = page_size * (i - 1)
            stop = start + page_size
    return (start, stop)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the items in a page of the dataset"""
        assert (type(page) is int and page > 0)
        assert (type(page_size) is int and page_size > 0)
        data = self.dataset()

        try:
            p = index_range(page, page_size)[0]
            size = index_range(page, page_size)[1]
            return data[p: size]
        except IndexError:
            return []
