import page
from base.base import Base


class PageLogin(Base):
    def page_click_login_page_btn(self):
        """
        进入登录界面
        :return:
        """
        self.base_click(page.page_login_page_btn)

    def page_input_username(self, value):
        """
        输入用户名
        :param value:
        :return:
        """
        self.base_input(page.page_username, value)

    def page_input_password(self, value):
        """
        输入密码
        :param value:
        :return:
        """
        self.base_input(page.page_password, value)

    def page_click_login_btn(self):
        """
        点击登录按钮
        :return:
        """
        self.base_click(page.page_login_btn)

    def page_click_sign_btn(self):
        """
        点击签到
        :return:
        """
        self.base_click(page.page_sign_btn)

    def page_screenshot(self, imagename):
        """
        截图
        :param imagename:
        :return:
        """
        self.base_get_screenshot(imagename)

    def page_man_machine_brn(self):
        """
        点击人机校验按钮
        :return:
        """
        self.base_click(page.page_man_machine)

    def page_man_machine_calibration(self):
        """
        进行人机校验
        :return:
        """
        self.base_man_machine_calibration(page.page_img, page.page_hd_btn, page.page_man_machine)

    def page_send_email(self, user, password, receiver, image_path, today):
        """

        :param result: 运行结果
        :param user:
        :param password:
        :param receiver:
        :param image_path:
        :param today:
        :return:
        """
        # 邮件标题内容
        subject = str(today) + ': ' + 'HiFiNi - 音乐磁场自动化签到结果'
        # 邮件正文
        text = "天地有正气，杂然赋流形。下则为河岳，上则为日星。于人曰浩然，沛乎塞苍冥。" \
               "皇路当清夷，含和吐明庭。时穷节乃见，一一垂丹青。在齐太史简，在晋董狐笔。" \
               "在秦张良椎，在汉苏武节。为严将军头，为嵇侍中血。为张睢阳齿，为颜常山舌。" \
               "或为辽东帽，清操厉冰雪。或为出师表，鬼神泣壮烈。或为渡江楫，慷慨吞胡羯。" \
               "或为击贼笏，逆竖头破裂。是气所磅礴，凛烈万古存。当其贯日月，生死安足论。" \
               "地维赖以立，天柱赖以尊。三纲实系命，道义为之根。嗟予遘阳九，隶也实不力。" \
               "楚囚缨其冠，传车送穷北。鼎镬甘如饴，求之不可得。阴房阗鬼火，春院閟天黑。" \
               "牛骥同一皂，鸡栖凤凰食。一朝蒙雾露，分作沟中瘠。如此再寒暑，百沴自辟易。" \
               "嗟哉沮洳场，为我安乐国。岂有他缪巧，阴阳不能贼。顾此耿耿在，仰视浮云白。" \
               "悠悠我心悲，苍天曷有极。哲人日已远，典刑在夙昔。风檐展书读，古道照颜色。"
        self.base_send_email(user, password, receiver, image_path, subject, text)

    def page_read_yaml(self):
        return self.base_read_yaml("C:/base/info.yaml")

