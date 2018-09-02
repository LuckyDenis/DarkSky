# -*- coding: utf8 -*-

import pytest
import time
from API.ttime import ConvertTime


def test_input():
    t = ConvertTime.convert(int(time.time()))
    assert t == time.strftime('%a, %d %b %Y %H:%M:%S', time.gmtime(int(time.time())))


@pytest.mark.parametrize('f', ['%A, %S', '%H:%M', '%B', '%a, %b, %c'])
def test_format(f):
    t = ConvertTime.convert(int(time.time()), f)
    assert t == time.strftime(f, time.gmtime((int(time.time()))))


def test_error_type_time():
    with pytest.raises(TypeError):
        ConvertTime.convert('')


def test_error_type_format():
    with pytest.raises(TypeError):
        ConvertTime.convert(int(time.time()), 123)
