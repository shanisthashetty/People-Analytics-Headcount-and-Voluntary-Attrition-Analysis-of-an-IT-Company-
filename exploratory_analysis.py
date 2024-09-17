

# employee attrition analysis and retention

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

cols=['Age', 'Attrition','Education', 'Gender','Department','JobSatisfaction','EnvironmentSatisfaction', 
      'WorkLifeBalance', 'MonthlyIncome','YearsSinceLastPromotion',
      'YearsAtCompany', 'YearsInCurrentRole','JobSatisfaction','YearsAtCompany',
      'OverTime'
      ]

edf=pd.read_csv('C:/UE2023W/DA/project/employee_hr_data.csv')
print(edf.head())


edf=edf[cols]

# check shape of the dataset
edf.shape


edf.info()

# check if any column has null data values
checknulls=edf.isnull().any().sum()
print(checknulls)


checknulls=edf.isnull().sum()
print(checknulls)

checkna=edf.isna().any().sum()
print(checkna)


dup=edf.duplicated().sum()

print(dup)

# no duplicates found




# Numeric means
print(edf. mean(numeric_only=True))

print(edf. median(numeric_only=True))



# change attrition field from text yes/no to categorical 1/0

edf['Attrition']=edf['Attrition'].apply(lambda x:1 if x=='Yes' else 0)

# change overtime field from text yes/no to categorical 1/0

edf['OverTime']=edf['OverTime'].apply(lambda x:1 if x=='Yes' else 0)


cols=['Age', 'Education', 'JobSatisfaction','EnvironmentSatisfaction', 
      'WorkLifeBalance', 'MonthlyIncome','YearsSinceLastPromotion',
      'YearsAtCompany', 'YearsInCurrentRole', 'Attrition','OverTime'
      ]

nedf=edf[cols]




correlations = nedf.corr()
f, ax = plt.subplots(figsize = (20, 20))
sns.heatmap(nedf.corr(), annot=True)
plt.show()



nedf.hist(bins=30, figsize=(20,20), color='g')
plt.show()


sns.boxplot(x='YearsAtCompany',data=edf)
plt.show()

sns.boxplot(data=nedf)
plt.show()


