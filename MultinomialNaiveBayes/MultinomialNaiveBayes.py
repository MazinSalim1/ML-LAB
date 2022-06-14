#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sklearn.datasets import fetch_20newsgroups
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
news_train = fetch_20newsgroups(subset='train',categories=categories)
news_test = fetch_20newsgroups(subset='test',categories=categories)


# In[15]:


print(news_train.keys())
print(news_train['target_names'])


# In[16]:


from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
X_train_tf=count_vect.fit_transform(news_train.data)
print(X_train_tf)
X_train_tf.shape


# In[17]:


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer=TfidfTransformer()
X_train_tfidf=tfidf_transformer.fit_transform(X_train_tf)
X_train_tfidf.shape


# In[18]:


from sklearn.naive_bayes import MultinomialNB
clf= MultinomialNB().fit(X_train_tfidf, news_train.target)


# In[19]:


X_test_tf=count_vect.transform(news_test.data)
X_test_tfidf=tfidf_transformer.transform(X_test_tf)
predicted=clf.predict(X_test_tfidf)
predicted


# In[20]:


from sklearn import metrics 
from sklearn.metrics import accuracy_score
print("Accuracy",accuracy_score(news_test.target,predicted))
print(metrics.confusion_matrix(news_test.target,predicted))


# In[ ]:




