import re
import pytest
from password_generator.password_generator import password_generator

class TestPasswordGenerator:
    def test_parameter_error(self):
        length="blabla"
        with pytest.raises(ValueError):
            password_generator(length=length)
    def test_parametr_ok(self):
        length=12
        password_generator(length=length)
    def test_upper_symbols_ok(self):
        password=password_generator(length=12)
        pattern = re.compile("[A-Z]+")
        assert pattern.search(password)
    def test_lower_symbols_ok(self):
        password = password_generator(length=12)
        pattern = re.compile("[a-z]+")
        assert pattern.search(password)
    def test_numbers_symbols_ok(self):
        password = password_generator(length=12)
        pattern = re.compile("[0-9]+")
        assert pattern.search(password)
    def test_special_simbols_ok(self):
        pattern = re.compile('[^A-Za-z0-9]+')
        password = password_generator(length=12)
        assert pattern.search(password)





