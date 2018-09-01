# -*- coding: utf8 -*-


import pytest
from API.wind import WindBearing


@pytest.mark.parametrize('g, answer', [
    (337, 'North'), (0, 'North'), (22, 'North'),
    (23, 'North-East'), (45, 'North-East'), (66, 'North-East'),
    (67, 'East'), (90, 'East'), (112, 'East'),
    (113, 'South-East'), (135, 'South-East'), (156, 'South-East'),
    (157, 'South'), (180, 'South'), (202, 'South'),
    (203, 'South-West'), (225, 'South-West'), (246, 'South-West'),
    (247, 'West'), (270, 'West'), (292, 'West'),
    (293, 'North-West'), (315, 'North-West'), (336, 'North-West')
])
def test_convert_north(g, answer):
    assert WindBearing.convert(g) == answer


def test_convert_error_type():
    with pytest.raises(TypeError):
        WindBearing.convert('123')
    with pytest.raises(TypeError):
        WindBearing.convert(int)
    with pytest.raises(TypeError):
        WindBearing.convert(123.123)
