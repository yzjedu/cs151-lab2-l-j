# Programmers:  Leif and Jordi
# Course:  CS151, Professor Zelalem Yalew
# Due Date: September 26, 12:15
# Programming Assignment:  Lab 02
# Problem Statement:  Create a machine that takes the birth, death, and immigration rates of a country, as well as their current population and desired years into the future, and calculate the expected population change in addition to the new population in the time frame
# Data In:  Birth, death, and immigration rates expressed via space between events in seconds, current population, and desired years to calculate
# Data Out:  The calculated change in population, the calculated total end population, and an increase or decrease statement
# Credits:  In-class instruction

# import math module for a later print statement
import math
year_in_seconds = 31536000

# requests birth, death, and immigration rates + current population + desired years from user
birth_rate = int(input("How many seconds between births in your country? "))
death_rate = int(input("How many seconds between deaths in your country? "))
immigration_rate = int(input("How many seconds between immigrations in your country? "))
current_population =int(input("What is the current population in your country? "))
years_in_future = int(input("How many years in the future do you want to calculate? "))

# calculates the population change given the constant and user input values and rounds down to a whole number without typecasting as an integer
population_change = ((year_in_seconds/birth_rate + year_in_seconds/immigration_rate - year_in_seconds/death_rate) * years_in_future) // 1

# calculates the expected population using simple addition
future_population = current_population + population_change

# prints the current population and calculated future population to the user
print('In', years_in_future,"year(s), your country's population will go from", current_population, "to", future_population,)

# determines whether it is an increase or decrease, then prints a statement containing the population change accordingly
if population_change > 0:
    print('The population will increase by', population_change,'people')
else:
    print('The population will decrease by', math.fabs(population_change),'people')