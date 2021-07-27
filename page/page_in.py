from base.get_driver import *
from page.page_login import PageLogin
driver = get_home_page_driver()


class PageIn():
    def page_get_pagelogin(self):
        return PageLogin(driver)

