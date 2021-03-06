
# GamestonkTerminal 🚀

[![Build Status](https://github.com/DidierRLopes/GamestonkTerminal/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/DidierRLopes/GamestonkTerminal/actions)
[![GitHub release](https://img.shields.io/github/release/DidierRLopes/GamestonkTerminal.svg?maxAge=3600)](https://github.com/DidierRLopes/GamestonkTerminal/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About

Gamestonk Terminal is an awesome stock and crypto market terminal that has been developed for fun, while I saw my GME shares tanking. But hey, I like the stock 💎🙌.

The implementation (in python) allows to easily add more commands, and expand on their configuration.

Feel free to request features, I'll be happy to work on them on my spare time.

## Table of contents

* [Features](#Features)
  * [Discover Stocks](#Discover_Stocks)
  * [Market Sentiment](#Market_Sentiment)
  * [Research Web pages](#Research_Web_pages)
  * [Fundamental Analysis](#Fundamental_Analysis)
  * [Technical Analysis](#Technical_Analysis)
  * [Due Diligence](#Due_Diligence)
  * [Prediction Techniques](#Prediction_Techniques)
* [Install](#Install)
* [API Keys](#API_Keys)
* [Disclaimer](#Disclaimer)
* [Support](#Support)

## Features <a name="Features"></a>

The main menu allows the following commands:

```text
load -t S_TICKER [-s S_START_DATE] [-i {1,5,15,30,60}]
```

* Load stock ticker to perform analysis on
  * -s : The starting date (format YYYY-MM-DD) of the stock
  * -i : Intraday stock minutes

```text
clear
```

* Clear previously loaded stock ticker.

```text
view -t S_TICKER [-s S_START_DATE] [-i {1,5,15,30,60}] [--type N_TYPE]
```

* Visualise historical data of a stock. An alpha_vantage key is necessary.
  * -s : The starting date (format YYYY-MM-DD) of the stock
  * -i : Intraday stock minutes
  * --type : 1234 corresponds to types: 1. open; 2. high; 3.low; 4. close; while 14 corresponds to types: 1.open; 4. close

![GNUS](https://user-images.githubusercontent.com/25267873/108925137-f2920e80-7633-11eb-8274-6e3bb6a19592.png)

Note: Until a ticker is loaded, the menu will only show *disc* and *sen* menu, as the others require a ticker being provided.

### [Discover Stocks](gamestonk_terminal/discovery/README.md) <a name="Discover_Stocks"></a>

Command|Description|Source
---|---|---
`map`           |S&P500 index stocks map |[Finviz](https://finviz.com)
`sectors`       |show sectors performance |[Alpha Vantage](www.alphavantage.co)
`gainers`       |show latest top gainers |[Yahoo Finance](https://finance.yahoo.com/)
`orders`        |orders by Fidelity Customers |[Fidelity](https://www.fidelity.com/)
`up_earnings`   |upcoming earnings release dates |[Seeking Alpha](https://seekingalpha.com/)
`high_short`    |show top high short interest stocks of over 20% ratio |[High Short Interest](https://www.highshortinterest.com/)
`low_float`     |show low float stocks under 10M shares float |[Low Float](https://www.lowfloat.com/)
`simply_wallst` |Simply Wall St. research data |[Simply Wall St.](https://simplywall.st/about)
`spachero`      |great website for SPACs research |[SpacHero](https://www.spachero.com/)
`uwhales`       |good website for SPACs research |[UnusualWhales](https://unusualwhales.com/)

### [Market Sentiment](gamestonk_terminal/sentiment/README.md) <a name="Market_Sentiment"></a>

Command|Description
----|----
[Reddit](https://reddit.com)|
`wsb`           |show what WSB gang is up to in subreddit wallstreetbets
`watchlist`     |show other users watchlist
`popular`       |show popular tickers
`spac_c`        |show other users spacs announcements from subreddit SPACs community
`spac`          |show other users spacs announcements from other subs
[Stocktwits](https://stocktwits.com/)|
`bullbear`      |estimate quick sentiment from last 30 messages on board
`messages`      |output up to the 30 last messages on the board
`trending`      |trending stocks
`stalker`       |stalk stocktwits user's last message
[Twitter](https://twitter.com/)|
`infer`         |infer about stock's sentiment from latest tweets
`sentiment`     |in-depth sentiment prediction from tweets over time
[Google](https://google.com/)|
`mentions`      |interest over time based on stock's mentions
`regions`       |regions that show highest interest in stock
`queries`       |top related queries with this stock
`rise`          |top rising related queries with stock

### Research Web pages <a name="Research_Web_pages"></a>

Command|Website
----|----
`macroaxis`         |www.macroaxis.com
`yahoo`             |www.finance.yahoo.com
`finviz`            |www.finviz.com
`marketwatch`       |www.marketwatch.com
`fool`              |www.fool.com
`businessinsider`   |www.markets.businessinsider.com
`fmp`               |www.financialmodelingprep.com
`fidelity`          |www.eresearch.fidelity.com
`tradingview`       |www.tradingview.com
`marketchameleon`   |www.marketchameleon.com
`stockrow`          |www.stockrow.com
`barchart`          |www.barchart.com
`grufity`           |www.grufity.com
`fintel`            |www.fintel.com
`zacks`             |www.zacks.com
`macrotrends`       |www.macrotrends.net
`newsfilter`        |www.newsfilter.io
`resources`         |www.tradinganalysisresources.com

### [Fundamental Analysis](gamestonk_terminal/fundamental_analysis/README.md) <a name="Fundamental_Analysis"></a>

Command|Description
----- | ---------
`screener`      |screen info about the company ([Finviz](https://finviz.com/))
`mgmt`          |management team of the company ([Business Insider](https://markets.businessinsider.com/))
[Market Watch API](https://markets.businessinsider.com/) |
`income`        |income statement of the company
`assets`        |assets of the company
`liabilities`   |liabilities and shareholders equity of the company
`operating`     |cash flow operating activities of the company
`investing`     |cash flow investing activities of the company
`financing`     |cash flow financing activities of the company
[Yahoo Finance API](https://finance.yahoo.com/) |
`info`          |information scope of the company
`shrs`          |shareholders of the company
`sust`          |sustainability values of the company
`cal`           |calendar earnings and estimates of the company
[Alpha Vantage API](https://www.alphavantage.co/) |
`overview`      |overview of the company
`income`        |income statements of the company
`balance`       |balance sheet of the company
`cash`          |cash flow of the company
`earnings`      |earnings dates and reported EPS
[Financial Modeling Prep API](https://financialmodelingprep.com/) |
`profile`       |profile of the company
`quote`         |quote of the company
`enterprise`    |enterprise value of the company over time
`dcf`           |discounted cash flow of the company over time
`inc`           |income statements of the company
`bal`           |balance sheet of the company
`cashf`         |cash flow of the company
`metrics`       |key metrics of the company
`ratios`        |financial ratios of the company
`growth`        |financial statement growth of the company

### [Technical Analysis](gamestonk_terminal/technical_analysis/README.md) <a name="Technical_Analysis"></a>

Command | Description | Sources
------ | ------ | ------
[overlap](https://github.com/twopirllc/pandas-ta/tree/master/pandas_ta/overlap) |
`ema`         | exponential moving average | [Wikipedia](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average), [Investopedia](https://www.investopedia.com/terms/e/ema.asp)
`sma`         |simple moving average | [Wikipedia](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average_(boxcar_filter)), [Investopedia](https://www.investopedia.com/terms/s/sma.asp)
`vwap`        |volume weighted average price | [Wikipedia](https://en.wikipedia.org/wiki/Volume-weighted_average_price), [Investopedia](https://www.investopedia.com/terms/v/vwap.asp)
[momentum](https://github.com/twopirllc/pandas-ta/tree/master/pandas_ta/momentum) |
`cci`         |commodity channel index | [Wikipedia](https://en.wikipedia.org/wiki/Commodity_channel_index), [Investopedia](https://www.investopedia.com/terms/c/commoditychannelindex.asp)
`macd`        |moving average convergence/divergence | [Wikipedia](https://en.wikipedia.org/wiki/MACD), [Investopedia](https://www.investopedia.com/terms/m/macd.asp)
`rsi`         |relative strength index | [Wikipedia](https://en.wikipedia.org/wiki/Relative_strength_index), [Investopedia](https://www.investopedia.com/terms/r/rsi.asp)
`stoch`       |stochastic oscillator | [Wikipedia](https://en.wikipedia.org/wiki/Stochastic_oscillator), [Investopedia](https://www.investopedia.com/terms/s/stochasticoscillator.asp)
[trend](https://github.com/twopirllc/pandas-ta/tree/master/pandas_ta/trend) |
`adx`         |average directional movement index | [Wikipedia](https://en.wikipedia.org/wiki/Average_directional_movement_index), [Investopedia](https://www.investopedia.com/terms/a/adx.asp)
`aroon`       |aroon indicator | [Investopedia](https://www.investopedia.com/terms/a/aroon.asp)
[volatility](https://github.com/twopirllc/pandas-ta/tree/master/pandas_ta/volatility) |
`bbands`      |bollinger bands | [Wikipedia](https://en.wikipedia.org/wiki/Bollinger_Bands), [Investopedia](https://www.investopedia.com/terms/b/bollingerbands.asp)
[volume](https://github.com/twopirllc/pandas-ta/tree/master/pandas_ta/volume) |
`ad`          |chaikin accumulation/distribution line values | [Wikipedia](https://en.wikipedia.org/wiki/Accumulation/distribution_index), [Investopedia](https://www.investopedia.com/terms/a/accumulationdistribution.asp)
`obv`         |on balance volume | [Wikipedia](https://en.wikipedia.org/wiki/On-balance_volume), [Investopedia](https://www.investopedia.com/terms/o/onbalancevolume.asp)

### [Due Diligence](gamestonk_terminal/due_diligence/README.md) <a name="Due_Diligence"></a>

Command|Explanation|Source
------ | --------|----
`news`          |latest news of the company |[Finviz](https://finviz.com/)
`red`           |gets due diligence from another user's post |[Reddit](https://reddit.com)
`analyst`       |analyst prices and ratings of the company |[Finviz](https://finviz.com/)
`rating`        |rating of the company from strong sell to strong buy | [FMP](https://financialmodelingprep.com/)
`pt`            |price targets over time |[Business Insider](https://www.businessinsider.com/)
`est`           |quarter and year analysts earnings estimates |[Business Insider](https://www.businessinsider.com/)
`ins`           |insider activity over time |[Business Insider](https://www.businessinsider.com/)
`insider`       |insider trading of the company |[Finviz](https://finviz.com/)
`sec`           |SEC filings |[MarketWatch](https://www.marketwatch.com/)
`short`         |short interest |[Quandl](https://www.quandl.com/)
`warnings`      |company warnings according to Sean Seah book |[MarketWatch](https://www.marketwatch.com/)

### [Prediction Techniques](gamestonk_terminal/prediction_techniques/README.md) <a name="Prediction_Techniques"></a>

Command|Technique|Sources
------ | ------------|---
`sma`         |simple moving average | [Wikipedia](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average), [Investopedia](https://www.investopedia.com/terms/s/sma.asp)
`knn`         |k-Nearest Neighbors | [Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
`linear`      |linear regression (polynomial 1) | [Wikipedia](https://en.wikipedia.org/wiki/Linear_regression), [Investopedia](https://www.investopedia.com/terms/r/regression.asp)
`quadratic`   |quadratic regression (polynomial 2) | [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_regression), [Investopedia](https://www.investopedia.com/terms/r/regression.asp)
`cubic`       |cubic regression (polynomial 3) | [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_regression), [Investopedia](https://www.investopedia.com/terms/r/regression.asp)
`regression`  |regression (other polynomial) | [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_regression), [Investopedia](https://www.investopedia.com/terms/r/regression.asp)
`arima`       |autoregressive integrated moving average | [Wikipedia](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average), [Investopedia](https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp)
`prophet`     |Facebook's prophet prediction | [Details](https://facebook.github.io/prophet/)
`mlp`         |MultiLayer Perceptron | [Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron)
`rnn`         |Recurrent Neural Network  | [Wikipedia](https://en.wikipedia.org/wiki/Recurrent_neural_network)
`lstm`        |Long Short-Term Memory  | [Wikipedia](https://en.wikipedia.org/wiki/Long_short-term_memory), [Details](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## Install <a name="Install"></a>

This project was written and tested with Python 3.6.8.

In order to install, you must run:

```text
git clone https://github.com/DidierRLopes/GamestonkTerminal
cd GamestonkTerminal/
pip install -r requirements.txt
```

Then run:

```text
python terminal.py
```

Note: The libraries specified in the [requirements.txt](/requirements.txt) file have been tested and work for the purpose of this project, however, these may be older versions. Hence, it is recommended for the user to set up a virtual python environment prior to installing these. This allows to keep dependencies required by different projects in separate places.

Note: The libraries specified in the [requirements.txt](/requirements.txt) file have been tested and work for the purpose of this project, however, these may be older versions. Hence, it is recommended for the user to set up a virtual python environment prior to installing these. This allows to keep dependencies required by different projects in separate places.

## API Keys <a name="API_Keys"></a>

The project is build around several different API calls, whether it is to access historical data or financials.

These are the ones where a key is necessary:

* Alpha Vantage: <https://www.alphavantage.co>
* Financial Modeling Prep: <https://financialmodelingprep.com/developer>
* Quandl: <https://www.quandl.com/tools/api>
* Reddit: <https://www.reddit.com/prefs/apps>
* Twitter: <https://developer.twitter.com>

When these are obtained, don't forget to update [config_terminal.py](gamestonk_terminal/config_terminal.py).  Alternatively, you can also set them to the following environment variables

* GT_API_KEY_ALPHAVANTAGE
* GT_API_KEY_FINANCIALMODELINGPREP
* GT_API_KEY_QUANDL
* GT_API_REDDIT_CLIENT_ID
* GT_API_REDDIT_CLIENT_SECRET
* GT_API_REDDIT_USERNAME
* GT_API_REDDIT_USER_AGENT
* GT_API_REDDIT_PASSWORD
* GT_API_TWITTER_KEY
* GT_API_TWITTER_SECRET_KEY
* GT_API_TWITTER_BEARER_TOKEN.

Note that it is not necessary to have a valid Alpha Vantage key to get daily OHLC values.

## Disclaimer <a name="Disclaimer"></a>

"A few things I am not. I am not a cat. I am not an institutional investor, nor am I a hedge fund. I do not have clients and I do not provide personalized investment advice for fees or commissions." DFV

## Support <a name="Support"></a>

If you like this project, and would like me to maintain it and keep adding features, feel free to buy me a coffee!

<a href="https://www.buymeacoffee.com/didierlopes" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>
