from appium.webdriver.common.appiumby import AppiumBy


class CalculatorHelperUI:
    def __init__(self, app):
        self.app = app
        self.nums = NumsHelperUI(app)
        self.operators = OperatorsHelperUI(app)

    @property
    def btn_clear(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/clr')

    @property
    def result(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/result_final')


class NumsHelperUI:
    def __init__(self, app):
        self.app = app

    def btn_digit(self, number:str):
        return self.app.appium.find_element(by=AppiumBy.ID, value=f'com.google.android.calculator:id/digit_{number}')


class OperatorsHelperUI:
    def __init__(self, app):
        self.app = app

    @property
    def btn_equals(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/eq')

    @property
    def btn_sum(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/op_add')

    @property
    def btn_minus(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/op_sub')

    @property
    def btn_multiply(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/op_mul')

    @property
    def btn_divide(self):
        return self.app.appium.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/op_div')

