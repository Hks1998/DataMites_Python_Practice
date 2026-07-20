import json
import urllib.request

def convert_currency(amount, from_curr, to_curr):
    # API URL for live conversion using standard ISO codes
    url = f"https://frankfurter.app/latest?amount={amount}&from={from_curr.upper()}&to={to_curr.upper()}"
    
    try:
        # Fetch the exchange rates from the web
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
        rate = data['rates'][to_curr.upper()]
        return rate
    except Exception as e:
        print(f"Error fetching conversion: {e}")
        return None

# User Inputs
amount_to_convert = float(input("Enter amount: "))
source_currency = input("From currency (e.g., USD): ").upper()
target_currency = input("To currency (e.g., INR): ").upper()

# Calculate & Display
converted_amount = convert_currency(amount_to_convert, source_currency, target_currency)

if converted_amount is not None:
    print(f"{amount_to_convert} {source_currency} = {converted_amount} {target_currency}")
