import logging
import allure


@allure.suite("TestBasicOperation")
class TestBasicOperation:
    logging.basicConfig(level=logging.DEBUG)
    def test_add(self):
        print("Function to do addition")
        logging.info("logging info - Function to do addition")
        assert 4 == 3, "4 is not equal to 3"

    def test_sub(self):
        print("Function to do subtraction")
        logging.warning("logging warning - Function to do subtraction")
        assert True

    def test_mul(self):
        print("Function to do multiply")
        logging.error("logging error - Function to do multiply")
        assert 'a'!='b'

    def test_div(self):
        print("Function to do division")
        logging.info("logging info - Function to do division")
        assert 'a' != 'a', "a is not as expected"

    def test_mod(self):
        print("Function to do mod")
        logging.info("logging info - Function to do mod")
        assert 'a' == 'a', "a is not as expected"
