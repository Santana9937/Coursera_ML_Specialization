import os
import zipfile
import numpy as np
import pandas as pd

## Unzipping files with data

# Put files in current direction into a list
files_list = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filenames of unzipped files
unzip_files = ['kc_house_train_data.csv', 
				'kc_house_test_data.csv', 'kc_house_data.csv']

# If upzipped file not in files_list, unzip the file
for filename in unzip_files:
	if filename not in files_list:
		zip_file = filename + '.zip'
		zip = zipfile.ZipFile(zip_file)
		zip.extractall()
		zip.close


## Loading sales data, sales training data, and test_data into DataFrames

# Dictionary with the correct dtypes for the DataFrame columns
dtype_dict = {'bathrooms':float, 'waterfront':int, 'sqft_above':int, 
			  'sqft_living15':float, 'grade':int, 'yr_renovated':int, 
			  'price':float, 'bedrooms':float, 'zipcode':str, 'long':float, 
			  'sqft_lot15':float, 'sqft_living':float, 'floors':str, 
			  'condition':int, 'lat':float, 'date':str, 'sqft_basement':int, 
			  'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int}


sales = pd.read_csv('kc_house_data.csv', dtype = dtype_dict)
train_data = pd.read_csv('kc_house_train_data.csv', dtype = dtype_dict)
test_data = pd.read_csv('kc_house_test_data.csv', dtype = dtype_dict)

print
print 'Done!'


