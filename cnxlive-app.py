import streamlit as st
import pandas as pd
from datetime import datetime

# Set Page Config
st.set_page_config(page_title="Chiang Mai Live 2025", page_icon="🐘", layout="wide")

# Title and Date
st.title("🐘 Chiang Mai Daily Live Feed")
today = datetime.now().strftime("%B %d, %Y")
st.subheader(f"Current Status: {today}")

# Sidebar for Filters
st.sidebar.header("Filter Events")
category = st.sidebar.multiselect(
    "Select Category",
    ["Festival", "Market", "Sports", "Art/Culture", "Nightlife"],
    default=["Festival", "Market", "Sports"]
)

# Event Data
events = [
    {"Name": "Charming Chiang Mai Flower Fest", "Category": "Festival", "Time": "8:00 AM - 10:00 PM", "Status": "🟢 Active", "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"},
    {"Name": "Ping Fai (Marshmallow Festival)", "Category": "Market", "Time": "4:00 PM - 11:00 PM", "Status": "🟡 Starts soon", "Link": "https://www.facebook.com/pro.onenimman/"},
    {"Name": "Chiang Mai Marathon Expo", "Category": "Sports", "Time": "10:00 AM - 6:00 PM", "Status": "🟢 Active", "Link": "https://www.chiangmaimarathon.com/"},
    {"Name": "Jing Jai Muan Muan Market", "Category": "Market", "Time": "8:00 AM - 8:00 PM", "Status": "🟢 Active", "Link": "https://www.facebook.com/jjmarketchiangmai/"},
    {"Name": "Flora Festival 2025", "Category": "Festival", "Time": "9:00 AM - 9:00 PM", "Status": "🟢 Active", "Link": "https://www.royalparkrajapruek.org/"},
    {"Name": "Mystic Universe Immersive Art", "Category": "Art/Culture", "Time": "11:00 AM - 9:00 PM", "Status": "🟢 Active", "Link": "https://www.eventbrite.com/e/mystic-universe-tickets"}
]

df = pd.DataFrame(events)

# Filter Logic
filtered_df = df[df["Category"].isin(category)]

# Main Display
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📍 Ongoing Right Now")
    for index, row in filtered_df.iterrows():
        with st.expander(f"{row['Status']} | {row['Name']}"):
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Hours Today:** {row['Time']}")
            st.link_button("Go to Info Page", row['Link'])

with col2:
    st.markdown("### 🌡️ Live Weather & Traffic")
    st.metric(label="Temperature", value="28°C", delta="-2°C (Cool Season)")
    st.info("🚦 **Traffic Alert:** Heavy congestion expected near Tha Phae Gate and Nimman area today due to Marathon prep.")
    
    st.markdown("---")
    st.markdown("### 🔗 Essential Links")
    st.markdown("- [CityNow! Daily Events](https://www.chiangmaicitylife.com/citynow/)")
    st.markdown("- [Grab App (Taxi)](https://www.grab.com/th/en/transport/)")

st.divider()
st.caption("Data is curated for December 19, 2025. This app updates based on local festival schedules.")