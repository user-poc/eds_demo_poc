import pytest
import allure


@allure.suite("TestAllureSteps")
class TestAllureSteps:
    @allure.step
    def passing_step(self):
        pass

    @allure.step
    def passing_step_2(self):
        pass

    @allure.step
    def step_with_nested_steps(self):
        self.nested_step()

    @allure.step
    def nested_step(self):
        self.nested_step_with_arguments(1, 'abc')

    @allure.step
    def nested_step_with_arguments(self, arg1, arg2):
        pass

    def test_with_nested_steps(self):
        self.passing_step()
        self.passing_step_2()
        self.step_with_nested_steps()

    def test_with_single_step(self):
        self.passing_step()
