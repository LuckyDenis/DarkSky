# -*- coding: utf8 -*-


import pytest
from API.OptionsAPI import Options
from API.get import Request

# Your api key from run test
Options.key = None

if Options.key is not None:
    def test_not_lat_not_lon():
        with pytest.raises(TypeError):
            assert Request.answer()

    def test_error_lat():
        with pytest.raises(TypeError):
            Request.answer(-78, 106.8)

    def test_error_lon():
        with pytest.raises(TypeError):
            Request.answer(-78.467, 106)

    def test_answer():
        assert isinstance(Request.answer(-78.467, 106.8), dict)

    def test_answer_param():
        assert isinstance(Request.answer(-78.467, 106.8, lang='ru'), dict)

        p = {'lang': 'ru'}
        assert isinstance(Request.answer(-78.467, 106.8, **p), dict)

    def test_error_key():
        temp = Options.key
        Options.key = '123'
        with pytest.raises(TypeError):
            Request.answer(-78.467, 106.8)
        Options.key = temp
