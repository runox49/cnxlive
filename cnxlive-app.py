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
        "Brief_CN": "市政府主办。31日跨年夜以纳瓦拉桥为中心，有大型烟火秀。",
        "Brief_EN": "Official city countdown. Fireworks at Nawarat Bridge on Dec 31st.",
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
    }
]

# --- 2. DATA: REGULAR MARKETS ---
regular_markets = [
    {"Name_CN": "清迈观光夜市", "Name_EN": "Night Bazaar", "Day": "Daily", "lat": 18.7850, "lon": 99.0001},
    {"Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Market", "Day": [5, 6], "lat": 18.8073, "lon": 98.9955},
    {"Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street", "Day": 6, "lat": 18.7877, "lon": 98.9933}
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
    if m["Day"] == "Daily" or any(d.weekday() in (m["Day"] if isinstance(m["Day"], list) else [m["Day"]]) for d in date_range):
        final_list.append(m)

# --- 4. MAIN DISPLAY ---
st.title("Elephant Chiang Mai Explorer 🐘")
st.markdown("---")

date_str = d_start.strftime('%B %d, %Y')
st.subheader(f"📅 {date_str}")

if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(item.get('Brief_EN', ''))
            st.write(item.get('Brief_CN', ''))
            st.link_button("🌐 Info", item.get('Link', '#'))

# --- 5. DYNAMIC TRAVEL TIPS (BASED ON DATE) ---
st.markdown("---")
st.subheader("🚀 Smart Travel Tips / 出行智能贴士")

# Logic to determine which tips to show
is_countdown = any(d.month == 12 and d.day == 31 for d in date_range)
is_weekend = any(d.weekday() in [5, 6] for d in date_range)

if is_countdown:
    st.warning("⚠️ **New Year's Eve Alert / 跨年预警**")
    st.markdown("""
    * **English:** Roads near Nawarat Bridge and Tha Phae Gate close around 6 PM. Book Grabs 2 hours early!
    * **中文:** 纳瓦拉桥及塔佩门周边道路约18:00封路。跨年用车请提前2小时预约。
    """)
elif is_weekend:
    st.info("🛍️ **Weekend Market Tip / 周末市集建议**")
    st.markdown("""
    * **English:** For Jing Jai Market, arrive before 8:30 AM to avoid crowds and get better organic coffee.
    * **中文:** 建议8:30前到达Jing Jai市集，可以避开人流并享受更好的有机咖啡。
    """)
else:
    st.success("🛵 **Weekday Tip / 平日建议**")
    st.markdown("""
    * **English:** Traffic is lighter. Great time to visit Doi Suthep or distant Artisan villages.
    * **中文:** 交通状况较好，非常适合前往素贴山或较远的文创村落（如大佛塔寺）。
    """)

# Seasonal Weather Tip (Always shows in winter)
if any(d.month in [11, 12, 1] for d in date_range):
    st.write("❄️ **Winter Note:** Temperature drops to 16°C at night. / **冬季提醒:** 晚间气温降至16°C，请带外套。")
