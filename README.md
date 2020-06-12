## 1. Ranking top 5 exchanges trading DASH based on transparency

Based on the measures given by Nomics https://blog.nomics.com/essays/transparency-ratings/, we summarized its rating method, advantages and disadvantages, and would like to establish our own reliable and explicit ranking rules for cryptocurrency exchanges.

### Nomics' Exchanges Transparency Ratings

#### Historical Trade-Level Data
According to the examination of 10 trusted exchanges revealed by Bitwise, Nomics found eight of the 10 exchanges provide historical trade level data which is considered *the most granular and audible* form of data available. In contrast, for the exchanges called bad actors by Bitwise, every single one of them provides limited trading history and virtually no granularity around trading activity.

Nomics assign 7 types of transparency scores (A+,A,A-,B,C,D,F) to exchanges. The middle one is score B which represents a good exchange. For one to have rating B, it must provide, at the very least, this much candle history:
* 1-Day Candles: 7 candles with last candle occurring within a rolling 48 hours
* 1-Hour Candles: 24 candles with last candle occurring within a rolling 2 hours
* 1-Minute Candles: 60 candles with last candle occurring within a rolling 10 minutes

One advantage of Nomics ratings is that these are not subjective. They check their database and exchange APIs to determine the qualitiy of data. Meanwhile, Nomics says they have never charged for exchange listings. 

However, I think it is possible that the data obtained by exchange APIs is fake although exchanges release all historical data because some exchanges may follow the trend of very big exchanges such as Binance to simulate fake data. 

### Our Criterion 

In addition to the transparency score from Nomics, our ratings will analyze the trade data further and consider aspects besides data itself to draw our final conlusions.

* Alexa rank (more details at https://blog.alexa.com/marketing-research/alexa-rank/)
Alexa rank is a measure of website popularity, and it ranks millions of websites in order of popularity. This is a good feature to detect exchanges that do fake volumes in order to be listed first in websites like coinmarketcap. For example, if we rank active market pairs for DASH, the first one is DASH/TRX, traded in Cat.Ex with a volume(24h) $103,717,243. However, its official website only ranks 72,293 in the global Internet traffic over past 90 days. In this sense, volume is a very misleading factor and Alexa rank can be used to detect if exchanges post fake voumes effectively.

* Data consistency
(build candle data from historical trade data, and to see if the candle data is consistent with the released ticker data)


