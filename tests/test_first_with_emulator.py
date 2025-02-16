

class BaseOperatorsTest:

    @staticmethod
    def test_sum(app):
        two = 2
        three = 3
        app.calculator.nums.btn_digit(two).click()
        app.calculator.operators.btn_sum.click()
        app.calculator.nums.btn_digit(three).click()
        app.calculator.operators.btn_equals.click()
        result = app.calculator.result.text
        exp_result = two + three
        assert int(result) == exp_result, f"Wrong result: {two} + {three} != {result}. Must be: {exp_result}"
