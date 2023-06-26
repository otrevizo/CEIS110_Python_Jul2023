# -*- coding: utf-8 -*-
"""
CEIS110 lab 3 (2019 - 2022)

"""


# %% Week 3 - Build DB

# Purpose: Build weather database from NOAA data
# Name: Your name
# Date: the date
# See https://pypi.org/project/noaa-sdk/ for details on noaa_sdk package used

# %% Import libraries
#
from noaa_sdk import noaa
import sqlite3
import datetime

# %% init data
print("CEIS110 Week 3")

# parameters for retrieving NOAA weather data
zipCode = "60610"  # change to your postal code
country = "US"

# date-time format is yyyy-mm-ddThh:mm:ssZ, times are Zulu time (GMT)
#
# gets the most recent 14 days of data
#
today = datetime.datetime.now()
past = today - datetime.timedelta(days=14)
startDate = past.strftime("%Y-%m-%dT00:00:00Z")
endDate = today.strftime("%Y-%m-%dT23:59:59Z")

# %% Connect SQL
#
# create connection - this creates database if not exist
print("Preparing database...")
dbFile = "weather.db"

# Establish a connection to SQL
conn = sqlite3.connect(dbFile)
# create cursor to execute SQL commands
cur = conn.cursor()

# drop previous version of table if any so we start fresh each time
dropTableCmd = "DROP TABLE IF EXISTS observations;"
cur.execute(dropTableCmd)

# %% Create SQL table
# create new table to store observations
createTableCmd = """ CREATE TABLE IF NOT EXISTS observations (
                        timestamp TEXT NOT NULL PRIMARY KEY,
                        windSpeed REAL,
                        temperature REAL,
                        relativeHumidity REAL,
                        windDirection INTEGER,
                        barometricPressure INTEGER,
                        visibility INTEGER,
                        textDescription TEXT
                     ) ; """
cur.execute(createTableCmd)
print("Database prepared")

# %% Get NOAA data
#
# get hourly weather observations from NOAA Weather Service API
print("Getting weather data...")
n = noaa.NOAA()
observations = n.get_observations(zipCode, country, startDate, endDate)

# %% Insert SQL data
#
# populate table with weather observations
print("Inserting rows...")

# The following variable is required by the database
insertCmd = """ INSERT INTO observations
(timestamp, windSpeed, temperature, relativeHumidity, windDirection,
barometricPressure, visibility, textDescription)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

count = 0
for obs in observations:
    insertValues = (obs["timestamp"],
                    obs["windSpeed"]["value"],
                    obs["temperature"]["value"],
                    obs["relativeHumidity"]["value"],
                    obs["windDirection"]["value"],
                    obs["barometricPressure"]["value"],
                    obs["visibility"]["value"],
                    obs["textDescription"])
    cur.execute(insertCmd, insertValues)
    count += 1

if count > 0:
    cur.execute("COMMIT;")

print(count, "rows inserted")
print("Database load complete!")



# %% References
"""
Tips and references:

runfile('filename.py')

# Delete all variables from the namespace
%reset
help(functioname)

References:
* DeVry University CEIS110 labs 2019 - 2022
* NOAA package documentation https://pypi.org/project/noaa-sdk/
* MySQL Documentation https://dev.mysql.com/doc/
* MySQL Tutorial https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
* sqlite3 documentation https://docs.python.org/3/library/sqlite3.html
* Python datetime module https://docs.python.org/3/library/datetime.html

"""
