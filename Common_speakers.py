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
language=Table('countrylanguage', DBInfo, autoload=True)

#Selecting countries and official languagues from the sqlite database
query=select([country.c.Name,language.c.Language,language.c.IsOfficial])\
        .select_from(country.join(language))\
        .where(language.c.IsOfficial =='T')
country_language=conn.execute(query)

official_language=[]
c_language=[]
for item in country_language:
    official_language.append(item[1])
    c_language.append(item)

#Creating user input
while True:
    print("-------------------------")
    name = input("Enter an official language: ")
    cName = name.title()
    if cName not in official_language:
        print(f"{cName} language not found. Please, try again!")
    else: 
        print("We found places that speak your language!")
        break
#Grouping the commum speaker countries
common_speakers = []
for index in range(len(c_language)):
    #print(c_language[index])
    if cName == c_language[index][1]:
        common_speakers.append(c_language[index][0])

print(f"The following countries speak {cName}: {common_speakers}")
