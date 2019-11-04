import requests
import xmltodict
import onevizion
import json



url = 'pmi.gov.uz'
login = 'Biloliddinnapm'
password = '1234567890'
APIURL = 'https://pmi.gov.uz/api/v3/trackor_types/VEDOMSTVO/trackors?fields=VED_INN%2CVED_CHECK_INN&VED_CHECK_INN=1'




r=requests.get(APIURL, auth=(login, password))
response = r.json()
for data in response:
 INN = data['VED_INN']
 urlx = "https://ips.gov.uz:443/mediate/ips/ILDS/GetFullLegalEntityInfoLE"
 headers = {'content-type': 'application/soap+xml'}
 # headers = {'content-type': 'text/xml'}
 body = """<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:get="urn:megaware:/mediate/ips/ILDS/GetFullLegalEntityInfoLE/GetFullLegalEntityInfoLE.wsdl">
     <x:Header/>
     <x:Body>
         <get:GetFullLegalEntityInfo>
             <get:AuthInfo>
                 <get:userSessionId></get:userSessionId>
                 <get:WS_ID></get:WS_ID>
                 <get:LE_ID></get:LE_ID>
             </get:AuthInfo>
             <get:msg>
                 <get:_LHASH_KEY_>E001|oDlpS4ZiwZEd5giUkMSxKXBIb9bOafcOJOBXRnzuVyepiReYCylXFRL4qz9gV</get:_LHASH_KEY_>
                 <get:TIN>""" + str(INN) + """</get:TIN>
             </get:msg>
         </get:GetFullLegalEntityInfo>
     </x:Body>
 </x:Envelope>"""

 response = requests.post(urlx, data=body, headers=headers)

 my_dict = xmltodict.parse(response.content)
 myvars = my_dict['env:Envelope']['env:Body']['n1:LEGAL_ENTITY_INFORMATION']

 cbu_list_request = onevizion.Trackor(trackorType='VEDOMSTVO', URL=url, userName=login, password=password)




 cbu_list_request.create(
  fields={
   'VED_OKPO':myvars['OKPO'][1],
   'VED_INN':myvars['TIN'][1],

   'VED_KFS_CD':myvars['KFS_CD'][1],
   'VED_KOPF_CD':myvars['KOPF_CD'][1],
   'VED_SOATO':myvars['SOATO_CD'][1],
   'VED_OKONH':myvars['OKONH_CD'][1],
   'VED_OKED':myvars['OKED_CD'][1],
   'VED_SOOGU':myvars['SOOGU_CD'][1],
   'VED_SHORT_NAME':myvars['LE_NM_UZ'][1],
   'VED_NAME':myvars['LE_NM_UZ'][1],
   #'VED_REG_DATE':myvars['REG_DATE'][1],
   'VED_REG_NO':myvars['REG_NO'][1],
   'VED_LIQ_DATE':myvars['LIQ_DATE'][1],
   'VED_LIQ_NO':myvars['LIQ_NO'][1],
   'VED_ZIP':myvars['ZIP'][1],
   'VED_ADDRESS':myvars['ADDR'][1],
   'VED_FULL_NAME_HEAD':myvars['HEAD_NM'][1],
   'VED_HEAD_TIN':myvars['HEAD_TIN'][1],
   'VED_CONTACT_NUMBER':myvars['PHONE'][1],
   'VED_EMAIL':myvars['EMAIL'][1],
   'VED_AUTH_CAPITAL_SOM':myvars['AUTH_CAPITAL'][1],
   'VED_AUTH_CAPITAL_US':myvars['AUTH_CAPITAL_US'][1],
   'VED_SMALL_BIZ':myvars['SMALL_BIZ'][1],
   'VED_TYPE_OWNERSHIP':myvars['LE_TYP'][1],
   'VED_TAX_CD':myvars['TAX_CD'][1],
   'VED_LE_STATUS':myvars['LE_STATUS'][1],
   'VED_FOUNDER_NM1':myvars['FOUNDER_NM1'][1],
   'VED_FOUNDER_COUNTRY1':myvars['FOUNDER_COUNTRY1'][1],
   'VED_FOUNDER_NM2':myvars['FOUNDER_NM2'][1],
   'VED_FOUNDER_COUNTRY2':myvars['FOUNDER_COUNTRY2'][1],
   'VED_FOUNDER_NM3':myvars['FOUNDER_NM3'][1],
   'VED_FOUNDER_COUNTRY3':myvars['FOUNDER_COUNTRY3'][1],


  }
    )











