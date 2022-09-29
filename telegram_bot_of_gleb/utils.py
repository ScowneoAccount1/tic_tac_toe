import requests
from extensions import keys

class ConvertionException(Exception):
    pass


class CursConverter:
    @staticmethod
    def convert(base:str, quote:str, amount:str):
        
        
        if quote == base:
            raise ConvertionException('одинаковые валюьты')
        
        #quote, base, data = CursConverter.convert(quote, base, amount)
        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'ну удалось обработать валюту "{base}"')
        
        try:
            base_ticker  = keys[quote]
        except KeyError:
            raise ConvertionException(f'ну удалось обработать валюту "{quote}"')
        
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException('не удалось обработать количество')
        
        data = requests.get(f"https://api.coingate.com/v2/rates/merchant/{base_ticker}/{quote_ticker}").json()
        return round(data, 5)
