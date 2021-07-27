from selenium import webdriver


def get_home_page_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.hifini.com/")
    return driver