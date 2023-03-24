import logging
import allure


@allure.suite("TestBasicOperation")
class TestBasicOperation:
    def test_add(self):
        print("Function to do addition")
        logging.info("logging info - Function to do addition")
        assert 4 == 3, "4 is not equal to 3"

    def test_sub(self):
        print("Function to do subtraction")
        logging.warning("logging warning - Function to do addition")
        assert True

    def test_mul(self):
        print("Function to do multiply")
        logging.error("logging error - Function to do addition")
        assert 'a'!='b'

    def test_div(self):
        print("Function to do division")
        assert 'a' != 'a', "a is not as expected"

    def test_mod(self):
        print("Function to do mod")
        assert 'a' == 'a', "a is not as expected"
