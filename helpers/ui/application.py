from typing import Optional

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import WebDriver

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
DEFAULT_PORT = 4723


class Application:
    def __init__(self, config):
        self.config = config
        self.appium: Optional[WebDriver]= None
        self.__calculator = None
        self.appium_service = AppiumService()

    @property
    def calculator(self) -> CalculatorHelperUI:
        if not self.__calculator:
            self.__calculator = CalculatorHelperUI(self)
        return self.__calculator

    def set_appium_driver(self):
        # todo move appium service to conftest
        self.appium_service.start(args=['--address', '127.0.0.1', '-p', str(DEFAULT_PORT)])
        assert self.appium_service.is_running
        assert self.appium_service.is_listening

        self.appium = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(self.config))


    def destroy(self):
        if self.appium:
            self.appium.quit()
        if self.appium_service:
            self.appium_service.stop()

