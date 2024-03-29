from selenium.webdriver.common.by import By


# 登录界面按钮
page_login_page_btn = By.XPATH, '//*[@id="nav"]/ul[2]/li[4]/a'
# 用户名
page_username = By.CSS_SELECTOR, '[placeholder="Email / 用户名"]'
# 密码
page_password = By.CSS_SELECTOR, '[name="password"]'
# 登录按钮
page_login_btn = By.CSS_SELECTOR, '[data-loading-text="正在提交..."]'
# 签到按钮
page_sign_btn = By.ID, 'sign'
# 用户名头像
page_user_picture = By.XPATH, '//*[@id="nav"]/ul[2]/li[5]/a'
# 人机交互按钮
page_man_machine = By.CSS_SELECTOR, '[class="btn btn-secondary btn-block"]'
# 滑动按钮
page_hd_btn = By.CSS_SELECTOR, '[class="verify-left-bar"]'
# 获取图片
page_img = By.CSS_SELECTOR, 'img'
