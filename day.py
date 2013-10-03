#!/usr/bin/python2

import datetime

weekday_names = {
  0: "Monday",
  1: "Tuesday",
  2: "Wednesday",
  3: "Thursday",
  4: "Friday",
  5: "Saturday",
  6: "Sunday",
}

def main():
  print weekday_names[getDayOfWeek()] + ",",
  print(getToday())

def getToday():
  today = datetime.date
  return today.today()

def getDayOfWeek():
  date = datetime.date
  today = date.today()
  year = today.year
  month = today.month
  day = today.month
  return date(year, month, day).weekday()


main()
