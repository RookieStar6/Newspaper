from collect import CollectData
from EmailSend import SendEmail

if __name__ == '__main__':
    collectdata = CollectData()
    sendEmail = SendEmail(collectdata.weekNum, collectdata.NG7weekNum, collectdata.dicNews, collectdata.GBPExchgeRate, collectdata.GBPExchgeDate, collectdata.itemDic, collectdata.itemIntro)

