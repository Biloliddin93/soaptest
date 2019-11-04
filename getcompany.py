import requests
import xmltodict
import onevizion
import json



INN = 305875205
url="https://ips.gov.uz:443/mediate/ips/ILDS/GetFullLegalEntityInfoLE"
headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
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
                <get:TIN>"""+str(INN)+"""</get:TIN>
            </get:msg>
        </get:GetFullLegalEntityInfo>
    </x:Body>
</x:Envelope>"""


response = requests.post(url,data=body,headers=headers)


my_dict = xmltodict.parse(response.content)
myvars = my_dict['env:Envelope']['env:Body']['n1:LEGAL_ENTITY_INFORMATION']

print(myvars['TIN'][1])
