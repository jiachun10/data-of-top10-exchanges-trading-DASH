
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
    (result: In general, we found that if an exchange failed this test, it would fail almost all the
others as well,which means that they don't make their data avaliable)
    2.  criterion 2: for each trade with price p and size x, checked the most recently-reported orderbook whether a) contained bids with totalling size>=x and averege price >=p, or offers with totalling size >=x and average price <=p. if neither the two conditions is met, it failed
    (result: Note that the distribution is bimodal, with most exchanges either having close to 0 or close to all of their trades crossing the best bid or offer)
    3.  criterion 3: having set of reputable exchanges established(strict regulation):Coinbase, Poloniex, Bittrex, Gemini, Kraken, Bitstamp, and itBit(**we need to choose our own index for dash market**). creating a time series by summing their volume up per unit of time, and calculate the correlation of other exchanges' volume by time.
    if correlation>=0.5, it passes the criterion.
    ![alt text](https://github.com/jiachun10/data-of-top10-exchanges-trading-DASH/blob/master/Screen%20Shot%202020-06-13%20at%208.19.47%20PM%20copy.png)
    4.  invest 500 millions usd(pass)
    5.  criterion 5: if *order book ratio*>=0.005 pass the criterion
        1.  for c1/c2 pairs, getting order book threshold σt at time t is the sum of the hourly
standard deviations (in terms of USD) of c1 and c2.
        2.  define the *order book depth* to be the total of all the orders
on the order book with price within σt of the best bid and offer
        3.  order book ratio=order book depth/exchange's reported average daily volume for c1/c2
    6.  criterion 6: saying that having real c1/c2 market: if order book ratio>=10^(-6), if an exchange  has <= 5% fake market, then this exchange pass the criterion
