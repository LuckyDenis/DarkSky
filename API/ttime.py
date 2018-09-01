# -*- coding: utf8 -*-

from time import strftime
from time import gmtime

__all__ = ['ConvertTime']


class ConvertTime(object):
    """
    Convert time

    Convert time from int into a string using the specified format.

    :t int(time.time())
    :f str(), default = '%a, %d %b %Y %H:%M:%S'
    """
    @staticmethod
    def convert(t, f=None):
        if not isinstance(t, int):
            raise TypeError()
        format_ = f or '%a, %d %b %Y %H:%M:%S'
        if not isinstance(format_, str):
            raise TypeError()
        return strftime(format_, gmtime(t))
