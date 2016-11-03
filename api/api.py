#Import
import requests
import xmltodict

#API Authentication
auth_details = ('joshuajessy47@gmail.com', 'vlgUm9-dkCiFX8swDoQ4uNdO1kiNtZhBs1CAIkbJl6gX3946BJ8uEQ')

#User Input
Station = input(str('Naam van het station? '))

#API Query
api_url = 'http://webservices.ns.nl/ns-api-avt?station='+ Station
response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)

#Result
print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16] # 18:36
    trein = vertrek['TreinSoort']
    spoor = str(vertrek['VertrekSpoor'])
    spoor1 = spoor.replace("OrderedDict([('@wijziging', 'false'), ('#text', '", "")
    spoor2 = spoor1.replace("')])", "")
    spoor3 = spoor2.replace("OrderedDict([('@wijziging', 'true'), ('#text', '", "")
    try:
        vertraging = ' met ' + vertrek['VertrekVertragingTekst'] + ' vertraging '
    except KeyError:
        vertraging = ""

    vertragingInfo = vertraging.replace("+", "")

    print('Om '+vertrektijd+' vertrekt een ' + trein + ' naar '+ eindbestemming + ' op spoor ' + spoor3 + vertragingInfo)
