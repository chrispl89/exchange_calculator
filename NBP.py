import requests

body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = body.json()

currency = input('Which currency do you want to exchange? [USD/EUR/CHF]: ')
quantity = int(input('What amount do you want to exchange? '))

for rate in response[0]['rates']:
    if currency == rate['code']:
        result = quantity * float(rate['mid'])
        print(f'You will receive {result} PLN.')
        break
