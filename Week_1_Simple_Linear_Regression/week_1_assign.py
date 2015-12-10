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


def simple_linear_regression(input_feature, output):

	# Computing sums needed to calculate slope and intercept
	xi_sum = sum(input_feature)
	yi_sum = sum(output)
	yi_xi_sum = sum(input_feature*output)
	xi_squared_sum = sum(input_feature*input_feature)
	N = float(len(input_feature))

	# Values for slope and intercept
	slope = (yi_xi_sum - (xi_sum*yi_sum)/N)/(xi_squared_sum - (xi_sum*xi_sum)/N)
	intercept = yi_sum/N - slope*(xi_sum/N)

	return (intercept, slope)

test_feature = np.arange(5)
test_output = 1.0 + 1.0*np.arange(5)
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print
print "Intercept: " + str(test_intercept)
print "Slope: " + str(test_slope)	

sqft_intercept, sqft_slope = simple_linear_regression(train_data['sqft_living'].values, train_data['price'].values)
print
print "Intercept: " + str(sqft_intercept)
print "Slope: " + str(sqft_slope)

def get_regression_predictions(input_feature, intercept, slope):
    
    predicted_values = intercept + slope*input_feature

    return predicted_values
    
my_house_sqft = 2650
estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
print
print "The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqft, estimated_price)


print
print 'Done!'


