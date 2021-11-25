import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import date, timedelta


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

        self.receiver = ['psxcz10@nottingham.ac.uk', 'aqxyz4@nottingham.ac.uk', 'enxsl19@nottingham.ac.uk ',
                         '516874282@qq.com', 'xinyuanfan@outlook.com', '1323850726@qq.com', 'lixyl221@nottingham.ac.uk'
                         ,'eexxx9@nottingham.ac.uk', 'lixty19@nottingham.ac.uk']
        # self.receiver = ['psxcz10@nottingham.ac.uk', '984397521@qq.com', 'nuaazcx@163.com']
        # self.receiver = ['alycl15@exmail.nottingham.ac.uk']
        self.receiverName = ['Changxin', 'ZHU']

        self.sender = '984397521@qq.com'
        today = date.today() + timedelta(days=-1)
        today.ctime()
        self.todayDate = str(today.day) + '/' + str(today.month) + '/' + str(today.year)
        self.EmailText()



    def EmailText(self):
        Newstitle = []
        for i in self.dicNews:
            Newstitle.append(i)

        mailMsg0 = ','.join(self.receiverName)
        mailMsg1 = f"""<p>Hi, </p><br>
        <p>Good Morning! This is an automatic email, please don't reply it.</p>
        <p><u><b>Positive Reported Number</b></u></p>
        <p>The daily number of tested people positive reported for <i>last 7 days</i> is <b>{self.NG7weekNum}</b> in the 
        area of <i>NG7 3LP</i>.</p> 
        <p>The number reported on <i>{self.todayDate}</i> is <b>{self.dailyNum}</b> in Nottingham! 
        And the positive reported number for <i>last 7 days</i> is <b>{self.weekNum}</b>. </p>
        <p><u><b>Daily News</b></u></p>
        <p>You might be intersted in the daily News below (from BBC News):</p>"""

        mailMsg2 = """"""
        for News in self.dicNews:
            mailMsg2 += f"""<a href = {self.dicNews[News]}>{News}<a><br>"""
        mailMsg2 += f"""
        <p><u><b>Exchange Rate</b></u></p>
        <p>The current market price for changing 100 <b>GBP</b> directly for <b>RMB</b> is <b>{self.GBPExchgeRate}</b>, 
        which is published at <i>{self.GBPExchgeDate}</i>(UTC+8). <b>(BANK OF CHINA)</b></p>

        <p>Remember to wear a mask and keep social distance, even if you don't care it. Enjoy your day!</p>
        <br></br>
        <p>Best wishes,</p>
        <p>Changxin ZHU</p>"""

        mailMsg = mailMsg1 + mailMsg2
        # f"""<a href = {self.dicNews[Newstitle[0]]}>{Newstitle[0]}<a><br>
        # <a href = {self.dicNews[Newstitle[1]]}>{Newstitle[1]}<a><br>
        # <a href = {self.dicNews[Newstitle[2]]}>{Newstitle[2]}<a><br>
        # <a href = {self.dicNews[Newstitle[3]]}>{Newstitle[3]}<a>

        message = MIMEText(mailMsg, 'html', 'utf-8')
        # message['From'] = Header("菜鸟教程", 'utf-8')
        # message['To'] = Header("测试", 'utf-8')

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header('Daily hello from Changxin', 'utf-8')
        message['From'] = ("%s<"+self.sender+">") % (Header(self.sender, 'utf-8'))
        message['To'] = ','.join(self.receiver)
        # mailMsg += mailMsg0
        try:
            smtpObj = smtplib.SMTP_SSL(self.hostServer)
            smtpObj.login(self.mailUser, self.password)
            smtpObj.sendmail(self.sender, message['To'].split(','), message.as_string())
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