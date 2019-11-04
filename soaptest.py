import requests


url="https://ips.gov.uz:443/mediate/ips/STC/GetTinbyPasNum"
headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
body = """<x:Envelope xmlns:x="http://schemas.xmlsoap.org/soap/envelope/" xmlns:get="urn:megaware:/mediate/ips/STC/GetTinbyPasNum/GetTinbyPasNum.wsdl">
    <x:Header/>
    <x:Body>
        <get:gettin>
            <get:AuthInfo>
                <get:userSessionId></get:userSessionId>
                <get:WS_ID></get:WS_ID>
                <get:LE_ID></get:LE_ID>
            </get:AuthInfo>
            <get:message>
                <get:lang>1</get:lang>
                <get:pasSer>AA</get:pasSer>
                <get:pasNum>0347012</get:pasNum>
            </get:message>
        </get:gettin>
    </x:Body>
</x:Envelope>"""

response = requests.post(url,data=body,headers=headers)

resx = str(response.content)
mysp = resx.split('<tin>')[1].split('</tin>')[0]


print (mysp)