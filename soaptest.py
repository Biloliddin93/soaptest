from suds.client import Client
url = 'https://ips.gov.uz:443/mediate/ips/STC/GetTinbyPasNum?wsdl'
client = Client(url)
print (client)


