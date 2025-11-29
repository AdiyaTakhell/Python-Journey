import requests
import sys


def main():
    try:
        btc=float(sys.argv[1])


        if btc:
            try:
                response = requests.get(
                    "https://rest.coincap.io/v3/assets/bitcoin?apiKey=32a33b2871263a0cb5bc2be9b81c6a32ce3eb4ae426366f6642c51b6774c0492")
                result = response.json()
                btc_price_usd=float(result["data"]["priceUsd"])
                amount=btc_price_usd*btc
                print(f"${amount:,.4f}")



            except requests.RequestException:
                print(f"Network Error")



    except ValueError:
        sys.exit("Command line Argument is not a number:")
    except IndexError:
        sys.exit("Missing Command Line Argument")

main()