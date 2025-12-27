import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "清迈官方跨年庆典 (纳瓦拉桥/塔佩门)", 
        "Name_EN": "Chiang Mai Countdown 2026 (Official)",
        "Start": datetime(2025, 12, 28), "End": datetime(2026, 1, 1),
        "Brief_CN": "市政府主办。28日起塔佩门有音乐会；31日跨年夜以纳瓦拉桥为中心，有大型烟火秀。",
        "Brief_EN": "Official city countdown. Concerts at Tha Phae Gate and fireworks at Nawarat Bridge.",
        "Location_CN": "纳瓦拉桥 & 塔佩门广场", "Location_EN": "Nawarat Bridge & Tha Phae Gate",
        "lat": 18.7879, "lon": 99.0045, "Link": "https://www.facebook.com/cmmayor"
    },
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 29), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。清迈年末最盛大的灯光盛宴。",
        "Brief_EN": "Massive light sculptures and musical fountain shows at the PAO Park.",
        "Location_CN": "清迈省政府中心", "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "皇家花园花卉节", "Name_EN": "Flora Festival",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "年度盛大花展，包含兰花园、空中步道和数百万株冬季花卉。",
        "Brief_EN": "Grand annual botanical garden festival featuring winter flower displays.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    }
]

# --- 2. DATA: REGULAR & DAILY MARKETS ---
regular_markets = [
    {
        "Name_CN": "清迈观光夜市 (每日)", "Name_EN": "Night Bazaar (Daily)",
        "Day": "Daily", "lat": 18.7850, "lon": 99.0001, "Link": "https://maps.google.com/?q=Night+Bazaar",
        "Brief_CN": "长康路上的每日夜市，包含阿努善市场，适合晚餐和按摩。", 
        "Brief_EN": "Iconic daily market on Chang Klan Road. Best for food and souvenirs."
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/",
        "Brief_CN": "清迈最有格调的市集，有机咖啡和高质感手作。", 
        "Brief_EN": "Upscale weekend market for organic food and coffee."
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "https://maps.google.com/?q=Sunday+Walking+Street",
        "Brief_CN": "全清迈最大的夜市，贯穿老城中心。", 
        "Brief_EN": "Chiang Mai largest and most famous night market."
    }
]

# --- 3. UI LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip")
selected_date = st.sidebar.date_input("Select Date", datetime.now())
view_mode = st.sidebar.radio("View Range", ["Single Day", "Full Week"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

for m in regular_markets:
    if m["Day"] == "Daily":
        final_list.append(m)
    else:
        active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
        if any(d.weekday() in active_days for d in date_range):
            final_list.append(m)

# --- 4. MAIN DISPLAY ---
st.title("Elephant Chiang Mai Explorer 🐘")
st.markdown("---")

date_str = d_start.strftime('%B %d, %Y') if "Single" in view_mode else f"Week of {d_start.strftime('%b %d')}"
st.subheader(f"📅 {date_str}")

if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(item.get('Brief_EN', ''))
            st.write(item.get('Brief_CN', ''))
            c1, c2 = st.columns(2)
            with c1: st.link_button("🌐 Info", item['Link'])
            with c2: 
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Navigation", maps_url)
else:
    st.info("No major events found for this selection.")

# --- 5. TRAVEL TIPS (AT BOTTOM) ---
st.markdown("---")
with st.expander("🚀 Essential Travel Tips / 出行贴士"):
    st.markdown("**Countdown:** Nawarat Bridge for fireworks. Expect road closures on Dec 31st.")
    st.markdown("**跨年建议:** 纳瓦拉桥观赏烟火的最佳地点，12月31日注意封路。")
