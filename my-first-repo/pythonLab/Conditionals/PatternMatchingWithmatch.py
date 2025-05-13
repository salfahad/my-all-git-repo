##Lab 4: Pattern Matching with match
#1.Basic match Statement:
import calendar
import datetime
date = "september 14"

match date:
    case "september 14":
        print("Start of the work week.")
    case "september 16":
        print("Almost the weekend!")
    case _:
        print("Have a Holiday!")
