# -*- coding: utf-8 -*-
"""
CEIS110 lab 3 (2019 - 2022)

"""
# %% Week 4 - Query DB

# Purpose: Query database using SQL
# Name: Your name
# Date: Your date
# Run BuildWeatherDB.py to build weather database before running this program

# %% Import libraries

import sqlite3
import pandas as pd

# %% Init options
#
# format output
#
# There is another Pandas method get_option() that is related.
#
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

# %% SQL establish connection
#
# connect to and query weather database
#
# Assign the database file to a variable named dbFile 
#
dbFile = "weather.db"

# Connect to the database
#
# Requirement: the database must have been created already in Lab 3.
#
conn = sqlite3.connect(dbFile)

# %% SQL query by timestamp
#
# Reference https://dev.mysql.com/doc/refman/8.0/en/select.html
#
selectCmd = " SELECT * FROM observations ORDER BY timestamp; "

result = pd.read_sql_query(selectCmd, conn)

print(result)

# %% SQL query min/max temp
# To see the lowest and highest temperatures observed in this data set...

selectCmd = " SELECT MIN(temperature), MAX(temperature) FROM observations; "

result = pd.read_sql_query(selectCmd, conn)

print(result)

# %% SQL query temp, wind when clear
# To find the temperature and windspeed with a textDescription of clear. 

selectCmd = "SELECT temperature, windspeed, textDescription \
     FROM observations where textDescription = 'Clear'; "

result = pd.read_sql_query(selectCmd, conn)

print(result)


# %% References
"""
Tips and references:

runfile('filename.py')

# Delete all variables from the namespace
%reset
help(functioname)

References:
* MySQL Documentation https://dev.mysql.com/doc/
* MySQL Tutorial https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
* sqlite3 documentation https://docs.python.org/3/library/sqlite3.html
* Pandas documentation https://pandas.pydata.org/docs/
* Pandas read_sql_query() https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html?highlight=read_sql#pandas.read_sql_query

"""
