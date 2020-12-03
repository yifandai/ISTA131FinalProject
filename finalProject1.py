# import required packages #
import csv
import numpy as np
import pandas as pd
import ggplot as gp
import seaborn as sns
import matplotlib.pyplot as plt


# read data from csv file #
rider_data = pd.read_csv('/Users/whyit/Desktop/ISTA131HW/131final/data.csv')


# look at the data #
print(rider_data.head(5))


# clean the data a little bit #
print(rider_data.dropna(how='any'))
rider_data_clean = rider_data.dropna(how='any')


# look at the distribution of gender based on usertype #
rider_data_melt = pd.melt(rider_data_clean,id_vars='gender')
rider_data_melt = rider_data_melt[rider_data_melt['variable'] == 'usertype']
print(rider_data_melt)
print(rider_data_melt.value_counts())
rider_data_melt.value_counts().plot(kind='bar')
plt.ylabel("Count", labelpad=14)
plt.title("Count of genders and usertype")
plt.show()
