from suds.client import Client
url = 'ips.gov.uz:443/mediate/ips/STC/GetTinbyPasNum?wsdl'
client = Client(url)
print (client)


