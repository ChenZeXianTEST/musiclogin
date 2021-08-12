import page
from base.base import Base


class PageLogin(Base):
    def page_click_login_page_btn(self):
        self.base_click(page.page_login_page_btn)

    def page_input_username(self, value):
        self.base_input(page.page_username, value)

    def page_input_password(self, value):
        self.base_input(page.page_password, value)

    def page_input_login_code(self,value):
        self.base_input(page.page_login_code, value)

    def page_click_login_btn(self):
        self.base_click(page.page_login_btn)

    def page_click_sign_btn(self):
        self.base_click(page.page_sign_btn)

    def page_find_login_code_error(self):
        return self.base_is_element_existence(page.page_login_code_error)

    def page_screenshot(self, imagename):
        self.base_get_screenshot(imagename)

    def page_send_email(self, user, password, receiver, image_path, today):
        # 邮件标题内容
        subject = str(today) + ': ' + 'HiFiNi - 音乐磁场自动化签到结果'
        # 邮件正文
        text = "一般来说如果发出了这封邮件基本上都是签到成功的，唯一出现问题的就是GitHub网络连接不稳定，" \
               "这会导致Jenkins直接停止执行，程序不会走到执行Python文件，也就不会看到这封邮件,出现这种情况只能重复构建。" \
               "\n还有就是阿里云服务器与登录网址连接不稳定、\n网站升级了验证码校验功能、\n签到按钮id修改了、\n界面改变了等等"
        self.base_send_email(user, password, receiver, image_path, subject, text)

    def page_read_yaml(self):
        return self.base_read_yaml("C:/base/info.yaml")


