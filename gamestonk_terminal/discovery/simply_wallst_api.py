import argparse
import webbrowser
from gamestonk_terminal.helper_funcs import parse_known_args_and_warn


def simply_wallst(l_args):
    parser = argparse.ArgumentParser(
        prog="simply_wallst",
        description="""
            Simply Wall Street Research. Opens web browser. Although this does not require
            an API key, it requires a subscription to the website by the user
            (there's a 14 days free trial).[Source: Simply Wall St.]
        """,
    )

    parser.add_argument(
        "-i",
        "--industry",
        action="store",
        dest="s_industry",
        type=str,
        default="any",
        help="Industry of interest.",
        choices=[
            "any",
            "automobiles",
            "banks",
            "capital-goods",
            "commercial-services",
            "consumer-durables",
            "consumer-services",
            "diversified-financials",
            "energy",
            "consumer-retailing",
            "food-beverage-tobacco",
            "healthcare",
            "household",
            "insurance",
            "materials",
            "media",
            "pharmaceuticals-biotech",
            "real-estate",
            "retail",
            "semiconductors",
            "software",
            "tech",
            "telecom",
            "transportation",
            "utilities",
        ],
    )

    ns_parser = parse_known_args_and_warn(parser, l_args)

    webbrowser.open(f"https://simplywall.st/stocks/us/{ns_parser.s_industry}?page=1")
    print("")
