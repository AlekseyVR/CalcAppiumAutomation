import pytest
import json
import os.path
from typing import Optional
from helpers.ui.application import Application


app_fixture: Optional[Application] = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global app_fixture
    # browser = request.config.getoption("--browser")
    # config = load_config(request.config.getoption("--target"))

    config = load_config("C:\\MyProjects\\TestProject\\config.json")
    app_fixture = Application(config=config)
    app_fixture.set_appium_driver()
    if app_fixture is None: # if fixture is None or not fixture.is_valid():
        app_fixture = Application(config=config)
        app_fixture.set_appium_driver()
    return app_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        app_fixture.destroy()

    request.addfinalizer(fin)
    return app_fixture
