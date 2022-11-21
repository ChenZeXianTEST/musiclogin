import base64
import smtplib
import time
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import cv2
import yaml
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        """
        查找元素
        :param loc: 元素
        :param timeout: 时间限制
        :param poll_frequency: 检测频率
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def base_input(self, loc, value):
        """
        输入
        :param loc:
        :param value:
        :return:
        """
        el = self.base_find_element(loc)
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(value)

    def base_click(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        self.base_find_element(loc).click()

    def base_is_element_existence(self, element):
        """
        判断是否存在
        :param element:
        :return:
        """
        try:
            self.base_find_element(element)
        except:
            return False
        else:
            return True

    def base_action_chains_click(self, x, y):
        ActionChains(self.driver).move_by_offset(x, y).click().perform()

    def base_get_screenshot(self, imagename):
        """
        截图
        :param imagename:
        :return:
        """
        self.driver.get_screenshot_as_file(imagename)

    def base_read_yaml(self, yaml_path):
        """
        读取yaml文件
        :param yaml_path:
        :return:
        """
        with open(yaml_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def base_man_machine_calibration(self, img, hd_btn, man_machine):
        """
        验证滑块功能,成功率不算高,好在测试网页没有次数限制
        代码来源:https://www.cnblogs.com/lihongtaoya/p/16793699.html
        :param img:图片
        :param hd_btn:活动按钮
        :param man_machine:人机交互按钮
        :return:
        """
        while True:
            img_list = self.base_find_elements(img)
            hk_img = img_list[2].get_attribute("src")  # 获取定位滑块的src
            hk_img = hk_img[22:]  # 截取所需要的url
            with open("C:/base/hk.png", mode="wb") as f:
                f.write(base64.b64decode(hk_img))  # base64解密后保存到本地img下
            qk_img = img_list[1].get_attribute("src")  # 获取定位缺口的src
            qk_img = qk_img[22:]  # 截取所需要的url
            # base64解密后保存到本地img下
            with open("C:/base/qk.png", mode="wb") as f:
                f.write(base64.b64decode(qk_img))
            hk_img_01 = cv2.imread("C:/base/hk.png", 0)  # 灰度化
            qk_img_01 = cv2.imread("C:/base/qk.png", 0)
            # 获取滑块在缺口图的位置
            late = cv2.matchTemplate(qk_img_01, hk_img_01, cv2.TM_CCOEFF_NORMED)
            loc = cv2.minMaxLoc(late)
            x = int(loc[2][0] * 47 / 50)
            action = ActionChains(self.driver)
            try:
                action.drag_and_drop_by_offset(self.base_find_element(hd_btn), x, 0).perform()
            except:
                pass
            time.sleep(3)
            if self.base_find_element(man_machine).text == "验证成功":
                break

    def base_send_email(self, user, password, receiver, image_path, subject, text):
        """
        SMTP服务器,发邮件
        :param user: 用户名
        :param password: 密码
        :param receiver: 接收
        :param image_path: 图片路径
        :param subject: 主题
        :param text:
        :return:
        """
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
