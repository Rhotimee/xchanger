import requests

def naira():
    return 1334

# def naira():
#     response1 = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc")
#     response2 = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=btc-sbd")
#     response_ngn = requests.get("http://www.apilayer.net/api/live?access_key=a1c2abd1172003288d57872b5da731c4")
#     data1 = response1.json()
#     data2 = response2.json()
#     usd_btc = data1['result']['Last']
#     btc_sbd = data2['result']['Last']
#     usd_sbd = usd_btc * btc_sbd
#     return int(usd_sbd *365)