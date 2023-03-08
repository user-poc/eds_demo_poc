import pytest
import allure
from datetime import datetime, timedelta


@allure.suite("TestPytestFeatures")
class TestPytestFeatures:
    def test_skip(self):
        """this test is skipped"""
        pytest.skip('skipped for demo!')

    def test_broken(self):
        raise Exception('oops')

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_the_unknown(self):
        print("skipped test case")

    testdata = [
        (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
        (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
    ]

    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_timedistance_v0(self, a, b, expected):
        diff = a - b
        assert diff == expected
