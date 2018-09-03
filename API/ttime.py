# -*- coding: utf8 -*-

from datetime import datetime
import pytz

__all__ = ['Time']


class Time(object):

    @staticmethod
    def convert(t, f=None, tz=None):
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
        d = datetime.fromtimestamp(t)
        if isinstance(tz, str):
            d = d.astimezone(pytz.timezone(tz))
        return d.strftime(format_)

    @staticmethod
    def get_timezone(request_json):
        """
        Takes the timezone from the request.

        :param request_json: request (DarkSky.net), format: dict
        :return: example: 'Europe/Moscow', format: str
        """
        if 'timezone' in request_json:
            return request_json['timezone']
