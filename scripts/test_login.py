import os, sys

sys.path.append(os.getcwd())
from pathlib import Path
from page.page_in import PageIn
import time
import datetime


class TestLogin():
    start = 0

    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()

    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self):
        info = self.login.page_read_yaml()
        self.login.page_click_login_page_btn()
        self.login.page_input_username(info['username'])
        self.login.page_input_password(info['password'])
        count = True
        today = datetime.date.today()
        image_path = "C:/base/" + str(today) + ".png"
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
        if Path(image_path).exists():
            pass
        else:
            self.login.page_screenshot(image_path)
        print("签到完成")
        self.login.page_send_email(info["user"], info["pwd"], info["receiver"], image_path, today)



