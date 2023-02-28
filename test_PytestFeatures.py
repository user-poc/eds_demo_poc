import pytest
import allure


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
