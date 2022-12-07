# Project2
Repository to develop codes for Project 2 BSC4453 class.

The objective of this assignment is to use a sqlite database. We choose the world.sqlite that contains information about all the countries in this world. We must define at last two functions and have a JOIN using SQLAlchemy.

The Continent language script describes a function to query continent language information. The continent and country name will be verified and returns the country's all spoken language(s), official language(s), most spoken language, and other countries where the most spoken language is spoken on the continent.

The Continent Information script contains a function that provides a summary of continent information entered by the user. The continent name will be verified and returns the country with the smallest and largest surface area, independence year, population size, life expectancy, and gross national income.

The Common Speakers file has a function that queries the countries by language. The user can enter a known language and the script will return the countries where the user can travel.

The Country and City script generates a list of country names with assoicated code, population, and life expectancy from Country table; a list of city names with associated country code and population from City table; and then joins Country and City tables using Country Code from City table and Code from Country table to generate a list of city names with associated population and life expectancy. This is listed in descending order of life expectancy.  

The Life Expentancy and Language script includes a selection of query data of the countries with a life expectancy greater than 80 years old which returns 5 different countries from the "world" database. This table is then joined with the countrylanguage table to include the main language of that country. Then a pandas as pd is done to create a table that organizes this join. 

Hope this can be useful to you,

Please, feel free to contact us regarding this project

Best Regards,

Paul Adunola, Mariana Vianna, Margaret Lilyestrom, and Ellen Garcia 
