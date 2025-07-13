# Smart Offer Agent – Contextual Recommender

A mini proof-of-concept inspired by Crayon Data’s **maya.ai**, showcasing how user preferences and contextual intelligence can drive hyper-personalized offer recommendations.

---

# Live Demo

Click here to launch the app - (https://tamanna-smart-offer.streamlit.app)  

---

# Overview

This application mimics the personalization logic used in platforms like **maya.ai**, combining:

**Taste profiling** via TF-IDF and cosine similarity
**Real-time context** (weather, time, occasion)
**Hybrid scoring logic** to deliver top 3 most relevant offers

---

# Sample Use Case

- **User 002** is tagged with preferences like *coffee, books, solo travel*
- Current context: *Rainy morning + Weekend*
- Output: 
  > 1. 20% off Starbucks — Valid on morning coffee purchases  
  > 2. ₹500 off Goibibo — Use on weekend travel bookings  
  > 3. 30% off Crossword — Perfect for book lovers on rainy days

Each recommendation comes with a **breakdown of taste and context match scores**.

---

# How It Works

## Recommendation Flow

1. **User Tags** → Match with offer tags using TF-IDF
2. **Context Tags** → Matched against weather, time of day, and occasion
3. **Final Score** = Taste score + Context score (adjustable)

---


