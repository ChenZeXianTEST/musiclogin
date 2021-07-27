import os, sys

sys.path.append(os.getcwd())
from page.page_in import PageIn
import time


class TestLogin():
    start = 0

    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()

    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self):
        self.login.page_click_login_page_btn()
        self.login.page_input_username('test_01')
        self.login.page_input_passwrof('admintest')
        count = True
        num = 0
        while count:
            time.sleep(0.5)
            self.login.page_input_login_code(num)
            time.sleep(0.5)
            self.login.page_click_login_btn()
            time.sleep(0.8)
            num += 1
            count = self.login.page_find_login_code_error()
        self.login.page_click_sign_btn()
        time.sleep(1)
        self.login.page_screenshot("./image/sign")
