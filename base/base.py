from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # el.clear()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(value)

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_is_element_existence(self, element):
        try:
            ele = self.base_find_element(element)
        except:
            return False
        else:
            return True

    def base_action_chains_click(self, x, y):
        ActionChains(self.driver).move_by_offset(x, y).click().perform()

    def base_get_screenshot(self, imagename):
        self.driver.get_screenshot_as_file("./" + imagename + '.png')
