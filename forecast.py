# -*- coding: utf-8 -*-
"""

"""
import forscripts as fs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "place",
    help="Enter any place, it can be city, district, etc.")
parser.add_argument(
    "-d",
    "--date",
    help="Give --date 10/01/2019 or -d 10/01/2019 to view forecast for that date. Either of --date or --type args can be passed.")
parser.add_argument(
    "-t",
    "--type",
    help="Give --type argument for different type of forecast. Accepted types: '--type hourly/daily/now/5/15/five/fifteen' \t    *5/15 corresponds to 5days and 15days")

args = parser.parse_args()
print(args)
active = None

if args.date is not None:
    print("Date argument found")
    Date = args.date
    if args.type is not None:
        print("type also found, Only one is allowed.")
        active = "Both"
    else:
        active = "Date"
else:
    if args.type is not None:
        print("Type arg found")
        Type = args.type
        active = "Type"
        
print(active)
        
