import requests
import xmltodict
auth_details = ('joshuajessy47@gmail.com', 'vlgUm9-dkCiFX8swDoQ4uNdO1kiNtZhBs1CAIkbJl6gX3946BJ8uEQ')
Station = input(str('Naam van het station? '))
api_url = 'http://webservices.ns.nl/ns-api-avt?station='+ Station
response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
 eindbestemming = vertrek['EindBestemming']
 vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
 vertrektijd = vertrektijd[11:16] # 18:36
 print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)