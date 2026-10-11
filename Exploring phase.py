#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


loan_app = pd.read_csv(r"D:\البومي\EXCEL\Loan Risk Analysis\loan_applications.csv")
borrower_info = pd.read_csv(r"D:\البومي\EXCEL\Loan Risk Analysis\borrower_profiles.csv")


# In[4]:


loan_app.info()


# In[5]:


borrower_info.info()


# In[6]:


loan_app.head(10)


# In[7]:


loan_app['application_date'] = pd.to_datetime(loan_app['application_date'])


# In[8]:


loan_app.info()


# In[9]:


loan_app.head(50)


# In[10]:


borrower_info.head(50)


# In[11]:


Fact_table = pd.merge(loan_app, borrower_info, on='borrower_id', how='inner')


# In[12]:


Fact_table.head(10)


# In[13]:


Fact_table.describe()


# In[14]:


Fact_table.to_csv('D:\البومي\EXCEL\Loan Risk Analysis\Fact_table_clean.csv', index=False)


# In[24]:


# 1. Add your buckets and groups (your code)
bins_cs = [300, 579, 669, 739, 799, 850]
labels_cs = ['Poor', 'Fair', 'Good', 'Very Good', 'Exceptional']
Fact_table['credit_score_bucket'] = pd.cut(
    Fact_table['credit_score'], bins=bins_cs, labels=labels_cs
)

bins_dti = [-float('inf'), 35, 50, 75, float('inf')]
labels_dti = ['Low (<=35%)', 'Manageable (36-50%)', 'High (51-75%)', 'Critical (>75%)']
Fact_table['dti_bucket'] = pd.cut(
    Fact_table['dti_ratio'], bins=bins_dti, labels=labels_dti
)


def categorize_employment(status):
  if status in ['Full-Time', 'Part-Time', 'Contract']:
    return 'Employed'
  elif status == 'Self-Employed':
    return 'Self-Employed'
  elif status == 'Retired':
    return 'Retired'
  else:
    return 'Other'


Fact_table['employment_group'] = Fact_table['employment_status'].apply(
    categorize_employment
)


def categorize_purpose(purpose):
  consumer_personal = ['Vacation', 'Medical Expenses', 'Wedding', 'Moving']
  debt_assets = ['Debt Consolidation', 'Major Purchase', 'Auto Loan']
  investment_growth = ['Home Improvement', 'Business Loan', 'Education']

  if purpose in consumer_personal:
    return 'Consumer & Personal'
  elif purpose in debt_assets:
    return 'Debt & Assets'
  elif purpose in investment_growth:
    return 'Investment & Growth'
  else:
    return 'Other'


Fact_table['loan_purpose_group'] = Fact_table['loan_purpose'].apply(
    categorize_purpose
)


# In[25]:


Fact_table['credit_score_bucket_code'] = Fact_table[
    'credit_score_bucket'
].cat.codes
Fact_table['dti_bucket_code'] = Fact_table['dti_bucket'].cat.codes

# For text-based groups, use pd.get_dummies() or factorize
Fact_table['employment_group_code'] = pd.factorize(
    Fact_table['employment_group']
)[0]
Fact_table['loan_purpose_group_code'] = pd.factorize(
    Fact_table['loan_purpose_group']
)[0]


# In[26]:


Fact_table.corr()


# In[27]:


numeric_cols = Fact_table.select_dtypes(include=['number'])
corr_matrix = numeric_cols.corr()

# 2. Create the figure and axis
plt.figure(figsize=(10, 8))

# 3. Plot the heatmap using imshow
cax = plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

# 4. Add a color bar to show scale
plt.colorbar(cax)

# 5. Add labels, ticks, and title
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title('Correlation Heatmap of Numerical Features')

# 6. Display the plot
plt.tight_layout()
plt.show()


# In[28]:


# 1. Select numeric columns and compute the correlation matrix
numeric_cols = Fact_table.select_dtypes(include=['number'])
corr_matrix = numeric_cols.corr()

# 2. Create the figure and axis
plt.figure(figsize=(10, 8))

# 3. Plot the heatmap using imshow
cax = plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

# 4. Add a color bar
plt.colorbar(cax)

# 5. Add labels and ticks
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title('Correlation Heatmap with Values')

# 6. Loop over data dimensions and create text annotations (labels)
for i in range(len(corr_matrix.columns)):
  for j in range(len(corr_matrix.columns)):
    value = corr_matrix.iloc[i, j]
    # Choose text color based on background intensity for readability
    text_color = 'white' if abs(value) > 0.5 else 'black'
    plt.text(
        j,
        i,
        f'{value:.2f}',
        ha='center',
        va='center',
        color=text_color,
        fontsize=8,
    )

# 7. Display the plot
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




