from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import requests
import re

class CollectData():
    def __init__(self):
        self.url = "https://coronavirus.data.gov.uk/search?postcode=NG73LP"
        self.urlNews = "https://www.bbc.co.uk/news/uk"
        self.urlExchgeRate = "https://www.boc.cn/sourcedb/whpj/"
        self.urlDealmoon = "https://www.dealmoon.co.uk/"
        self.process()
        self.analyze()
        self.getNews()
        self.getExchgeRate()
        self.getItem()

    def process(self):

        # html = urlopen(self.url)
        # self.htmlText = bytes.decode(html.read())
        self.r = requests.get(self.url)
        self.rNews = requests.get(self.urlNews)
        self.rExchgeRate = requests.get(self.urlExchgeRate)
        self.rDealmoon = requests.get(self.urlDealmoon)
        self.rExchgeRate.encoding = 'utf-8'

    def analyze(self):
        obj = bf(self.r.text, 'lxml')
        # objText = obj.find('span', attrs={'class': 'govuk-link--no-visited-state number-link number'}).get_text()
        # objText1 = obj.find('span', attrs={'class': 'govuk-link--no-visited-state number-link'}).get_text()


        miniCard = obj.find('li', attrs={'class': 'mini-card'})

        node = miniCard.find('span', attrs={'class': 'govuk-link--no-visited-state number-link'})

        objText = node.contents[0]
        # node1 = miniCard.find('span', attrs={'class': 'govuk-link--no-visited-state number-link'})
        # objText1 = node1.contents[0]

        NG7Node = obj.find('ul', attrs={'class': 'govuk-list numbers-container govuk-!-margin-top-2'})
        objText2 =  NG7Node.find('span', attrs={'class': 'govuk-link--no-visited-state number-link number'}).get_text()

        objText = re.sub(r'\t|\n','', objText) #去除制表符
        # ret0 = re.search(r'D', objText).span()
        # objText1 = re.sub(r'\t|\n','', objText1)
        # objText1 = ''.join(temp)
        # print(objText1)
        # ret1 = re.search(r'N', objText1).span()
        objText2 = re.sub(r'\t|\n','', objText2)
        # print(objText2)
        # print(ret1)
        # ret1 = re.search(r'[^Daily]+[$2021]', objText).span()
        print(objText)
        # self.dailyNum = objText
        self.weekNum = objText
        self.NG7weekNum = objText2

        print(self.weekNum, self.NG7weekNum)

    def getNews(self):
        root = "https://www.bbc.co.uk"
        obj = bf(self.rNews.text, 'lxml')
        #头条新闻
        objText1 = obj.find('h3', attrs={
            'class': 'gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text'}).get_text()
        url1 = obj.find('a', attrs={
            'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor'}).get(
            "href")
        urlNews1 = root + url1
        self.dicNews = {objText1 : urlNews1}
        lst1 = obj.find('ul', attrs={'class': 'gel-layout gel-layout--equal nw-c-related-items__list--row'}).find_all('li')
        for i in lst1:
            objText1 = i.get_text()
            url1 = i.contents[0].contents[0].attrs['href']
            urlNews1 = root + url1
            self.dicNews[objText1] = urlNews1

        print(self.dicNews)




        # objText2 = obj.find('span', attrs={'class': 'nw-c-related-items__text gs-u-align-bottom'}).get_text()
        # url2 = obj.find('a', attrs={'nw-o-link-split__anchor gs-u-pt- gs-u-pb- gs-u-display-block nw-o-link-split__text'}).get("href")
        # urlNews2 = root + url2
        #
        # objText3 = obj.find('span', attrs={'class': 'nw-c-related-items__text gs-u-align-bottom'}).get_text()
        # url3 = obj.find('a', attrs={
        #     'nw-o-link-split__anchor gs-u-pt- gs-u-pb- gs-u-display-block nw-o-link-split__text'}).get("href")
        # urlNews3 = root + url2
        # print(objText2)




        # ret = re.split(r'Daily', objText)
        # print(ret)
    def getExchgeRate(self):
        obj = bf(self.rExchgeRate.text, 'lxml')
        nodeGBP = obj.find('div', attrs={'class': 'BOC_main'})
        res = r'(?<=<td>).*?(?=</td>)'
        exchgeLst = nodeGBP.find_all('td')
        for i in range(0, len(exchgeLst)):
            if '英镑' in exchgeLst[i]:
                GBPnodeInd = i
        self.GBPExchgeRate = exchgeLst[GBPnodeInd + 3]
        self.GBPExchgeRate = self.GBPExchgeRate.contents[0]
        self.GBPExchgeDate = exchgeLst[GBPnodeInd + 6]
        self.GBPExchgeDate = self.GBPExchgeDate.contents[0]

    def getItem(self):
        self.itemDic = {}
        self.itemIntro = {}
        obj = bf(self.rDealmoon.text, 'lxml')
        nodeItem = obj.find('div', attrs={'class': 'box_outer'})
        secNodeItem = nodeItem.find('div', attrs={'class': 'downContent'})
        lst1 = secNodeItem.find_all(
            'div', attrs={'class': 'box_item box_item_new'})
        for item in lst1:
            if len(self.itemDic) <= 4:
                itemImg = item.contents[1].contents[1].contents[1].attrs['src']
                itemHref = item.contents[1].attrs['href']
                itemIntro = item.contents[1].contents[1].contents[1].attrs['alt']
                self.itemDic[itemImg] = itemHref
                self.itemIntro[itemHref] = itemIntro


