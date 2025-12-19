import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set Page Config
st.set_page_config(page_title="Chiang Mai Live 2025", page_icon="🐘", layout="wide")

# --- DATA ENGINE ---
# This contains all the event info from the previous versions
events_master = [
    {
        "Name": "Charming Chiang Mai Flower Fest",
        "Category": "Festival",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief": "Theme: 'Gold of Lanna'. Features massive light sculptures, musical fountain shows (7, 8, 9, 10 PM), and a glowing 'Tree of Life'. Free entry.",
        "Location": "Chiang Mai PAO Park", "lat": 18.8288, "lon": 98.9772,
        "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name": "Ping Fai Festival (Santa Village)",
        "Category": "Market",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief": "A winter market where you can roast marshmallows over open fires, shop at 50+ craft vendors, and see the giant Christmas tree.",
        "Location": "One Nimman", "lat": 18.7999, "lon": 98.9678,
        "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name": "Jing Jai Muan Muan Market",
        "Category": "Market",
        "Start": datetime(2025, 12, 18), "End": datetime(2025, 12, 21),
        "Brief": "Annual Open House with 600+ vendors. Best for high-quality Lanna crafts, organic coffee, and eco-friendly art.",
        "Location": "Jing Jai Central", "lat": 18.8073, "lon": 98.9955,
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name": "Flora Festival 2025",
        "Category": "Festival",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief": "Theme: 'Bloom for the Future'. Highlights include the Orchid House, a 360-degree Sky Walk, and millions of highland winter flowers.",
        "Location": "Royal Park Rajapruek", "lat": 18.7516, "lon": 98.9247,
        "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name": "Chiang Mai Marathon Expo",
        "Category": "Sports",
        "Start": datetime(2025, 12, 19), "End": datetime(2025, 12, 20),
        "Brief": "Race pack collection for the marathon. Lively area with sports gear booths and local food near the gate.",
        "Location": "Tha Phae Gate", "lat": 18.7877, "lon": 98.9933,
        "Link": "https://www.chiangmaimarathon.com/"
    }
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🗓️ Event Navigator")
selected_date = st.sidebar.date_input("Pick a Date", datetime(2025, 12, 19))
view_mode = st.sidebar.radio("View Mode", ["Single Day", "Full Week"])

# Determine date range for filtering
d_start = datetime.combine(selected_date, datetime.min.time())
d_end = d_start if view_mode == "Single Day" else d_start + timedelta(days=6)

# Filter Logic: Show events that are active during the chosen range
filtered_events = [e for e in events_master if (e["Start"] <= d_end and e["End"] >= d_start)]

# --- MAIN UI ---
st.title("🐘 Chiang Mai Event Explorer")
date_label = d_start.strftime('%B %d, %Y') if view_mode == "Single Day" else f"{d_start.strftime('%b %d')} - {d_end.strftime('%b %d, %Y')}"
st.subheader(f"Status for: {date_label}")

# Map Section
if filtered_events:
    st.markdown("### 🗺️ Live Event Map")
    map_df = pd.DataFrame(filtered_events)
    st.map(map_df)
else:
    st.info("No major events listed for this range. Try picking a date closer to the weekend!")

# Details Section
st.markdown("### 📍 Event Details & Directions")
if filtered_events:
    for ev in filtered_events:
        with st.expander(f"📌 {ev['Name']} ({ev['Location']})"):
            st.write(f"**Description:** {ev['Brief']}")
            st.write(f"**Category:** {ev['Category']}")
            st.write(f"**Dates:** {ev['Start'].strftime('%b %d')} to {ev['End'].strftime('%b %d, %Y')}")
            
            # Action Buttons
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("🌐 Official Website", ev['Link'])
            with c2:
                # Direct Google Maps link
                gmaps = f"https://www.google.com/maps?q={ev['lat']},{ev['lon']}"
                st.link_button("📍 Open in Google Maps", gmaps)
else:
    st.write("No details to show.")

st.divider()
st.info("🚦 **Tip:** Traffic is heaviest in Chiang Mai between 4:30 PM and 6:30 PM, especially near the Old City and Nimman.")