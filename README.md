# Newspaper


This project mainly provides an idea instead of the template, to implement the daily newspaper as the email format. It was created in 2021, which was an unnormal year that meeting with the COVID-19. For the people who live overseas, hope they could take care of themselves so that offering such the available info. 

<div  align = "center"><img src = "https://user-images.githubusercontent.com/94005108/174389281-d02604b0-6183-45f1-852e-0640412437ac.jpg" width = "200px"></div>

The main.py is the extrance of the whole project.

It mainly involves two external libraries, which are requests and email, respectively. 

The info, including the reported postive number, exchange rate, and BBC news, are all collected via analyzing the structure of the html, as shown in collect.py.

In EmailSend.py, the content of newspaper with info will be edited as html, and send it individually to person.
The parameters here need to be filled:

self.hostServer = 'smtp.qq.com'

self.mailUser = '******@qq.com'

self.password = '**********'

Besides, the newspaper has been added a function of scheduled sending, which is implemented via actions of Github, the email will be sent at 7 A.M. everyday. (This is the most valuable funciton for me in this project)
