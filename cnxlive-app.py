import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。清迈年末最盛大的花卉灯光盛宴。",
        "Brief_EN": "Massive light sculptures and musical fountain shows. The biggest year-end flower fest.",
        "Location_CN": "清迈省政府公园", "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "2025 皇家花园花卉节", "Name_EN": "Flora Festival 2025 (Royal Park)",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "‘为未来绽放’。包含兰花园、空中步道及数百万株冬季花卉，非常壮观。",
        "Brief_EN": "Bloom for the Future. Featuring orchid houses, sky walks, and millions of winter flowers.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7516, "lon": 98.9247, "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "Ping Fai 烤火节", "Name_EN": "Ping Fai Festival",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区最火的圣诞活动：围炉烤棉花糖、文创市集、巨型圣诞树。",
        "Brief_EN": "The coolest Christmas vibe in Nimman: Marshmallow roasting and craft market.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.7999, "lon": 98.9678, "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name_CN": "CAD 跨年烟火秀", "Name_EN": "Chiang Mai CAD Countdown 2026",
        "Start": datetime(2025, 12, 30), "End": datetime(2025, 12, 31),
        "Brief_CN": "泰北跨年巅峰：极致烟火表演、兰纳文化演出与传统美食。",
        "Brief_EN": "The ultimate NYE event: Grand fireworks, cultural shows, and Lanna food.",
        "Location_CN": "CAD 文化中心", "Location_EN": "CAD Cultural Center",
        "lat": 18.7663, "lon": 99.2421, "Link": "https://faceticket.net/"
    }
]

# --- DATA: REGULAR & ARTISAN MARKETS ---
# Day: 5 = Saturday, 6 = Sunday
regular_markets = [
    {
        "Name_CN": "椰林市集 (Coconut Market)", "Name_EN": "Coconut Market (Kad Maprao)",
        "Day": [5, 6], 
        "Brief_CN": "清迈必拍！在优美的椰子林中逛吃，有独特的木桥步道。",
        "Brief_EN": "Instagrammable market in a coconut grove with wooden bridges and local food.",
        "Location_CN": "清迈东北郊区", "Location_EN": "Ban Phueak (Northeast CM)",
        "lat": 18.8354, "lon": 99.0333, "Link": "https://www.facebook.com/kadmaprao/"
    },
    {
        "Name_CN": "雨树市集 (Chamcha Market)", "Name_EN": "Chamcha Market (ฉำฉา)",
        "Day": [5, 6], 
        "Brief_CN": "文艺青年最爱。在大树下售卖精致手作服饰、蓝染和创意艺术品。",
        "Brief_EN": "Artisan community under giant trees featuring handmade clothing and crafts.",
        "Location_CN": "桑甘烹手工艺村", "Location_EN": "San Kamphaeng (Sankamphang Crafts)",
        "lat": 18.7758, "lon": 99.0712, "Link": "https://www.facebook.com/ChamchaMarket/"
    },
    {
        "Name_CN": "竹林亲子市集 (Bamboo Family Market)", "Name_EN": "Bamboo Family Market",
        "Day": [5, 6], 
        "Brief_CN": "隐藏在竹林里的社区市集，适合带小孩参加工作坊，环境极其舒适。",
        "Brief_EN": "Relaxed community market in a bamboo forest with workshops and organic food.",
        "Location_CN": "桑甘烹区", "Location_EN": "San Kamphaeng Area",
        "lat": 18.7885, "lon": 99.0825, "Link": "https://www.facebook.com/BambooFamilyMarket/"
    },
    {
        "Name_CN": "Jing Jai 'ม่วนม่วน' 市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6],
        "Brief_CN": "清迈最有质感的周末市集。主打有机农产、高品质手作和一流咖啡。",
        "Brief_EN": "Upscale weekend market for organic food, local coffee, and high-end crafts.",
        "Location_CN": "Jing Jai 创意区", "Location_EN": "Jing Jai Central",
        "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, 
        "Brief_CN": "清迈人气最旺的夜市。封锁老城主干道，物品极其丰富。",
        "Brief_EN": "Chiang Mai's most famous and largest night market in the heart of Old City.",
        "Location_CN": "老城塔佩门", "Location_EN": "Old City (Tha Phae Gate)",
        "lat": 18.7877, "lon": 98.9933, "Link": "http://google.com/maps?q=18.7877,98.9933"
    },
    {
        "Name_CN": "周六步行街", "Name_EN": "Saturday Walking Street",
        "Day": 5, 
        "Brief_CN": "位于南门瓦莱路，以精美的泰北银器和地道街头小吃著称。",
        "Brief_EN": "Famous for silver crafts and diverse street food on Wualai Road.",
        "Location_CN": "瓦莱路 (南门)", "Location_EN": "Wualai Road (South Gate)",
        "lat": 18.7812, "lon": 98.9863, "Link": "http://google.com/maps?q=18.7812,98.9863"
    }
]

# --- LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip / 行程计划")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime.now())
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

# Filter Festivals
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

# Filter Regular Markets
for m in regular_markets:
    active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
    if any(d.weekday() in active_days for d in date_range):
        final_list.append(m)

# --- DISPLAY ---
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
    st.info("No events found. / 该日期暂无活动。")

st.divider()
st.caption("Tip: Most artisan markets close by 3:00 PM. Night markets start from 6:00 PM.")
