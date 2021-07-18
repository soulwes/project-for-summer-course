import requests
import keys_TG


class Rate:
    def __init__(self):
        self.prev_dollar = 0
        self.prev_euro = 0

    def exchange_dol(self) -> int:
        r = requests.get('https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB')
        item = sorted(r.json()['payload']['rates'],
                      key=lambda d: d['category'] == 'DebitCardsTransfers')[0]
        self.prev_dollar = item['sell']
        return item['sell']

    def exchange_eu(self) -> int:
        r = requests.get('https://api.tinkoff.ru/v1/currency_rates?from=EUR&to=RUB')
        item = sorted(r.json()['payload']['rates'],
                      key=lambda d: d['category'] == 'DebitCardsTransfers')[0]
        self.prev_euro = item['sell']
        return item['sell']


class Bank:
    def __init__(self):
        self.str = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

    def near_bank(self, location: str) -> str:
        radius = '2000'
        keyword = 'банк'
        parameters = 'location=' + location + '&radius=' + radius + '&keyword=' + keyword + '&language=ru-Ru' + '&key='
        parameters += keys_TG.google_token
        final_url = self.str + parameters
        response = requests.get(final_url)
        s = ''
        for el in response.json()['results']:
            if el['types'][0] == 'bank':
                s += el['name'] + ' по адресу ' + el['vicinity'] + '\n\n'
        return s


rate = Rate()
bank = Bank()
