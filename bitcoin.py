import sys
import json
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()

    bpi = r["bpi"]
    usd = bpi["USD"]
    rate_float = usd["rate_float"]
    value = float(sys.argv[1])
    rate_float = float(rate_float)
    amount = rate_float * value

    print(f"${amount:,.4f}")

except (requests.RequestException, ValueError):
    sys.exit("Command-line argument is not a number")
