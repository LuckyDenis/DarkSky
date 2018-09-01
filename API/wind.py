# -*- coding: utf8 -*-


class WindBearing(object):
    """
    Converts degrees-wind direction (from degrees to direction).

    :g int(degrees)
    :return str(direction)
    """
    @staticmethod
    def convert(g):
        if not isinstance(g, int):
            raise TypeError(type(g))
        elif 337 <= g <= 360:
            return 'North'
        elif 0 <= g <= 22:
            return 'North'
        elif 22 < g < 67:
            return 'North-East'
        elif 67 <= g <= 112:
            return 'East'
        elif 112 < g < 157:
            return 'South-East'
        elif 157 <= g <= 202:
            return 'South'
        elif 202 < g < 247:
            return 'South-West'
        elif 247 <= g <= 292:
            return 'West'
        elif 292 < g < 337:
            return 'North-West'
