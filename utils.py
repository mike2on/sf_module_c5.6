import requests
import json
from config import keys, api_key

class ConvertionException(Exception):
    pass

class MoneyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        quote_ticker, base_ticker = keys[quote], keys[base]

        if quote == base:
            raise ConvertionException('валюты одинаковы')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать количество валюты {amount}')

        r = requests.get(
            f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}',
            headers=api_key)

        total = json.loads(r.content)["result"]
        return total
