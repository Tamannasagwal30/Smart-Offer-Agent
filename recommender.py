#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


def get_recommendations(user_id, weather, time_of_day, occasion, users_df, offers_df):
    #Get User Tags
    user_tags = users_df[users_df['user_id'] == user_id]['tags'].values[0]

    #Combine all tags from offers for TF-IDF
    offer_tags = offers_df['taste_tags'].fillna('')

    #Create TF-IDF Matrix
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([user_tags] + offer_tags.tolist())

    #Compute Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    #Add similarity scores to offers
    offers_df = offers_df.copy()
    offers_df['taste_score'] = cosine_sim

    #Add Context Score
    def context_match_score(context_str):
        tags = context_str.lower().split(', ')
        score = 0
        if weather.lower() in tags:
            score += 0.3
        if time_of_day.lower() in tags:
            score += 0.3
        if occasion.lower() in tags:
            score += 0.3
        return score
    offers_df['context_score'] = offers_df['context_tags'].apply(context_match_score)

    #Final Score = Taste + Context
    offers_df['final_score'] = offers_df['taste_score'] + offers_df['context_score']

    #Return Top 3 Offers
    top_offers = offers_df.sort_values(by = 'final_score', ascending = False).head(3)
    return top_offers[['offer_title', 'offer_desc', 'final_score']]
               


# In[ ]:




