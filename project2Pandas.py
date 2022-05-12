#Project 2 
#Here I used pandas to load my NBA draft data once again
# so I could answer my other questions pertaining to this data
# while also using it as an example for project 2.
# Our first project inpired me to expore this data set further.
# I also use matplotlib to plot my data onto some graphs

# Hypothesis: I belive that there might be a drop off
# in rebounds per game and an increase in FT%
# as the game favours guards now over big men.

#Conclusion: Inclusive. There is no real trend to be seen in the 
# rebounds per game as there are spikes throughout the dataset.
# The FT% seems to have increased over time and this could be
# due to the demand for better shooters, regardless of position.


import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Get the data
df = pd.read_csv('draft-data-20-years.csv', index_col=0)


maxRpg = df['RPG'].max()
mostRpgQuery = df[df['RPG']==maxRpg]

print("The drafted player(s) who had the most RPG is ")
print(mostRpgQuery)

maxR = df['TOTTRB'].max()
mostRQuery = df[df['TOTTRB']==maxR]

print("The drafted player(s) who had the most Rebounds in their career is ")
print(mostRQuery)

maxFT = df['FT%'].max()
mostFTQuery = df[df['FT%']==maxFT]


print("The drafted player(s) who had the highest FT% is ")
print(mostFTQuery)
##

ftYear = df.groupby(['DraftYear'])['FT%'].mean()
print(ftYear)

chart1 = ftYear.plot(x='DraftYear',y='FT%',title='FT% by Draft Year')
plt.legend()
plt.show()

rYear = df.groupby(['DraftYear'])['RPG'].mean()
print(rYear)

chart2 = rYear.plot(x='DraftYear',y='RPG',title='Rebounds per game')
plt.legend()
plt.show()






