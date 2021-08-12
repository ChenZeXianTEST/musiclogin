import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(value)

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_is_element_existence(self, element):
        try:
            self.base_find_element(element)
        except:
            return False
        else:
            return True

    def base_action_chains_click(self, x, y):
        ActionChains(self.driver).move_by_offset(x, y).click().perform()

    def base_get_screenshot(self, imagename):
        self.driver.get_screenshot_as_file(imagename)

    def base_read_yaml(self, yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def base_send_email(self, user, password, receiver, image_path, subject, text):
        # SMTP服务器
        smtpserver = 'smtp.163.com'
        message = MIMEMultipart()
        # 邮件标题
        message['Subject'] = Header(subject, 'utf-8')
        # 正文
        message.attach(MIMEText(text, 'plain', 'utf-8'))
        # 需要一个大文件,否则会被认为是垃圾邮件或骚扰邮件,报错看邮件退件代码
        doc_file = open(R'C:/base/压轴.docx', 'rb').read()
        # 图片路径
        image_file = open(image_path, 'rb').read()
        att_doc = MIMEText(doc_file, 'base64', 'utf-8')
        att_doc['Content-Type'] = 'application/octet-stream'
        att_image = MIMEImage(image_file)
        att_doc.add_header('Content-Disposition', 'attachment', filename='压轴.docx')
        att_image.add_header('Content-Disposition', 'attachment', filename='签到结果.png')
        message.attach(att_doc)
        message.attach(att_image)
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(user, password)
        smtp.sendmail(user, receiver, message.as_string())
        smtp.quit()
