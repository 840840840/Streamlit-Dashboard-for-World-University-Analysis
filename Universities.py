# %%
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
import warnings
warnings.filterwarnings("ignore")


# %%
# import dataset
df = pd.read_csv("top universities.csv")

# %%
df.head(1)

# %%
 #Count of universities per country
country_counts = df['Country'].value_counts()
print(country_counts.head(10))

# %%
# USA Universities
usa_universities = df[df['Country'].str.contains("Usa", case=False)]
print("USA universities:", len(usa_universities))

# %%
# Top 10 ranked universities in USA
top_usa = usa_universities.sort_values(by='Global Rank').head(10)
print(top_usa[['University', 'City', 'Global Rank']])

# %%
# Plot: Top 10 countries with most universities
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.head(10).values, y=country_counts.head(10).index)
plt.title("Top 10 Countries with Most Universities")
plt.xlabel("Number of Universities")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# %%
import streamlit as st
st.set_page_config(page_title="University Dashboard", layout="wide")

st.title("🌍 World University Dashboard")
st.markdown("Built by **Muhammad Usama**")

countries = sorted(df['Country'].unique())
selected_country = st.sidebar.selectbox("🌍 Select a Country", countries)

# Main Dashboard Columns
col1, col2 = st.columns(2)

# Country-wise summary
with col1:
    st.subheader(f"🎯 Universities in {selected_country}")
    country_df = df[df['Country'] == selected_country]
    st.write(f"Total Universities: **{len(country_df)}**")

    top_10_ranked = country_df.sort_values(by="Global Rank").head(10)
    st.markdown("🏆 **Top 10 Ranked Universities**")
    st.table(top_10_ranked[['University', 'City', 'Global Rank']])

# Chart - Top 10 countries with most universities
with col2:
    st.subheader("📊 Top 10 Countries with Most Universities")

    country_counts = df['Country'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis", ax=ax)
    ax.set_xlabel("Number of Universities")
    ax.set_ylabel("Country")
    ax.set_title("Top 10 Countries by University Count")
    st.pyplot(fig)

# Full data table (optional)
st.markdown("🔍 **University Listings in Selected Country**")
st.dataframe(country_df[['University', 'City', 'Global Rank']].sort_values(by='Global Rank'))



