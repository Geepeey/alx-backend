#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        all_data = self.dataset()
        data = self.get_page(page, page_size)
        ps = len(data)
        total_pages = math.ceil(len(all_data) / page_size)
        p, n = index_range(page, page_size)
        prev_page = page - 1
        next_page = page + 1

        if p <= 0:
            prev_page = None
        elif n > len(all_data):
            next_page = None

        return {'page_size': ps,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}
