import os
import requests

class ExternalService:
    '''
    Manages external API calls.
    '''

    BASE_URI = os.getenv("EXCHANGE_RATE_API_URL")

    @classmethod
    def get_exchange_rate(cls, currency_code="VES") -> float:
        '''
        Retrieves the current exchange rate from an external API.
        '''

        default_rate = 1

        if not cls.BASE_URI:
            raise ValueError("Exchange rate API URL is not configured.")
        
        uri = cls.BASE_URI
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.request("GET", uri, headers=headers)
            exchange_rate = response.json().get("rates", {}).get(currency_code)
            return exchange_rate if exchange_rate is not None else default_rate
        except requests.RequestException as e:
            return default_rate