import os, sys
import random

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
        # 点击用户登录, 进入登录界面
        self.login.page_click_login_page_btn()
        # 输入账号密码
        self.login.page_input_username(info['username'])
        self.login.page_input_password(info['password'])
        time.sleep(random.randint(1, 5))
        # 点击人机交互按钮
        self.login.page_man_machine_brn()
        time.sleep(2)
        # 人机校验
        self.login.page_man_machine_calibration()
        # 点击登录按钮
        self.login.page_click_login_btn()

        today = datetime.date.today()
        image_path = "C:/base/" + str(today) + ".png"

        # 点击签到
        self.login.page_click_sign_btn()
        time.sleep(1)
        # 判断图片路径是否存在
        if Path(image_path).exists():
            pass
        else:
            self.login.page_screenshot(image_path)

        self.login.page_send_email(info["user"], info["pwd"], info["receiver"], image_path, today)



