import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Find all tables in the DB
conn = sqlite3.connect('factbook.db')
q1 = "SELECT * FROM sqlite_master WHERE type = 'table'"
tables = pd.read_sql_query(q1, conn)
# print(tables)

#Return first 5 rows of facts table
q2 = "SELECT * FROM facts"
rows = pd.read_sql_query(q2, conn)
# print(rows[:5])

#Population Statistics from facts table
q3 = "SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth) FROM facts"
pop_facts = conn.execute(q3).fetchone()
print('Min Population -', pop_facts[0])
print('Max Population -', pop_facts[1])
print('Min Population Growth -', pop_facts[2])
print('Max Population Growth -', pop_facts[3])

#Focus on outliers
q4 = 'SELECT * FROM facts WHERE population == (SELECT MIN(population) FROM facts) OR population == (SELECT MAX(population) FROM facts)'
pop_out = conn.execute(q4).fetchall()
# print(pop_out)

#Histogram excluding MIN/MAX population values
# q5 = 'SELECT population, population_growth, birth_rate, death_rate FROM facts WHERE population != (SELECT MAX(population) FROM facts) OR population != (SELECT MIN(population) FROM facts)'
# fig = plt.figure(figsize=(10,10))
# ax = fig.add_subplot(111)
# pd.read_sql_query(q5, conn).hist(ax=ax)

#Ratio Fun
q6 = 'SELECT name Country, CAST(population as float)/CAST(area_land as float) "Population Density" FROM facts ORDER BY "Population Density" DESC LIMIT 5'
high_den_pop = pd.read_sql_query(q6, conn)
print()
print(high_den_pop)

q7 = 'SELECT name Country, CAST(area_water as float)/CAST(area_land as float) "Water to Land Ratio" FROM facts ORDER BY "Water to Land Ratio" DESC LIMIT 5'
w2lr = pd.read_sql_query(q7, conn)
print()
print(w2lr)

q8 = 'SELECT name Country, area_water Water, area_land Land FROM facts WHERE Water > Land'
more_water = pd.read_sql_query(q8, conn)
print()
print('Countries with more water than land')
print(more_water)
