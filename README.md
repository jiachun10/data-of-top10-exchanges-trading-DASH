
# data-of-top10-exchanges-trading-DASH
Use exchange API to get trading data of DASH


# Is cryptocurrency price manipulated?

## Ranking top 10 exchanges trading DASH

### daijiachun
1. nomics 
    1. advantages
        1. nomics dose not charge for exchage listing, only creating deep data integration
    2. disadvantages
        1. don't mention does they proofread the historical or current data 
2. summary of the evaluation
    1.  criterion 1: an exchange is considered to fail this criterion if more than 10% of its trades by volume did not appear on its order book prior or if we could identify its prints as time-delayed relays from other exchanges.
    2.  criterion 2: for each trade with price p and size x, checked the most recently-reported orderbook whether a) contained bids with totalling size>=x and averege price >=p, or offers with totalling size >=x and average price <=p. if neither the two conditions is met, it failed
    3.  criterion 3: having set of reputable exchanges established(strict regulation):Coinbase, Poloniex, Bittrex, Gemini, Kraken, Bitstamp, and itBit. creating a time series by summing their volume up per unit of time, and calculate the correlation of other exchanges' volume by time.
    if correlation>=0.5, it passes the criterion
    4.  invest 500 millions usd(pass)
    5.  criterion 5: 
        a) for c1/c2 pairs, getting order book threshold σt at time t is the sum of the hourly
standard deviations (in terms of USD) of c1 and c2.
