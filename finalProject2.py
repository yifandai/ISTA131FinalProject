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


# look at the distribution of age based on usertype #
# add a new column age #
rider_data_clean['thisyear'] = rider_data_clean.apply(lambda x: 2018, axis=1)
rider_data_clean['age'] = rider_data_clean['thisyear'] - rider_data_clean['birthyear']
print(rider_data_clean)
rider_data_melt_2 = pd.melt(rider_data_clean,id_vars='age')
rider_data_melt_2 = rider_data_melt_2[rider_data_melt_2['variable'] == 'usertype']
print(rider_data_melt_2)
print(rider_data_melt_2.value_counts())
print(rider_data_melt_2.value_counts().plot.hist)


