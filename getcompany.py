from suds.client import Client
url = 'https://ips.gov.uz/mediate/ips/ILDS/GetFullLegalEntityInfoLE?wsdl'
client = Client(url)

client.set_options(service='GetFullLegalEntityInfoLEService', port='GetFullLegalEntityInfoLESOAP12BindingPort')
rest = client.service.receive(_LHASH_KEY_='E001|oDlpS4ZiwZEd5giUkMSxKXBIb9bOafcOJOBXRnzuVyepiReYCylXFRL4qz9gV',TIN='305219838')
print (rest)
