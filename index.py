import datetime

import dateutil
import requests
import json

from dateutil.parser import parse


with open('pass.json', "rb") as PFile:
    passwordData = json.loads(PFile.read().decode('utf-8'))
user = passwordData["UserName"]
password = passwordData["Password"]
site = passwordData["URL"]
urlsite = passwordData["URLSITE"]

moneycbu = requests.get(site)


dataa = json.loads(moneycbu.text)
le = len(dataa)
i = 0





while i < le:
    datetimex = parse(dataa[i]['Date'])


    jsonx = '{ "fields":{ "CBU_CCY": "' + dataa[i]['Ccy'] + '",'
    jsonx += '"CBU_CCYNM_EN": "' + dataa[i]['CcyNm_EN'] + '",'
    jsonx += '"CBU_CCYNM_RU": "' + dataa[i]['CcyNm_RU'] + '",'
    jsonx += '"CBU_CCYNM_UZ": "' + dataa[i]['CcyNm_UZ'] + '",'
    jsonx += '"CBU_CODE": "' + dataa[i]['Code'] + '",'
    jsonx += '"CBU_DATE": "' + str(datetimex.date()) + '",'
    jsonx += '"CBU_NOMINAL": "' + dataa[i]['Nominal'] + '",'
    jsonx += '"CBU_RATE": "' + dataa[i]['Rate'] + '",'
    jsonx += '"CBU_STATUS": 1  }}'

    answer = requests.post(urlsite, data=json.dumps(json.loads(jsonx)),auth=(user, password))
    print(answer.text)
    i += 1





