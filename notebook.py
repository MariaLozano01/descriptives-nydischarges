import pandas as pd
import numpy as np   
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
data
data.shape
data.dtypes

##Splits a dataframe on values of categorical variables
groupby_gender = data.groupby('gender')
for gender, value in groupby_gender['facility_id']:
    print((gender,value.mean())) ##prints the mean of value numbers for each gender based on their facility_id info

groupby_gender = data.groupby('gender')
for gender, value in groupby_gender['facility_id']:
    print((gender,value.count())) #provides a count of the facility_id values based on gender while ignoring the NaN values within it 

data.columns

data['gender'].value_counts(dropna= False)#to see how many values are there present for each gender in the dataset 
##F 621
##M 379

import pandas.plotting as plotting
graph = pd.plotting.scatter_matrix(data[['total_costs','facility_id']])
graph

import matplotlib.pyplot as plt
plt.show()
##to make a scatter plot^

#TO CREATE A SCATTER PLOT
import pandas as pd
data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
data

x= data['total_costs']
y=data['facility_id']

import matplotlib.pyplot as plt
graph2 =plt.scatter(x,y)
plt.xlabel('total_costs') #to rename x-axis on our scatte plot
plt.ylabel('facility_id') ##to rename y-axis on our scatter plot
plt.show()

























