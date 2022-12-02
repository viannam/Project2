#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import data

import os
os.chdir('/Users/paul.adunola/Desktop')
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import sql, select, join, desc
from sqlalchemy import inspect

# Create a Engine object which is our handle into the database.
engine = create_engine('sqlite:///world.sqlite')

# Connect to the database
conn = engine.connect() #conextion


# In[ ]:


# Read the metadata from the existing database.
#  Since the database already exists and has tables defined, 
#we can create Python objects based on these automatically.
DBInfo=MetaData(engine)


# In[ ]:


#Check tables present in engine
inspector = inspect(engine)
schemas = inspector.get_schema_names()
print(inspector.get_table_names())


# In[ ]:


# Auto-create the city object basedon the metadata read into the DBInfo.
country=Table('country', DBInfo, autoload=True)
city=Table('city', DBInfo, autoload=True)
language=Table('countrylanguage', DBInfo, autoload=True)


# In[ ]:


print("------------------------------- Continent Info -------------------------------")
continent_lst = ['Africa','Asia','Europe','North America','South America','Oceania']

#Check if country is present in the list
while True:
    print("-------------------------")
    print("Enter the name of any continent of your choice.")
    name = input("Enter Africa, Asia,Europe,North America, Oceania or South America: ")
    name.lower()
    continent = name.title()
    if continent not in continent_lst:
        print(f"{continent} not found. Try again!")
    else:
        print(f"{continent} found!")
        break

#Query data
query=select([country.c.Name,country.c.Continent,country.c.SurfaceArea,country.c.IndepYear,country.c.Population,country.c.LifeExpectancy,country.c.GNP,country.c.GovernmentForm]).where(country.c.Continent == continent )
result = conn.execute(query)

#Assigning Index of data to variable
SurfaceArea = 2
IndepYear = 3
Population = 4
LifeExpectancy = 5
GNP = 6

#Store querried data is list
result1 = []
for row in result:
    result1.append(row)

#Function for getting information summary about a continent
def continentSummary(result1):
    count = 0
    country_lst = []
    for index in range(len(result1)):
        count += 1
        country_lst.append(result1[index][0])
    country_lst.sort()
    return(count,country_lst)

#Function for getting largest information about a continent
def countryInfo_largest(pos):
    Info = 0
    for index in range(len(result1)):
        try:
            countryInfo = int(result1[index][pos])
            lc = result1[index][0]
            if countryInfo > Info:
                Info = countryInfo
                largestCountry = lc
        except:
            continue
    return(largestCountry,Info)
        
#Function for getting smallest information about a continent     
def countryInfo_smallest(pos):
    for index in range(len(result1)):
        try:
            countryInfo = int(result1[index][pos])
            if index == 0:
                smallInfo = countryInfo
                smallCountry = result1[index][0]
            else:
                if countryInfo != 0 and countryInfo < smallInfo:
                    smallInfo = countryInfo
                    smallCountry = result1[index][0]
        except:
            if index == max(range(len(result1))):
                smallInfo = 0
                smallCountry = result1[index][0]
            else:
                continue
    return(smallCountry,smallInfo)


print("------------------------------- Continent Summary -------------------------------")
summary = continentSummary(result1)
print(f"The number of countries in Africa {summary[0]}.")
print(f"There names are: {summary[1]}.")
print("------------------------------- Surface Area -------------------------------")
large_surfaceArea = countryInfo_largest(SurfaceArea)
small_surfaceArea = countryInfo_smallest(SurfaceArea)
print(f"The largest country in {continent} is {large_surfaceArea[0]}.")
print(f"{large_surfaceArea[0]} has surface area of {large_surfaceArea[1]} square kilometer.")
print(f"The smallest country in {continent} is {small_surfaceArea[0]}.")
print(f"{small_surfaceArea[0]} has surface area of {small_surfaceArea[1]} square kilometer.")

print("------------------------------- Independece Year -------------------------------")
large_IndepYear = countryInfo_largest(IndepYear)
small_IndepYear = countryInfo_smallest(IndepYear)
print(f"The youngest country in {continent} is {large_IndepYear[0]}.")
print(f"{large_IndepYear[0]} gained indepedence in year {large_IndepYear[1]}.")
print(f"The oldest country in {continent} is {small_IndepYear[0]}.")
print(f"{small_IndepYear[0]} gained indepedence in year {small_IndepYear[1]}.")

print("------------------------------- Population -------------------------------")
large_Population = countryInfo_largest(Population)
small_Population = countryInfo_smallest(Population)
print(f"The most populated country in {continent} is {large_Population[0]}.")
print(f"{large_Population[0]} has a population of {large_Population[1]} people.")
print(f"The least populated country in {continent} is {small_Population[0]}.")
print(f"{small_Population[0]} has a population of {small_Population[1]} people.")

print("------------------------------- LifeExpectancy -------------------------------")
large_LifeExpectancy = countryInfo_largest(LifeExpectancy)
small_LifeExpectancy = countryInfo_smallest(LifeExpectancy)
print(f"The country with the highest Life Expectancy in {continent} is {large_LifeExpectancy[0]}.")
print(f"{large_LifeExpectancy[0]} has a Life Expectancy of {large_LifeExpectancy[1]} years.")
print(f"The country with the lowest Life Expectancy in {continent} is {small_LifeExpectancy[0]}.")
print(f"{small_LifeExpectancy[0]} has a Life Expectancy of {small_LifeExpectancy[1]} years.")

print("------------------------------- GNP -------------------------------")
large_GNP = countryInfo_largest(GNP)
small_GNP = countryInfo_smallest(GNP)
print(f"The country with the highest Gross National Product in {continent} is {large_GNP[0]}.")
print(f"{large_GNP[0]} has a Gross National Product of {large_GNP[1]}.")
print(f"The country with the lowest Gross National Product in {continent} is {small_GNP[0]}.")
print(f"{small_GNP[0]} has a Gross National Product of {small_GNP[1]}.")

print("******************************* Note *******************************")
print("Where info is 0, there is no information and country name might be incorrect.")


# In[ ]:


print("------------------------------- Continent Info -------------------------------")
continent_lst = ['Africa','Asia','Europe','North America','South America','Oceania']

#Check if country is present in the list
while True:
    #print("-------------------------")
    print("Enter the name of any continent of your choice.")
    name = input("Enter Africa, Asia,Europe,North America, Oceania or South America: ")
    name.lower()
    continent = name.title()
    if continent not in continent_lst:
        print(f"{continent} not found. Try again!")
    else:
        print(f"{continent} found!")
        break

#Query data
query1=(select([country.c.Name,country.c.Continent,language.c.Language,language.c.IsOfficial,language.c.Percentage])        .select_from(country.join(language))        .where(country.c.Continent == continent))
cLang = conn.execute(query1)

cLang1 = []
for row in cLang:
    cLang1.append(row)

#Function for getting information summary about a continent
def continentSummary(cLang1):
    country_lst = []
    for index in range(len(cLang1)):
        if cLang1[index][0] not in country_lst: 
            country_lst.append(cLang1[index][0])
    country_lst.sort()
    return(country_lst)

print("------------------------------- Continent Summary -------------------------------")
countryLst = continentSummary(cLang1)
print(countryLst)


#Check if country is present in the list
while True:
    print("-------------------------")
    name = input("Select a country name from the country list above: ")
    cName = name.title()
    if cName not in countryLst:
        print(f"{cName} not found. Try again!")
    else:
        print(f"{cName} found!")
        break


#cName = 'Spain'
cName_lst = []
offLang = []
hLang = 0
otherCountries = []

for index in range(len(cLang1)):
    #print()
    if cName == cLang1[index][0]:
        cName_lst.append(cLang1[index][2])
        offLang_T = cLang1[index][3]
        try:
            if offLang_T == 'T':
                offLang.append(cLang1[index][2])
        except:
            continue
        perLang = cLang1[index][4]
        try:
            if perLang > hLang:
                hLang = perLang
                mostSpokenLang = cLang1[index][2:]
        except:
            continue
    if mostSpokenLang[0] == cLang1[index][2] and cName != cLang1[index][0]:
        otherCountries.append(cLang1[index][0])


print(f"Languages spoken in {cName} are: {cName_lst}.")
print("--------")
if len(offLang) == 0:
    print(f"{cName} has no official language.")
else:
    print(f"The official language in {cName} is {offLang}.")
print("--------")
print(f"The most spoken language in {cName} is {mostSpokenLang[0]} by {round(mostSpokenLang[2],0)}% of people.")
print("--------")
if len(otherCountries) == 0:
    print(f"{mostSpokenLang[0]} is not spoken in other countries in {continent}.")
else:
    print(f"{mostSpokenLang[0]} is spoken in {otherCountries} in {continent}.")

