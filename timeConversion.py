#!/bin/python3

import os

HOURS_IN_HALF_DAY = 12
MIDNIGHT_HOUR = 0

def timeConversion(s):
    assert len(s) == 10, "Invalid time format"
    
    hour_12 = int(s[:2])
    assert 0 <= hour_12 <= HOURS_IN_HALF_DAY, "Invalid hour value"
    
    meridiem = s[-2:]
    assert meridiem in ["AM", "PM"], "Invalid meridium value"
    
    hour_24 = hour_12 % HOURS_IN_HALF_DAY + (HOURS_IN_HALF_DAY if meridiem == "PM" else 0)
    hour_str = str(hour_24) if hour_24 >= 10 else "0" + str(hour_24)
    
    return hour_str + s[2:8]

if __name__ == '__main__':
    time_str = input().strip()
    military_time_str = timeConversion(time_str)
    print(military_time_str)
