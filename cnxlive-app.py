import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- DATA: SPECIAL EVENTS (One-off or Seasonal) ---
festivals = [
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。免费入场。",
        "Brief_EN": "Massive light sculptures and musical fountain shows. Free entry.",
        "Location_CN": "清迈省政府公园", "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "Ping Fai 烤火节", "Name_EN": "Ping Fai Festival",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区围炉烤棉花糖、文创摊位、巨型圣诞树。",
        "Brief_EN": "Toast marshmallows over open fires, craft vendors in Nimman.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.7999, "lon": 98.9678, "Link": "https://www.facebook.com/pro.onenimman/"
    }
]

# --- DATA: REGULAR & ARTISAN MARKETS ---
# Day: 5 = Saturday, 6 = Sunday
regular_markets = [
    {
        "Name_CN": "椰林市集 (Coconut Market)", "Name_EN": "Coconut Market",
        "Day": [5, 6], 
        "Brief_CN": "坐落在椰林中的绝美市集，适合拍照、品尝地道小吃。",
        "Brief_EN": "A picturesque market set in a coconut grove. Great for photos and local snacks.",
        "Location_CN": "清迈东北郊区", "Location_EN": "Ban Phueak (Northeast CM)",
        "lat": 18.8354, "lon": 99.0333, "Link": "https://www.facebook.com/kadmaprao/"
    },
    {
        "Name_CN": "雨树市集 (Chamcha Market)", "Name_EN": "Chamcha Market (ฉำฉา)",
        "Day": [5, 6], 
        "Brief_CN": "位于手工艺村，在大树下售卖精致手作服饰和创意艺术品。",
        "Brief_EN": "Artisan market under giant trees featuring handmade clothing and crafts.",
        "Location_CN": "桑甘烹手工艺村", "Location_EN": "San Kamphaeng (Sankamphang Crafts)",
        "lat": 18.7758, "lon": 99.0712, "Link": "https://www.facebook.com/ChamchaMarket/"
    },
    {
        "Name_CN": "竹林亲子市集 (Bamboo Family Market)", "Name_EN": "Bamboo Family Market",
        "Day": [5, 6], 
        "Brief_CN": "温馨的社区市集，有很多亲子活动、工作坊和健康有机食物。",
        "Brief_EN": "Community-focused market with kids' activities, workshops, and organic food.",
        "Location_CN": "桑甘烹区", "Location_EN": "San Kamphaeng Area",
        "lat": 18.7885, "lon": 99.0825, "Link": "https://www.facebook.com/BambooFamilyMarket/"
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, 
        "Brief_CN": "清迈规模最大的夜市，贯穿老城主干道。",
        "Brief_EN": "The biggest weekly market in CM, running through the Old City.",
        "Location_CN": "老城塔佩门", "Location_EN": "Old City (Tha Phae Gate)",
        "lat": 18.7877, "lon": 98.9933, "Link": "http://google.com/maps?q=Tha+Phae+Gate"
    }
]

# --- APP LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip / 行程计划")
# Default to current date if possible, else a specific date in 2025
try:
    default_date = datetime.now()
except:
    default_date = datetime(2025, 12, 20)

selected_date = st.sidebar.date_input("Select Date / 选择日期", default_date)
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

# 1. Add Festivals
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

# 2. Add Regular Markets
for m in regular_markets:
    active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
    if any(d.weekday() in active_days for d in date_range):
        final_list.append(m)

# --- UI DISPLAY ---
st.title("Elephant Chiang Mai Explorer 🐘 清迈探索者")
st.markdown(f"### {d_start.strftime('%B %d, %Y')} | {d_start.strftime('%Y年%m月%d日')}")
st.markdown("---")

if final_list:
    for item in final_list:
        with st.expander(f"📌 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(f"**{item['Brief_EN']}**")
            st.write(f"{item['Brief_CN']}")
            st.write(f"📍 {item['Location_EN']} | {item['Location_CN']}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("🌐 Info / 详情", item['Link'])
            with c2:
                gmaps = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Navigation / 导航", gmaps)
else:
    st.info("No major markets or festivals found for this date. / 该日期暂无主要市集或活动。")

st.divider()
st.caption("Tip: Most artisan markets (Coconut, Chamcha, Bamboo) only open on Sat/Sun until ~3:00 PM.")
