import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set Page Config
st.set_page_config(page_title="Chiang Mai Live Dashboard", page_icon="🐘", layout="wide")

# --- DATA ENGINE ---
# We define events with start/end dates to make the "Calendar" functional.
events_master = [
    {
        "Name": "Charming Chiang Mai Flower Fest",
        "Category": "Festival",
        "Start": datetime(2025, 11, 28),
        "End": datetime(2026, 1, 5),
        "Brief": "Theme: 'Gold of Lanna'. Massive light sculptures and musical fountain shows (7PM-10PM).",
        "Location": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772,
        "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name": "Ping Fai Festival (Santa Village)",
        "Category": "Market",
        "Start": datetime(2025, 12, 13),
        "End": datetime(2025, 12, 25),
        "Brief": "Toast marshmallows over open fires, shop at 50+ craft vendors in Nimman.",
        "Location": "One Nimman",
        "lat": 18.7999, "lon": 98.9678,
        "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name": "Flora Festival 2025",
        "Category": "Festival",
        "Start": datetime(2025, 11, 1),
        "End": datetime(2026, 2, 28),
        "Brief": "Millions of highland blooms and a 360-degree Sky Walk viewpoint.",
        "Location": "Royal Park Rajapruek",
        "lat": 18.7516, "lon": 98.9247,
        "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name": "Chiang Mai CAD Countdown 2026",
        "Category": "Festival",
        "Start": datetime(2025, 12, 29),
        "End": datetime(2025, 12, 31),
        "Brief": "Traditional Lanna market, fireworks, and cultural performances in Mae On.",
        "Location": "CAD Cultural Center",
        "lat": 18.7663, "lon": 99.2421,
        "Link": "https://faceticket.net/en/product/30-december-2025-ticket-chiang-mai-cad-festival/"
    },
    {
        "Name": "Jing Jai Muan Muan Market",
        "Category": "Market",
        "Start": datetime(2025, 12, 18),
        "End": datetime(2025, 12, 21),
        "Brief": "Annual Open House with 600+ craft and organic food vendors.",
        "Location": "Jing Jai Central",
        "lat": 18.8073, "lon": 98.9955,
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    }
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🗓️ Event Navigator")
selected_date = st.sidebar.date_input("Pick a Date", datetime(2025, 12, 19))
view_mode = st.sidebar.radio("View Mode", ["Single Day", "Full Week"])

# --- FILTER LOGIC ---
if view_mode == "Single Day":
    display_start = datetime.combine(selected_date, datetime.min.time())
    display_end = display_start
else:
    display_start = datetime.combine(selected_date, datetime.min.time())
    display_end = display_start + timedelta(days=6)

# Filter events that overlap with the selected range
filtered_events = [
    e for e in events_master 
    if (e["Start"] <= display_end and e["End"] >= display_start)
]

# --- UI LAYOUT ---
st.title("🐘 Chiang Mai Event Explorer")
if view_mode == "Single Day":
    st.header(f"What's happening on {selected_date.strftime('%A, %b %d')}")
else:
    st.header(f"Events for the Week of {selected_date.strftime('%b %d')} - {(selected_date + timedelta(days=6)).strftime('%b %d')}")

# Map Section
if filtered_events:
    map_df = pd.DataFrame(filtered_events)
    st.map(map_df)
else:
    st.warning("No major festivals found for this specific date range.")

# Details Section
st.subheader("📍 Event List & Highlights")
if filtered_events:
    for ev in filtered_events:
        with st.expander(f"📌 {ev['Name']} ({ev['Location']})"):
            st.write(f"**About:** {ev['Brief']}")
            st.write(f"**Dates:** {ev['Start'].strftime('%b %d')} to {ev['End'].strftime('%b %d, %Y')}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("🌐 Info Page", ev['Link'])
            with c2:
                gmaps = f"https://www.google.com/maps/search/?api=1&query={ev['lat']},{ev['lon']}"
                st.link_button("📍 Get Directions", gmaps)
else:
    st.info("Check back later or try picking a date closer to Christmas/New Year!")

st.divider()
st.caption("Tip: Most Chiang Mai events are announced on Facebook. Always check 'Official Info' links for last-minute schedule changes.")