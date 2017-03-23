#coding:utf-8
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "use_django_db.settings")
import django
django.setup()

import requests,re
from bs4 import BeautifulSoup
import threading
import logging



from match_stat.models import MatchInfo

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] \
                     %(levelname)s %(message)s",\
                    filename='error.log',\
                    filemode='w')
BASE_URL="http://300report.jumpw.com/"
STARTID=67482286

class MatchStat():
    def stat_match(self,matchid):
        try:
            html=requests.get(BASE_URL+'match.html?id=%d'%matchid)
            soup=BeautifulSoup(html.text,'lxml')
            datamsg=soup.findAll(attr={'class':'datamsg'})           #类型:竟技场 人头数:62/51 比赛时间:2017-03-22 22:19:13 比赛用时:41分40秒
            datamsg=datamsg[0].span.next_element.next_element.split()
            match_info=MatchInfo(matchid=matchid)
            match_info.info_type=datamsg[0].split(':')[1]
            match_info.info_date=datamsg[2].split(':')[1]
            match_info.info_time=datamsg[3]
            match_info.info_playtime=datamsg[4].split(":")[1]
            match_info.save()

        except Exception,e:
            logging.ERROR(e)

    def run(self):
        for i in range(10):
            self.stat_match(int(STARTID+i))

if __name__=='__main__':
    pass


