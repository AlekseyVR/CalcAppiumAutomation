from appium import webdriver
from appium.options.android import UiAutomator2Options

from helpers.ui.calculator import CalculatorHelperUI

appium_server_url='http://localhost:4723'
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

class Application:
    def __init__(self, config):
        self.config = config
        self.appium = None
        self.__calculator = None

    @property
    def calculator(self) -> CalculatorHelperUI:
        if not self.__calculator:
            self.__calculator = CalculatorHelperUI(self)
        return self.__calculator

    def set_appium_driver(self):
        self.appium = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(self.config))


    def destroy(self):
        if self.appium:
            self.appium.quit()

