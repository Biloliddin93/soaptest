from suds.client import Client
url = ' https://ips.gov.uz:443/mediate/ips/STC/GetTinbyPasNum?wsdl'
client = Client(url)

client.set_options(service='GetTinbyPasNumService', port='GetTinbyPasNumSOAP12BindingPort')
rest = client.service.rEQ(pasSer='AA', pasNum='2550708', lang='uz')
print (rest)
