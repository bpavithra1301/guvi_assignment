#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pymongo


# In[42]:


get_ipython().system('pip install pymongo')


# In[43]:


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


# In[44]:


mydb = client["teldir"]


# In[48]:


info = mydb.teldirinfo


# In[53]:


record ={  
    "name" : "sheela" ,
    "phone" : "908726281",
    "city" : "chennai",
    "age"  : 34 ,
    "sex"  :"female"
}  


# In[54]:


info.insert_one(record)


# In[55]:


for i in info.find() :
    print(i)


# In[58]:


records = [
      {
        "name" : "mala" ,
        "phone" :"879018272",
        "city" :"hyderabad",
        "age" : 45,
        "sex"  : "female"
    }, 
    {
        "name" : "kumar" ,
        "phone" : "8602837521",
        "city" : "mumbai",
        "age" : 32,
        "sex" :"male"
    },
    {
        "name" : "rahul",
        "phone" : "87652910123",
        "city" : "chennai",
        "age" : 25, 
        "sex" : "male"
    
    },
    {
        "name" : "pooja" ,
        "phone" : "854920134",
        "city" : "delhi" ,
        "age" : 28,
        "sex"  : "female"
      },
    {
        "name" : "geetha",
        "phone" : "7899625123",
        "city" : "hyderabad" ,
        "age"  : 18,
        "sex" : "female"
    },
    {
        "name" : "sai",
        "phone" : "902635272",
        "city" : "delhi",
        "age" : 29, 
        "sex" : "male"
    }
  
    ]


# In[59]:


info.insert_many(records)


# In[60]:


for i in info.find() :
    print(i)


# In[84]:


#updating the record using update_one :

info.update_one({"city" : "delhi"}, {"$set" : {"age" : 25 , 'name' : 'tiru'}})


# In[86]:


#output after updating record

for i in info.find() :
    print(i)


# In[89]:


#using delete_one() :

info.delete_one({"city" : "mumbai"}) 


# In[90]:


#output after deleting record 

for i in info.find() : 
    print(i)


# In[ ]:




