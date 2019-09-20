import pandas as pd
import numpy as np
import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('train.csv', sep=',', usecols=['GarageArea', 'SalePrice'])

# Create scatterplot of dataframe before removing Anamolies
sns.lmplot('GarageArea', # Horizontal axis
           'SalePrice', # Vertical axis
           data=df, # Data source
           fit_reg=False, # Don't fix a regression line
           scatter_kws={"marker": "o", # Set marker style
                        "s": 60}) # S marker size

# Set title
plt.title('plot between Garage Area and SalPrice')
plt.xlim(-200,1600)
# Set x-axis label
plt.xlabel('GarageArea')
# Set y-axis label
plt.ylabel('SalePrice')
plt.show()

# Using box plot to identifty the outliers
sns.boxplot(x=df['GarageArea'])

# Removing the Anamolies by directly specifying the limits of the outliers(anamolies are points which are far from group of samples)

train = df
train['GarageArea'] = train[train['GarageArea']>200]
train['GarageArea'] = train[train['GarageArea']<1200]


# Create Scatterplot of the dataframe after removing the anamolies in the data
sns.lmplot('GarageArea', # Horizontal axis
           'SalePrice', # Vertical axis
           data=train, # Data source
           fit_reg=False, # Don't fix a regression line
           scatter_kws={"marker": "o", # Set marker style
                        "s": 80}) # S marker size

# Set title
plt.title('plot between Garage Area and SalPrice')
plt.xlim(-200, 1600)
# Set x-axis label
plt.xlabel('GarageArea')
# Set y-axis label
plt.ylabel('SalePrice')
plt.show()


# Removing the Anamolies using z-score(68% and with in 95%)
# if the data is more than 3 standard deviations away then it is considered as outlier
# if the data is less than -3 standard deviations away then it is considered as outlier
df = pd.read_csv('train.csv', sep=',',usecols=(62,80))
z = np.abs(stats.zscore(df))
threshold = 3
print(np.where(z > 3))
modified_df = df[(z < 3).all(axis=1)]
print(df.shape) #dimensions represents shape
print(modified_df.shape)

# Create Scatterplot of the dataframe after removing the anamolies in the data
sns.lmplot('GarageArea', # Horizontal axis
           'SalePrice', # Vertical axis
           data=modified_df, # Data source
           fit_reg=False, # Don't fix a regression line
           scatter_kws={"marker": "o", # Set marker style
                        "s": 80}) # S marker size

# Set title
plt.title('plot between Garage Area and SalPrice')
plt.xlim(-200, 1600)
# Set x-axis label
plt.xlabel('GarageArea')
# Set y-axis label
plt.ylabel('SalePrice')
plt.show()


# Removing the anamolies using Quantile - removing less than 25% and more than 75% Qunatile
#Q1 = df.quantile(0.25)
#Q3 = df.quantile(0.75)
#IQR = Q3 - Q1
#print(IQR)
#print((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR)))

#modified_df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
#print(modified_df.shape)

# Create Scatterplot of the dataframe after removing the anamolies in the data
#sns.lmplot('GarageArea', # Horizontal axis
  #         'SalePrice', # Vertical axis
 #          data=modified_df, # Data source
   #        fit_reg=False, # Don't fix a regression line
    #       scatter_kws={"marker": "o", # Set marker style
     #                   "s": 80}) # S marker size

# Set title
#plt.title('plot between Garage Area and SalPrice')
#plt.xlim(-200, 1600)
# Set x-axis label
#plt.xlabel('GarageArea')
# Set y-axis label
#plt.ylabel('SalePrice')
#plt.show()