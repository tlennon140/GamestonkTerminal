import argparse
import finviz
import pandas as pd
from gamestonk_terminal.helper_funcs import parse_known_args_and_warn


def screener(l_args, s_ticker):
    parser = argparse.ArgumentParser(
        prog="screener",
        description="""
            Print several metrics about the company. The following fields are expected:
            Company, Sector, Industry, Country, Index, P/E, EPS (ttm), Insider Own,
            Shs Outstand, Perf Week, Market Cap, Forward P/E, EPS next Y, Insider Trans,
            Shs Float, Perf Month, Income, EPS next Q, Inst Own, Short Float, Perf Quarter,
            Sales, P/S, EPS this Y, Inst Trans, Short Ratio, Perf Half Y, Book/sh, P/B, ROA,
            Target Price, Perf Year, Cash/sh, P/C, ROE, 52W Range, Perf YTD, P/FCF, EPS past 5Y,
            ROI, 52W High, Beta, Quick Ratio, Sales past 5Y, Gross Margin, 52W Low, ATR,
            Employees, Current Ratio, Sales Q/Q, Oper. Margin, RSI (14), Volatility, Optionable,
            Debt/Eq, EPS Q/Q, Profit Margin, Rel Volume, Prev Close, Shortable, LT Debt/Eq,
            Earnings, Payout, Avg Volume, Price, Recom, SMA20, SMA50, SMA200, Volume, Change.
            [Source: Finviz]
        """,
    )

    try:
        parse_known_args_and_warn(parser, l_args)

        d_finviz_stock = finviz.get_stock(s_ticker)
        df_fa = pd.DataFrame.from_dict(
            d_finviz_stock, orient="index", columns=["Values"]
        )
        df_fa = df_fa[df_fa.Values != "-"]
        print(df_fa.to_string(header=False))

        print("")

    except Exception as e:
        print(e)
        print("")
        return
