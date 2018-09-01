# -*- coding: utf8 -*-


import requests
from API.OptionsAPI import Options


__all__ = ['Request']


class Request(object):
    @classmethod
    def answer(cls, lat, lon, **kwargs):
        """
        A request to the API site.

        Allows you to send a request with parameters,
        returns a response in json format.

        :param lat: latitude, must type float
        :param lon: longitude, must type: float
        :param kwargs: options, must type: dict
        :return: request answer, type: json
        """

        if not isinstance(Options.key, str):
            raise TypeError()
        if not isinstance(lat, float):
            raise TypeError()
        if not isinstance(lon, float):
            raise TypeError()
        s = 'https://api.darksky.net/forecast/{!s}/{!s},{!s}'.format(Options.key, lat, lon)
        with requests.get(s, timeout=Options.timeout, params=kwargs) as r:
            if r.ok:
                return r.json()
