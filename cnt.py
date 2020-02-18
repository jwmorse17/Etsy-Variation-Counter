
# File: cnt.py
# Using Python 3.4.2

# This program combines .csv files into a single frame, then
# takes some data from a specific column, cleans it up, and
# prints the number off occurences of an item in that column. 

# data is in the origional format: 
# Ring size:9.25 US,Width:6.5mm

# This function alters the string such that the data is in 
# the new format of:
# 9.25

# TODO:
# Data has some variability. Can be in the form 10.5 or 10 1/2. 
# create a function to clean that up such that all data is in the form 10.5


import pandas as pd
import glob

path = r'/home/parallels/Documents/prog/etsy/ringSizeCount/data' #location where .csv are stored
allFiles = glob.glob(path + "/*.csv")

list = []

for filename in allFiles:
	df = pd.read_csv(filename, index_col=None, header=0)
	list.append(df)

frame = pd.concat(list, axis=0, ignore_index=True)


frame['var_cl'] = frame['Variations'].str.split('US').str[0].str.split(':').str[1]
frame['clean'] = frame['var_cl'].str.replace(' 1/4', '.25').str.replace(' 1/2', '.5').str.replace( ' 3/4', '.75')

print(frame['clean'].value_counts())
