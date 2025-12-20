import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 29), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。清迈年末最盛大的灯光盛宴。",
        "Brief_EN": "Massive light sculptures and musical fountain shows at the PAO Park.",
        "Location_CN": "清迈省政府中心 (PAO Park)", "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "皇家花园花卉节", "Name_EN": "Flora Festival (Royal Park)",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "年度花展，包含兰花园和数百万株冬季花卉。",
        "Brief_EN": "Grand annual botanical garden festival featuring winter flower displays.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    }
]

# --- DATA: REGULAR MARKETS & ARTISAN SPOTS ---
regular_markets = [
    {"Name_CN": "椰林市集", "Name_EN": "Coconut Market", "Day": [5, 6], "lat": 18.8254, "lon": 99.0133, "Link": "https://www.facebook.com/kadmaprao/"},
    {"Name_CN": "雨树市集", "Name_EN": "Chamcha Market", "Day": [5, 6], "lat": 18.7758, "lon": 99.0712, "Link": "https://www.facebook.com/ChamchaMarket/"},
    {"Name_CN": "Jing Jai 市集", "Name_EN": "Jing Jai Weekend Market", "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/"},
    {"Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street", "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "https://maps.app.goo.gl/tha-phae-gate"},
]

# --- UI LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip")
selected_date = st.sidebar.date_input("Select Date", datetime.now())
view_mode = st.sidebar.radio("View Range", ["Single Day", "Full Week"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

# 1. NAP Week Logic (Dec 5 - 11)
is_nap_week = any(d.month == 12 and 5 <= d.day <= 11 for d in date_range)
if is_nap_week:
    final_list.append({
        "Name_CN": "⭐ NAP 宁曼艺术设计周",
        "Name_EN": "⭐ NAP Art & Design Promenade",
        "Brief_CN": "年度艺术盛会！宁曼路1巷封路，汇聚最顶尖的手作与设计。",
        "Brief_EN": "Iconic annual festival at Nimman Soi 1. The best of Chiang Mai art & crafts.",
        "Location_CN": "宁曼路 1 巷", "Location_EN": "Nimman Soi 1",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/nimmansoi1/"
    })

# 2. Add Festivals & Regular Markets
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

for m in regular_markets:
    active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
    if any(d.weekday() in active_days for d in date_range):
        final_list.append(m)

# --- MAIN DISPLAY ---
st.title("Elephant Chiang Mai Explorer 🐘")

# --- TRAVEL TIPS SECTION ---
with st.expander("🚀 Essential Travel Tips / 出行必备贴士"):
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""
        **English Tips:**
        * 🚕 **Getting Around:** Download **Grab** or **Maxim** for fair-priced taxis. For a local experience, hop on a **Songthaew** (Red Truck) - usually 30 THB per person within the city.
        * 🌡️ **Weather:** Dec/Jan is 'Cool Season'. Mornings are 16°C (60°F), afternoons are 30°C (86°F). **Dress in layers!**
        * 👟 **Artisan Markets:** Markets like Chamcha and Coconut are best visited before 11:00 AM to avoid the heat and crowds.
        """)
    with t2:
        st.markdown("""
        **中文贴士:**
        * 🚕 **交通:** 建议下载 **Grab** 或 **Maxim** 叫车。市内可以坐 **双条车 (Red Truck)**，古城内通常每人 30 泰铢。
        * 🌡️ **天气:** 12月/1月是凉季。清晨约 16°C，午后约 30°C。**请采用洋葱式穿法！**
        * 👟 **文创市集:** 像雨树市集和椰林市集建议在上午 11 点前到达，拍照更好看且不热。
        """)

st.markdown("---")

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
    st.info("No major events today.")
