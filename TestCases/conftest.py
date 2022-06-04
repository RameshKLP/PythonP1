import os
import time

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        time.sleep(3)
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'HRM Tool'
    config._metadata['Module Name'] = 'Admin'
    config._metadata['Tester'] = 'Ramesh Lingadalli'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://opensource-demo.orangehrmlive.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name=report.nodeid.replace("::", "_")+ ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px; height:200px;" onclick="window.open(' \
                       'this.src) align="right"/></div> ' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
        driver.close()
