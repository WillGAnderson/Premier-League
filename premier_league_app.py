import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# API setup
API_KEY = 'da5a30aa255d448b8da62a7f9b13169d'
url = 'https://api.football-data.org/v4/competitions/PL/seasons'
headers = {'X-Auth-Token': API_KEY}

# Fetch data
response = requests.get(url, headers=headers)
data = response.json()

# Process season data
seasons_data = []
for season in data['seasons']:
    year = season['year']
    if 2020 <= year <= 2025:
        start_date = datetime.strptime(season['startDate'], "%Y-%m-%d")
        end_date = datetime.strptime(season['endDate'], "%Y-%m-%d")
        duration = (end_date - start_date).days
        seasons_data.append({
            "Season": f"{year}-{year+1}",
            "Start Date": start_date,
            "End Date": end_date,
            "Days": duration
        })

# Convert to DataFrame
df = pd.DataFrame(seasons_data)

# Streamlit UI
st.set_page_config(page_title="Premier League Explorer", layout="centered")
st.title("📅 Premier League Season Explorer (2020–2025)")

# Display data
st.subheader("Season Data Table")
st.dataframe(df)

# Plot chart
st.subheader("📊 Season Lengths (Days)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Season"], df["Days"], color="skyblue")
ax.set_ylabel("Days")
ax.set_xlabel("Season")
ax.set_title("Premier League Season Lengths")
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
st.pyplot(fig)
