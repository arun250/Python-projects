from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.currencyapi.com/"
API_KEY = "cur_live_bmLMlue5IBcfFlS9VDUcjI5OyPyK3gewn4PUbjOE"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v3/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()["data"]
    data = list(data.items())
    data.sort()
    return data

def print_currencies(currencies):
    for name, currency in currencies:
        code = currency["code"]
        value = currency["value"]
        print(f'{code} - {value}')
        
def exchange_rate(currency1, currency2):
    endpoint = f"v3/latest?base_currency={currency1}&currencies={currency2}&apikey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()['data']
    
    if len(data) == 0:
        print("invalid currencies.")
        return 
    else:
        data = list(data.items())
        for name, currency in data:
            code = currency["code"]
            value = currency["value"]
            print(f"{currency1}  -> {currency2} = {value}")
            return value
        
def convert(currency1, currency2, amount):
    rate =  exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("invalid amount")
        return 
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount}{currency2}")    
    return converted_amount
    
    printer.pprint(data)
        

def main():
    currencies = get_currencies()
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from the currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()
    
    while True:
        command = input("Enter a command q to quit").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            c1 = input("eenter the base  curr").upper()
            amount = input(f"enter the amount in {c1}: ")
            c2 = input("eenter the curr to conver to ").upper()
            convert(c1, c2, amount)
        elif command == "rate":
            c1 = input("eenter the base  curr").upper()
            c2 = input("eenter the curr to conver to ").upper()
            exchange_rate(c1, c2)
        else:
            print("Unrecognized command")
            
main()
            
            
            
   
    


#data = get_currencies()
#printer.pprint(data)
#print_currencies(data)
#rate = exchange_rate("EUR","INR")
#print(rate)