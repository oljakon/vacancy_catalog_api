from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def wait(self, until, who=None, timeout=30, step=0.1):
    if who is None:
        who = self.driver
    return WebDriverWait(who, timeout, step).until(until)


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    context.browser = webdriver.Chrome('/Users/olga/Documents/vacancy_catalog_api/chromedriver', chrome_options=chrome_options)
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
