import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from datetime import date, timedelta
import time


class SendEmail:
    def __init__(self, dailyNum, weekNum, NG7weekNum, dicNews, GBPExchgeRate, GBPExchgeDate):

        self.dailyNum = dailyNum
        self.weekNum = weekNum
        self.NG7weekNum = NG7weekNum
        self.dicNews = dicNews
        self.GBPExchgeRate = GBPExchgeRate
        self.GBPExchgeDate = GBPExchgeDate
        self.hostServer = 'smtp.qq.com'
        self.mailUser = '984397521@qq.com'
        self.password = 'pkkmozwrurvdbbad'

        self.receiver = {'psxcz10@nottingham.ac.uk':"Changxin",
                         'aqxyz4@nottingham.ac.uk':"Yunzhen",
                         'enxsl19@nottingham.ac.uk ':"Shaozhen",
                         '516874282@qq.com':"Fubang",
                         'xinyuanfan@outlook.com':"Xinyuan",
                         '1323850726@qq.com':"Xuerong",
                         'lixyl221@nottingham.ac.uk':"Yuxuan",
                         'eexxx9@nottingham.ac.uk':"Xiaotian",
                         'lixty19@nottingham.ac.uk':"Tao"}
        # self.receiver = {'psxcz10@nottingham.ac.uk':"Changxin",
        #                  '984397521@qq.com':"Cx zhu",
        #                  'nuaazcx@163.com':"ZHU"}
        # self.receiver = ['alycl15@exmail.nottingham.ac.uk']
        self.receiverName = {}

        self.sender = '984397521@qq.com'
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
        <p>The daily number of tested people positive reported for <i>last 7 days</i> is <b>{self.NG7weekNum}</b> in the 
        area of <i>NG7 3LP</i>.</p> 
        <p>The number reported on <i>{self.todayDate}</i> is <b>{self.dailyNum}</b> in Nottingham! 
        And the positive reported number for <i>last 7 days</i> is <b>{self.weekNum}</b>. </p>
        <p><u><b>Daily News</b></u></p>
        <p>You might be intersted in the daily News below (from BBC News):</p>"""

        mailMsg2 = """"""
        for News in self.dicNews:
            mailMsg2 += f"""<a href = {self.dicNews[News]}>{News}</a><br>"""
        mailMsg2 += f"""
        <p><u><b>Exchange Rate</b></u></p>
        <p>The current market price for changing 100 <b>GBP</b> directly for <b>CNY</b> is <b>{self.GBPExchgeRate}</b>, 
        which is published at <i>{self.GBPExchgeDate}</i>(UTC+8). <b>(BANK OF CHINA)</b></p>

        <p>Remember to wear a mask and keep social distance, even if you don't care it. Enjoy your day!</p><br>
        <p>Here is my personal Home page, welcome to have a trip here--> <a href = "https://rookiestar6.github.io">Changxin's home</a> :)</p>
        <br></br>
        <p>Best wishes,</p>
        <p>Changxin ZHU</p>"""

        mailMsg = mailMsg1 + mailMsg2

        # mailWish = f"""
        # <p>朋友们</p></br>
        # <p>虎年新春即将到来，衷心的祝愿你在新的一年里，所有的期待都能出现，所有的梦想都能实现，所有的希望都能如愿，所有的付出都能兑现，新年快乐!</p>
        # <p>新的一年，我们都是追梦人!加油!奋斗路上的你!</p></br>
        # <p>顺颂时祺</p>
        # <p>朱昶歆</p>
        # """
        # f"""<a href = {self.dicNews[Newstitle[0]]}>{Newstitle[0]}<a><br>
        # <a href = {self.dicNews[Newstitle[1]]}>{Newstitle[1]}<a><br>
        # <a href = {self.dicNews[Newstitle[2]]}>{Newstitle[2]}<a><br>
        # <a href = {self.dicNews[Newstitle[3]]}>{Newstitle[3]}<a>

        file = open("./image/head.png", "rb")

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
                # message['From'] = Header("菜鸟教程", 'utf-8')
                # message['To'] = Header("测试", 'utf-8')

                subject = 'Python SMTP 邮件测试'
                # message['Subject'] = Header(f"Daily Hello to {self.receiver[receiver]}", 'utf-8')
                # message['From'] = ("%s<" + self.sender + ">") % ("Changxin ZHU")
                # print(self.receiver[receiver])
                # message['To'] = receiver
                msg['Subject'] = Header(f"Daily Hello to {self.receiver[receiver]}", 'utf-8')
                msg['From'] = ("%s<" + self.sender + ">") % ("Changxin ZHU")
                print(self.receiver[receiver])
                msg['To'] = receiver
                smtpObj = smtplib.SMTP_SSL(self.hostServer)
                smtpObj.login(self.mailUser, self.password)
                smtpObj.sendmail(self.sender, receiver, msg.as_string())
                # smtpObj.sendmail(self.sender, message['To'].split(','), message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


'''
        
        <p><u><b>The Trip to Oxford</b></u></p>
        <p>For the mates who are going to visit the Oxford, a series of <b>spots</b> listed would be useful to refer:(you can visit the tickets booking web via the link directly)<br>
        As a big fan of <b>Harry Potter</b>, the <a href = https://www.chch.ox.ac.uk/plan-your-visit/tickets>Christ Church Cathedral<a> 
        ,Tom Quad, <a href = https://visit.bodleian.ox.ac.uk/plan-your-visit>Bodleian Libraries<a>(It seems that you can't enter 
        without a permission, but Divinty School is available) must be in your list.<br><br>
        Also, the <a href = https://universitychurch.bookinglive.com>University Church of St Mary the Virgin<a> is a recommended
        spot to enjoy the whole city, and the trip to <a href = https://bookings.oxfordcastleandprison.co.uk/book>Oxford Castle & Prison<a>
        could be a way of knowing history, <a href = https://goo.gl/maps/PzazDWTia7skLGvq6>Radcliffe Camera<a>, <a href = https://goo.gl/maps/tdB2jujLwV6kxoot6>Bridge of Sighs<a>
        are both best known symbols of Oxford.<br>
        <b>Tasty food</b>: <br>
        <a href = https://goo.gl/maps/4DpKqdfi59DPRwnd9>Covered Market<a><br>
        British style: <a href = https://goo.gl/maps/T5waifeMjbKyjeLE7>Vaults and Garden<a><br>
        Thai: <a href = https://goo.gl/maps/seooodZdm7jT9RAb6>Thaikhun<a><br>
        Ice cream: <a href = https://goo.gl/maps/BcLFq3hUxfhWksmWA>George & Danver<a><br>
        <b>Shopping</b>:<br>
        <a href = https://g.page/AliceInWonderlandShop?share>Alice's shop<a><br></p>
        <p>Hope to have a wonderful trip!</p>
'''