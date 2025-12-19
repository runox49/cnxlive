import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from fpdf import FPDF
import io

# Set Page Config
st.set_page_config(page_title="Chiang Mai Live Dashboard", page_icon="🐘", layout="wide")

# --- DATA ENGINE ---
events_master = [
    {
        "Name": "Charming Chiang Mai Flower Fest",
        "Category": "Festival",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief": "Theme: 'Gold of Lanna'. Massive light sculptures and musical fountain shows (7PM-10PM).",
        "Location": "Chiang Mai PAO Park", "lat": 18.8288, "lon": 98.9772,
        "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name": "Ping Fai Festival (Santa Village)",
        "Category": "Market",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief": "Toast marshmallows over open fires, shop at 50+ craft vendors in Nimman.",
        "Location": "One Nimman", "lat": 18.7999, "lon": 98.9678,
        "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name": "Jing Jai Muan Muan Market",
        "Category": "Market",
        "Start": datetime(2025, 12, 18), "End": datetime(2025, 12, 21),
        "Brief": "Annual Open House with 600+ craft and organic food vendors.",
        "Location": "Jing Jai Central", "lat": 18.8073, "lon": 98.9955,
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name": "Flora Festival 2025",
        "Category": "Festival",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief": "Millions of highland blooms and a 360-degree Sky Walk viewpoint.",
        "Location": "Royal Park Rajapruek", "lat": 18.7516, "lon": 98.9247,
        "Link": "https://www.royalparkrajapruek.org/"
    }
]

# --- SIDEBAR & FILTERS ---
st.sidebar.title("🗓️ Plan Your Trip")
selected_date = st.sidebar.date_input("Pick a Date", datetime(2025, 12, 19))
view_mode = st.sidebar.radio("View Range", ["Single Day", "Full Week"])

# Determine date range for filtering
d_start = datetime.combine(selected_date, datetime.min.time())
d_end = d_start if view_mode == "Single Day" else d_start + timedelta(days=6)

# Filter Logic
filtered_events = [e for e in events_master if (e["Start"] <= d_end and e["End"] >= d_start)]

# --- PDF GENERATOR FUNCTION ---
def generate_pdf(events, date_str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Chiang Mai Itinerary: {date_str}", ln=True, align="C")
    pdf.ln(10)
    
    for ev in events:
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, f"• {ev['Name']}", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 5, f"Location: {ev['Location']}\nDescription: {ev['Brief']}\nLink: {ev['Link']}\n")
        pdf.ln(5)
    
    return pdf.output()

# --- MAIN UI ---
st.title("🐘 Chiang Mai Event Explorer")
col_map, col_details = st.columns([2, 1])

with col_map:
    st.subheader("📍 Event Map")
    if filtered_events:
        st.map(pd.DataFrame(filtered_events))
    else:
        st.info("No major festivals found for this range.")

with col_details:
    st.subheader("📑 Itinerary Export")
    date_label = d_start.strftime('%b %d') if view_mode == "Single Day" else f"{d_start.strftime('%b %d')} - {d_end.strftime('%b %d')}"
    
    if filtered_events:
        pdf_data = generate_pdf(filtered_events, date_label)
        st.download_button(
            label="📥 Save as PDF Itinerary",
            data=bytes(pdf_data),
            file_name=f"ChiangMai_Itinerary_{selected_date}.pdf",
            mime="application/pdf"
        )
    
    st.markdown("---")
    st.write("**Top Tip:** Evening temperatures drop to 16°C. Bring a light jacket for the outdoor markets!")

# Display Event Cards
st.divider()
st.subheader(f"Highlights for {date_label}")
for ev in filtered_events:
    with st.expander(f"📌 {ev['Name']}"):
        st.write(ev['Brief'])
        st.link_button("Official Link", ev['Link'])