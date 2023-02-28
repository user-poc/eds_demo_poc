import pytest
import allure


@allure.suite("TestAllureFeatures")
class TestAllureFeatures:
    @allure.description_html("""
    <h1>Test with some complicated html description</h1>
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr align="center">
        <td>William</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr align="center">
        <td>Vasya</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>
    """)
    def test_html_description(self):
        assert True

    @allure.description("""
    Multiline test description.
    That comes from the allure.description decorator.

    Nothing special about it.
    """)
    def test_description_from_decorator(self):
        assert 42 == int(6 * 7)

    def test_unicode_in_docstring_description(self):
        """Unicode in description.

        Этот тест проверяет юникод.

        你好伙计.
        """
        assert 42 == int(6 * 7)

    @allure.description("""
    This description will be replaced at the end of the test.
    """)
    def test_dynamic_description(self):
        assert 42 == int(6 * 7)
        allure.dynamic.description('A final description.')

    @allure.title("This test has a custom title with unicode: Привет!")
    def test_with_unicode_title(self):
        assert 3 + 3 == 6

    @allure.title("Parameterized test title: adding {param1} with {param2}")
    @pytest.mark.parametrize('param1,param2,expected', [
        (2, 2, 4),
        (1, 2, 5)
    ])
    def test_with_parameterized_title(self, param1, param2, expected):
        assert param1 + param2 == expected

    @allure.story('epic_1')
    def test_with_epic_1(self):
        pass

    @allure.story('story_1')
    def test_with_story_1(self):
        pass

    @allure.story('story_2')
    def test_with_story_2(self):
        pass

    @allure.feature('feature_2')
    @allure.story('story_2')
    def test_with_story_2_and_feature_2(self):
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_with_trivial_severity(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_with_normal_severity(self):
        pass
