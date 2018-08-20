
# coding: utf-8

# In[2]:

import json
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor


model_trained = False
knn = KNeighborsRegressor(n_neighbors=7, weights='distance')

# In[3]:

def train_model():

    consumo_energia = pd.read_csv('Consumo.csv')


    # In[4]:


    x = np.array([consumo_energia['weekDay']]).reshape(-1, 1)
    y = np.array([consumo_energia['consumption']]).reshape(-1, 1)
  

    
    knn.fit(x, y)
    
    model_trained = True


def predict_one_day(week_day):
    week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
    

    result  = knn.predict(np.array(week_day).reshape(-1, 1))
    result.tolist()
    data =  {week_days[week_day] : result}
    return data

def predict_week():
    week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
    
    int_week_days = np.arange(1, 8).reshape(-1, 1)
    result = knn.predict(int_week_days).tolist()

    data = {}

    for i in range(7):
        data[week_days[i]] = result[i]
    return data


""" # In[9]:


knn = KNeighborsRegressor(n_neighbors=1, weights='distance')
knn_1 = knn.fit(x, y)
print(knn)

# In[14]:

knn = KNeighborsRegressor(n_neighbors=5, weights='distance')
knn_5 = knn.fit(x, y)
print(knn)


# In[29]:

knn = KNeighborsRegressor(n_neighbors=7, weights='uniform')
knn_7_uniform = knn.fit(x, y)


# In[15]:

# In[16]:

knn = KNeighborsRegressor(n_neighbors=15, weights='distance')
knn_15 = knn.fit(x, y)
print(knn) """


# In[18]:


""" week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
int_week_days = np.arange(1, 8).reshape(-1, 1)

result = knn_5.predict(int_week_days)
print(result)

for i in range(7):
    print(f'{week_days[i]} : {result[i]}')


# In[19]:


plt.scatter(x, y, c='k', label='data')
plt.plot(int_week_days, result, c='g', label='prediction')
plt.axis('tight')
plt.legend()
plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (5,
                                                            'distance'))

plt.show()


# In[35]:


week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
int_week_days = np.arange(1, 8).reshape(-1, 1)

result_7 = knn_7.predict(int_week_days)
print(result)

for i in range(7):
    print(f'{week_days[i]} : {result_7[i]}')


# In[32]:


result_uniform = knn_7_uniform.predict(int_week_days)

for i in range(7):
    print(f'{week_days[i]} : {result_uniform[i]}')


# In[49]:


#plt.Figure(figsize = (140,140))
plt.scatter(x, y, c='k', label='data')
plt.plot(int_week_days, result_7, c='g', label='prediction7')


plt.plot(int_week_days, result, c='red', label='prediction5')
plt.plot(int_week_days, result_uniform, c='blue', label='prediction5_uniform')

plt.axis('tight')
plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (7,
                                                            'distance'))


plt.legend()


plt.show()


# In[28]:


week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
int_week_days = np.arange(1, 8).reshape(-1, 1)

result = knn_15.predict(int_week_days)
print(result)

for i in range(7):
    print(f'{week_days[i]} : {result[i]}') """
