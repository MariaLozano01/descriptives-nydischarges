import pandas as pd
import numpy as np
import tableone as t1
import researchpy as rp
import tabulate 
from tableone import TableOne

data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
data
data.columns
data.dtypes

data_columns = ['gender','race','ethnicity','facility_id']
data_categorical = ['gender','race','ethnicity']
data_groupby = ['facility_id']

data1 = TableOne(data, columns=data_columns,categorical=data_categorical, groupby=data_groupby, pval= False)
data1

print(data1.tabulate(tablefmt = "fancy_grid"))

data1.to_csv('tables/table1.csv') #to save the table as a csv file 


