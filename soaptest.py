from suds.client import Client
client = Client("https://ips.gov.uz:443/mediate/ips/STC/GetTinbyPasNum?wsdl")
print (client)
result = client.service.GetTinbyPasNum(pasSer='AA', pasNum='2550708', lang='uz')

print (result)
