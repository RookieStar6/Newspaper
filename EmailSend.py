import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from datetime import date, timedelta
import time


class SendEmail:
    def __init__(self, weekNum, NG7weekNum, dicNews, GBPExchgeRate, GBPExchgeDate, itemImg, itemIntro):

        # self.dailyNum = dailyNum
        self.weekNum = weekNum
        self.NG7weekNum = NG7weekNum
        self.dicNews = dicNews
        self.GBPExchgeRate = GBPExchgeRate
        self.GBPExchgeDate = GBPExchgeDate
        self.itemImg = itemImg
        self.itemIntro = itemIntro
        self.hostServer = 'smtp.qq.com'
        self.mailUser = '********@qq.com'
        self.password = '***************'

        self.receiver = {********@qq.com':"name"}
        
        self.receiverName = {}

        self.sender = self.mailUser
        today = date.today() + timedelta(days=-1)
        today.ctime()
        self.todayDate = str(today.day) + '/' + str(today.month) + '/' + str(today.year)
        self.mytime = time.localtime()
        self.EmailText()



    def EmailText(self):
        Newstitle = []
        for i in self.dicNews:
            Newstitle.append(i)

        if self.mytime.tm_hour < 12:
            mailMsg0 = """<p>Good morning! This is an automatic email, please don't reply it.</p>"""
        else:
            mailMsg0 = """<p>Good afternoon! This is an automatic email, please don't reply it.</p>"""
        mailMsg1 = mailMsg0 + f"""
        <p><u><b>Positive Reported Number</b></u></p>
        <p>The number of tested people positive reported for <i>last 7 days</i> is <b>{self.NG7weekNum}</b> in the 
        area of <i>NG7 3LP</i>.</p> 
        <p>The positive reported number on <i>{self.todayDate}</i> for <i>last 7 days</i> is <b>{self.weekNum}</b> in Nottingham. </p>
        <p><u><b>Daily News</b></u></p>
        <p>You might be intersted in the daily News below (from BBC News):</p>"""

        mailMsg2 = """"""
        for News in self.dicNews:
            mailMsg2 += f"""<a style = "color: green" href = {self.dicNews[News]}>{News}</a><br>"""
        mailMsg2 += f"""
        <p><u><b>Exchange Rate</b></u></p>
        <p>The current market price for changing 100 <b>GBP</b> directly for <b>CNY</b> is <b>{self.GBPExchgeRate}</b>, 
        which is published at <i>{self.GBPExchgeDate}</i>(UTC+8). <b>(BANK OF CHINA)</b></p>

        <p>Remember to wear a mask and keep social distance, even if you don't care it. Enjoy your day!</p><br>
        <p>Here is my personal Home page, welcome to have a trip here--> <a href = "https://rookiestar6.github.io">Changxin's home</a> :)</p>
        <br></br>
        <p>Here are some items you might be looking for: (英国省钱快报)</p>
        """

        mailMsg3 = f"""
        <table>
        <tr>"""

        for itemImg in self.itemImg:
            mailMsg3 += f"""<td>
                                <img src = "{itemImg}">
                            </td>"""
        mailMsg3 += """</tr>
        <tr style = "height:15px">"""

        for itemHref in self.itemIntro:
            mailMsg3 += f"""<td style = "text-align:center">
                                 <a style = "color: green" href = "{itemHref}">{self.itemIntro[itemHref]}</a>
                            </td>"""
        mailMsg3 += """</tr>
                       </table> 
                        """
        mailMsg4 = f"""
        <p>Best wishes,</p>
        <p>Changxin ZHU</p>
        """
        mailMsg = mailMsg1 + mailMsg2 +mailMsg3 + mailMsg4
       
        file = open("./image/head1.png", "rb")

        img_data = file.read()
        file.close()
        img = MIMEImage(img_data)
        img.add_header('Content-ID', '<image1>')
        # message['To'] = ','.join(self.receiver)
        # mailMsg += mailMsg0
        try:
            for receiver in self.receiver:
                msg = MIMEMultipart()
                msg.attach(img)
                finalMailMsg = f"""
                <html>
                <head>
                </head>
                <body>
                <img src = "cid:image1">
                <p>Dear {self.receiver[receiver]},</p><br>""" + mailMsg + """
                </body>
                </html>
                """
                message = MIMEText(finalMailMsg, 'html', 'utf-8')
                msg.attach(message)
                msg['Subject'] = Header(f"Daily Hello to {self.receiver[receiver]}", 'utf-8')
                msg['From'] = ("%s<" + self.sender + ">") % ("Changxin ZHU")
                print(self.receiver[receiver])
                msg['To'] = receiver
                smtpObj = smtplib.SMTP_SSL(self.hostServer)
                smtpObj.login(self.mailUser, self.password)
                smtpObj.sendmail(self.sender, receiver, msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
