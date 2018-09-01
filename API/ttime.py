# -*- coding: utf8 -*-

from time import strftime
from time import gmtime

__all__ = ['ConvertTime']


class ConvertTime(object):

    @staticmethod
    def convert(t, f=None):
        """
        Convert time.

        Convert time from int into
        a string using the specified format.

        :param t: time.time() must type: int
        :param f: format time, must type: str, default = '%a, %d %b %Y %H:%M:%S'
        :return 'Thu Sep 27 16:42:37 2012', type: str
        """

        if not isinstance(t, int):
            raise TypeError()
        format_ = f or '%a, %d %b %Y %H:%M:%S'
        if not isinstance(format_, str):
            raise TypeError()
        return strftime(format_, gmtime(t))
