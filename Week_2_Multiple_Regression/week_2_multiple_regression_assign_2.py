import os
import zipfile
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

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
              'price':float, 'bedrooms':float, 'zipcode':str, 
              'long':float, 'sqft_lot15':float, 'sqft_living':float, 
              'floors':str, 'condition':int, 'lat':float, 'date':str, 
              'sqft_basement':int, 'yr_built':int, 'id':str, 'sqft_lot':int, 'view':int}


# Loading sales data, sales training data, and test_data into DataFrames
sales = pd.read_csv('kc_house_data.csv', dtype = dtype_dict)
train_data = pd.read_csv('kc_house_train_data.csv', dtype = dtype_dict)
test_data = pd.read_csv('kc_house_test_data.csv', dtype = dtype_dict)


sales['constant'] = 1.0


# Looking at head of training data DataFrame
print
print sales.head()	












## Multiple features used to perform linear regression
#example_features = ['sqft_living', 'bedrooms', 'bathrooms']
## Dataframe with features used for linear regression
#X_multi_lin_reg = train_data[example_features]
## Dataframe with the price
#y_multi_lin_reg = train_data['price']

## Creating a LinearRegression Object
#example_model = LinearRegression()
## Learning the multiple linear regression model
#example_model.fit(X_multi_lin_reg, y_multi_lin_reg)

## printing the intercept and coefficients
#print
#print example_model.intercept_
#print example_model.coef_

## Putting the intercept and weights from the multiple linear regression into a Series
#example_weight_summary = pd.Series( [example_model.intercept_] + list(example_model.coef_),
#                                  index = ['intercept'] + example_features )
#print
#print example_weight_summary

#example_predictions = example_model.predict(X_multi_lin_reg)
#print
#print example_predictions[0] # should be close to 271789.505878

#def get_residual_sum_of_squares(model, data, outcome):
#    # First get the predictions
#    model_predictions = model.predict(data)

#    # Then compute the residuals/errors
#    residuals = outcome - model_predictions

#    # Then square and add them up
#    RSS = sum(residuals*residuals)

#    return(RSS) 

#print
#print test_data.head()    

#print
#print 'Done!'


