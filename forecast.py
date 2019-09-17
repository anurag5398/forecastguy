#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
main file. python3 forecast.py place -t type/-d date
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
    help="Give --date 10/01/2019 or -d 10/01/2019 to view forecast for that date. Either of --date or --type args can be passed. Default: current")
parser.add_argument(
    "-t",
    "--type",
    help="Give --type argument for different type of forecast. Accepted types: '--type hourly/daily/now/5/15/five/fifteen' \t    *5/15 corresponds to 5days and 15days. Default: daily")

args = parser.parse_args()
print(args)
active = None


Place = args.place
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
print(args)

if __name__ == "__main__":
    if(active is None):
        fs.setapiKey()
        pName, pCode = fs.getplaces(str(Place))
        out = fs.displayTypeForecast(pCode, pName, "current")
        if(out == 1):
            print("Completed!!!")
        else:
            print("Maybe something went wrong! Check and try again!")

    elif(active == "Type"):
        fs.setapiKey()
        pName, pCode = fs.getplaces(str(Place))
        out = fs.displayTypeForecast(pCode, pName, Type)
        if(out == 1):
            print("Completed!!!")
        else:
            print("Maybe something went wrong! Check and try again!")

    elif(active == "Date"):
        temp = Date.split("/")
        if(len(temp) == 3):
            if(int(temp[0]) > 0 and int(temp[0]) < 32 and int(temp[1]) > 0 and int(temp[1]) < 13 and int(temp[2]) > 1700 and int(temp[2]) < 2400):
                fs.setapiKey()
                pName, pCode = fs.getplaces(str(Place))
                out = fs.displayDateForecast(pCode, pName, Date)
                if(out == 1):
                    print("Completed!!!")
                else:
                    print("Maybe something went wrong! Check and try again!")
            else:
                print(
                    "Enter Valid date. Ex: day(2 digit.01)/month(2 digit.03/10)/year(4 digit 2018)")
        else:
            print("Check your date. Ex: day/month/year")
