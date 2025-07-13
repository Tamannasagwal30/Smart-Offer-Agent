#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from recommender import get_recommendations
import os


# In[2]:


#Load Data
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

users = pd.read_csv(os.path.join(DATA_DIR, "users.csv"))
offers = pd.read_csv(os.path.join(DATA_DIR, "offers.csv"))
context = pd.read_csv(os.path.join(DATA_DIR, "context.csv"))

st.set_page_config(page_title = "SMART OFFER AGENT", layout = "centered")
st.title("SMART OFFER AGENT - PERSONALIZED RECOMMENDER")
st.markdown("""
Welcome to the **Smart Offer Agent** - a proof of concept inspired by Crayon Data's *maya.ai* platform.

This mini-engine recommends top 3 personalized offers based on a user's taste profile and real-time context like weather, rain and occasion.

It blends:
\n 1.Taste profiling using TF-IDF

\n 2.Contextual filtering

\n 3.Real-time scoring

Ready to show how personalization drives engagement? Let’s go!
""")

#User Selector
user_id = st.selectbox("Select User", users['user_id'])
user_name = users[users['user_id'] == user_id]['name'].values[0]
st.markdown(f"Hello, {user_name}")

#Context Inputs
weather = st.selectbox("Current Weather", context['weather'].unique())
time_of_day = st.selectbox("Time of Day", context['time_of_day'].unique())
occasion = st.selectbox("Occasion", context['occasion'].unique())

#Button
if st.button("Get Smart Recommendations"):
    top_offers = get_recommendations(user_id, weather, time_of_day, occasion, users_df= users, offers_df = offers)
    st.subheader("Top Personalized offers for you")
    for i, row in top_offers.iterrows():
        st.markdown(f"""
        ---  
        **{row['offer_title']}**  
        {row['offer_desc']}  
        **Final Score:** `{row['final_score']:.2f}`  
        _Why this offer?_  
        - Taste Match Score: `{row['taste_score']:.2f}`  
        - Context Match Score: `{row['context_score']:.2f}`
        """)


# In[ ]:




