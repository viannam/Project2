#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import sql, select, join, desc

# Create a Engine object which is our handle into the database.
engine = create_engine('sqlite:///../world.sqlite')

# Connect to the database
conn = engine.connect() #conextion

# Read the metadata from the existing database.
#  Since the database already exists and has tables defined, we can create Python objects based on these automatically.
DBInfo=MetaData(engine)

# Auto-create the city object basedon the metadata read into the DBInfo.
country=Table('country', DBInfo, autoload=True)
city=Table('city', DBInfo, autoload=True)

query=select([country.c.Name, country.c.Continent, country.c.LifeExpectancy, country.c.Population, country.c.IndepYear, country.c.GNP])
result = conn.execute(query)
for row in result:
    print(row)

import pandas as pd

df=pd.read_sql(query, conn)

df.head()
