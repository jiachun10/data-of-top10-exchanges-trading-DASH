import requests
from time
import pandas as pd

# Cat.Ex
def catex_order(url, pair='DASH/TRX'):
	""" return a dataframe of the order book,
            containing columns exchange, pair, type, price, vol, timestamp.
	"""

	timestamp = int(time.time()*1000) # currrent timestamp

	# identify market pair
	request_url = url + """?market={0}&limit=100""".format(pair) # maximum limit is 100
	response = requests.get(request_url)

	# order_dictionary
	order_dict = response.json()['data'][0]
	ask = order_dict['asks'] # ask
	bid = order_dict['bids'] # bid

	ask_price = [float(item[0]) for item in ask]
	ask_vol = [float(item[1]) for item in ask]
	bid_price = [float(item[0]) for item in bid]
	bid_vol = [float(item[1])  for item in bid]

	# build dataframe from dict
	res_dict = {
	'exchange': 'Cat.Ex',
	'pair': pair,
	'type': ['ask']*100 + ['bid']*100,
	'price': ask_price + bid_price,
	'vol': ask_vol + bid_vol,
	'timestamp': timestamp
	}

	return pd.DataFrame(res_dict)

if __name__ == '__main__':
	# test catex_orderbook
	url = """https://www.catex.io/api/order"""
	df = catex_order(url)
	df.head()
