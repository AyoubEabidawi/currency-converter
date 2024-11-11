#Assignment 4

#Import Required Models
import requests


def get_available_currencies(api_key):

    url = 'https://api.freecurrencyapi.com/v1/currencies'
    params = {'apikey': api_key}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Return the JSON response containing currency data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
api_key = 'fca_live_tQrIiEqdsbJxZ4Hqac3ovbAKU5NVKCYIlFoOLALK'
currencies = get_available_currencies(api_key)
if currencies:
    print("Available Currencies:", currencies)
    

# Creat a menue    
print("What would you like to do today ?")
menu_option = int(input("1. list the available currencies\n2. Convert an amount from a base currency to another\nOption number:  "))

# Default Key
currency_key = "fca_live_tQrIiEqdsbJxZ4Hqac3ovbAKU5NVKCYIlFoOLALK"
currency_url = "https://api.freecurrencyapi.com/v1/currencies"+currency_key


if menu_option == 1 :
    currency_list = requests.get(currency_url)
    print(currency_list)
elif menu_option == 2:
    pass
else:
    print("You have entered Unvalid option")