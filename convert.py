from datetime import date
import pandas as pd
import numpy as np

def convert_time(time_series):
    month_dict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12,
                  "January":1, "February":2, "March":3, "April":4, "June":6, "July":7, "August":8, "September":9, "October":10,
                  "November":11, "December":12}

    return_series = pd.Series(dtype=np.float64)

    for i in time_series.index:
        time_str = time_series.at[i].replace(",", "").split(" ")
        month = month_dict[time_str[1]]
        if len(time_str) >= 4:
            day = int(time_str[2])
            year = int(time_str[3])
        else:
            day = 1
            year = int(time_str[2])
        
        return_series.at[i] = date(year, month, day)
    
    return return_series

def convert_unit(unit_series):
    return_series = pd.Series(dtype=np.float64)

    for i in unit_series.index:
        if type(unit_series.at[i]) == float or type(unit_series.at[i]) == np.float64:
            return_series.at[i] = unit_series.at[i]
        else:
            return_series.at[i] = float(unit_series.at[i].replace(",", "").split(" ")[0])
    
    return return_series

def convert_money(money_series):
    return convert_unit(money_series.str.replace("$", ""))

