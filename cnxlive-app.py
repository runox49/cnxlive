import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "清迈官方跨年庆典 (纳瓦拉桥)", "Name_EN": "Chiang Mai Countdown 2026",
        "Start": datetime(2025, 12, 28), "End": datetime(2026, 1, 1),
        "Brief_CN": "市政府主办。跨年夜以纳瓦拉桥为中心，有大型烟火秀和倒数仪式。",
        "Brief_EN": "Official city countdown with grand fireworks at Nawarat Bridge.",
        "lat": 18.7879, "lon": 99.0045, "Link": "https://www.facebook.com/cmmayor"
    },
    {
        "Name_CN": "NAP 文创艺术周", "Name_EN": "Nimman Art & Design Promenade (NAP)",
        "Start": datetime(2025, 12, 5), "End": datetime(2025, 12, 11),
        "Brief_CN": "宁曼路5巷最著名的文创艺术街头市集，汇集顶尖设计师作品。",
        "Brief_EN": "Famous art & design street fair at Nimman Soi 5.",
        "lat": 18.7995, "lon": 98.9680, "Link": "https://www.facebook.com/nimmansoi5"
    },
    {
        "Name_CN": "Ping Fai 烤火节 (圣诞村)", "Name_EN": "Ping Fai Festival",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区圣诞活动：围炉烤棉花糖、文创摊位、巨型圣诞树。",
        "Brief_EN": "Christmas vibe in Nimman with marshmallow roasting and crafts.",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name_CN": "坤昌阡樱花季", "Name_EN": "Khun Chang Kian Sakura",
        "Start": datetime(2025, 12, 25), "End": datetime(2026, 1, 31),
        "Brief_CN": "离城最近的樱花点。路窄，建议在素贴寺换乘双条车。",
        "Brief_EN": "Closest Sakura spot to city. Narrow road, Songthaew recommended.",
        "lat": 18.8394, "lon": 98.8974, "Link": "https://maps.app.goo.gl/rD6A28n4z3PjE6V9A"
    },
    {
        "Name_CN": "坤旺农业中心樱花隧道", "Name_EN": "Khun Wang Sakura Tunnel",
        "Start": datetime(2025, 12, 30), "End": datetime(2026, 2, 5),
        "Brief_CN": "最美的樱花隧道。位于茵他侬山，1月中旬是最佳观赏期。",
        "Brief_EN": "Iconic Sakura Tunnel at Doi Inthanon. Peak bloom in mid-Jan.",
        "lat": 18.6291, "lon": 98.5061, "Link": "https://maps.app.goo.gl/9Q6Y6xW7Z6Z6Z6Z6Z"
    }
]

# --- 2. DATA: REGULAR MARKETS ---
regular_markets = [
    {"Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Market", "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/"},
    {"Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street", "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "https://maps.app.goo.gl/ SundayWalkingStreet"},
    {"Name_CN": "椰林集市", "Name_EN": "Coconut Market", "Day": [5, 6], "lat": 18.8378, "lon": 99.0335, "Link": "https://maps.app.goo.gl/CoconutMarket"},
    {"Name_CN": "雨树集市", "Name_EN": "Chamcha Market", "Day": [5, 6], "lat": 18.7778, "lon": 99.0435, "Link": "https://maps.app.goo.gl/ChamchaMarket"}
]

# --- 3. UI & DATE LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip")
selected_date = st.sidebar.date_input("Select Date", datetime.now())
view_mode = st.sidebar.radio("View Range", ["Single Day", "Full Week"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

# --- 4. DYNAMIC TRAVEL TIPS ---
st.title("Elephant Chiang Mai Explorer 🐘")
st.markdown("---")

is_countdown = any(d.month == 12 and d.day == 31 for d in date_range)
is_weekend = any(d.weekday() in [5, 6] for d in date_range)
# 特别为坤旺增加判断逻辑
is_inthanon_season = any(d.month == 1 for d in date_range)

with st.expander("🚀 Essential Travel Tips / 出行贴士", expanded=True):
    c1, c2 = st.columns(2)
    with c1:
        if is_countdown:
            st.error("🎆 **NYE Alert:** Road closures at Nawarat Bridge from 6 PM.")
        elif is_inthanon_season:
            st.warning("🏔️ **Inthanon Tip:** Khun Wang is far (2.5h). Start at 5 AM!")
        elif is_weekend:
            st.info("🛍️ **Market Tip:** Go to Jing Jai before 9 AM for the best vibe.")
        else:
            st.success("🛵 **Weekday:** Perfect for Doi Suthep or cafe hopping.")
    with c2:
        if is_countdown:
            st.markdown("**跨年提醒:** 纳瓦拉桥周边封路，跨年夜用车极难预约。")
        elif is_inthanon_season:
            st.markdown("**观樱提醒:** 坤旺在茵他侬山深处，清晨出发可避开拥堵和浓雾。")
        elif is_weekend:
            st.markdown("**周末贴士:** 周日夜市下午5点入场；Jing Jai越早越好。")
        else:
            st.markdown("**平日贴士:** 避开高峰期，你可以独享宁曼路的网红咖啡馆。")

# --- 5. MAIN DISPLAY ---
final_list = []
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

for m in regular_markets:
    if m["Day"] == "Daily" or any(d.weekday() in (m["Day"] if isinstance(m["Day"], list) else [m["Day"]]) for d in date_range):
        final_list.append(m)

st.subheader(f"📅 {d_start.strftime('%B %d, %Y')}")
if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(item.get('Brief_EN', ''))
            st.write(item.get('Brief_CN', ''))
            st.link_button("🌐 Navigation / Info", item.get('Link', '#'))
else:
    st.info("No major events found for this selection.")
