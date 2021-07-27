import page
from base.base import Base


class PageLogin(Base):
    def page_click_login_page_btn(self):
        self.base_click(page.page_login_page_btn)

    def page_input_username(self, value):
        self.base_input(page.page_username, value)

    def page_input_passwrof(self, value):
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


