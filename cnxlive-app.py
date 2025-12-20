import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- DATA: SPECIAL & SEASONAL EVENTS ---
# Verified POI Coordinates
festivals = [
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 29), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。清迈年末最盛大的花卉灯光盛宴。",
        "Brief_EN": "Massive light sculptures and musical fountain shows at the PAO Park.",
        "Location_CN": "清迈省政府中心 (PAO Park)", "Location_EN": "Chiang Mai Provincial Government Center",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "2025 皇家花园花卉节", "Name_EN": "Flora Festival 2025 (Royal Park)",
        "Start": datetime(2025, 11, 17), "End": datetime(2026, 2, 28),
        "Brief_CN": "‘为未来绽放’。包含兰花园、空中步道及数百万株冬季花卉。",
        "Brief_EN": "Grand botanical garden featuring the Ho Kham Luang Royal Pavilion.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "Ping Fai 烤火节 (圣诞村)", "Name_EN": "Ping Fai Festival (Santa Village)",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区最火圣诞活动：围炉烤棉花糖、50+文创摊位、巨型圣诞树。",
        "Brief_EN": "The ultimate Christmas vibe in Nimman with marshmallow roasting and crafts.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name_CN": "CAD 跨年烟火秀", "Name_EN": "Chiang Mai CAD Countdown 2026",
        "Start": datetime(2025, 12, 30), "End": datetime(2025, 12, 31),
        "Brief_CN": "泰北最震撼的烟火表演，结合兰纳文化表演与传统美食。",
        "Brief_EN": "Breathtaking fireworks and Lanna cultural shows in Mae On.",
        "Location_CN": "CAD 文化中心 (梅翁区)", "Location_EN": "CAD Cultural Center Lanna",
        "lat": 18.7663, "lon": 99.2421, "Link": "https://faceticket.net/"
    }
]

# --- DATA: REGULAR & ARTISAN MARKETS ---
regular_markets = [
    {
        "Name_CN": "椰林市集 (Coconut Market)", "Name_EN": "Coconut Market (Kad Bapao)",
        "Day": [5, 6], # Sat, Sun
        "Brief_CN": "在椰子林中逛吃，有独特的木桥步道。建议早起避开人流。",
        "Brief_EN": "Charming weekend market set in a tropical coconut grove. Highly photogenic.",
        "Location_CN": "Fa Ham 区", "Location_EN": "94 Soi Ban Tong 2, Fa Ham",
        "lat": 18.8254, "lon": 99.0133, "Link": "https://www.facebook.com/kadmaprao/"
    },
    {
        "Name_CN": "雨树市集 (Chamcha Market)", "Name_EN": "Chamcha Market (ฉำฉา)",
        "Day": [5, 6], # Sat, Sun
        "Brief_CN": "文艺青年地标。在大树下售卖精致手作服饰、蓝染和创意艺术品。",
        "Brief_EN": "Artisan community market under giant rain trees. Famous for slow fashion.",
        "Location_CN": "桑甘烹区", "Location_EN": "13/16 Moo 2, Soi 11, San Klang",
        "lat": 18.7758, "lon": 99.0712, "Link": "https://www.facebook.com/ChamchaMarket/"
    },
    {
        "Name_CN": "竹林亲子市集 (Bamboo Family Market)", "Name_EN": "Bamboo Family Market",
        "Day": [5, 6], # Check FB for specific monthly weekends
        "Brief_CN": "温馨的社区市集。主打亲子活动、健康有机食物和手工体验。",
        "Brief_EN": "Eco-friendly market in a bamboo grove with workshops and kids' activities.",
        "Location_CN": "Sanggadee Space", "Location_EN": "Sang Ga Dee Space, San Kamphaeng",
        "lat": 18.7885, "lon": 99.0825, "Link": "https://www.facebook.com/BambooFamilyMarket/"
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6],
        "Brief_CN": "清迈最有格调的市集。主打有机咖啡、高质感手作和清晨现场音乐。",
        "Brief_EN": "Focuses on organic produce, artisan coffee, and curated handicrafts.",
        "Location_CN": "Atsadathon 路", "Location_EN": "45 Atsadathon Rd, Pa Tan",
        "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, 
        "Brief_CN": "全清迈最大的夜市。封锁老城主干道，物品极丰，极具当地氛围。",
        "Brief_EN": "Massive night market spanning Ratchadamnoen Road. A must-visit.",
        "Location_CN": "塔佩门", "Location_EN": "Tha Phae Gate, Old City",
        "lat": 18.7877, "lon": 98.9933, "Link": "http://maps.google.com/?q=Sunday+Walking+Street+Chiang+Mai"
    },
    {
        "Name_CN": "周六步行街", "Name_EN": "Saturday Walking Street",
        "Day": 5, 
        "Brief_CN": "瓦莱路传统的银器街市集，以手工银器和小吃闻名。",
        "Brief_EN": "Famous for silver crafts and diverse street food south of the city gates.",
        "Location_CN": "瓦莱路 (南门)", "Location_EN": "Wualai Road, Mueang",
        "lat": 18.7812, "lon": 98.9863, "Link": "http://maps.google.com/?q=Saturday+Walking+Street+Chiang+Mai"
    }
]

# --- STREAMLIT UI ---
st.title("🐘 Chiang Mai Explorer | 清迈探索者")
st.markdown("---")

# Sidebar
st.sidebar.header("Filter / 筛选")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime.now())
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

# Date Logic
d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

# Filter logic
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

for m in regular_markets:
    active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
    if any(d.weekday() in active_days for d in date_range):
        final_list.append(m)

# Display Results
date_str = d_start.strftime('%A, %b %d') if "Single" in view_mode else f"Week of {d_start.strftime('%b %d')}"
st.subheader(f"📅 {date_str}")

if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(f"**Description:** {item['Brief_EN']}")
            st.write(f"**中文简介:** {item['Brief_CN']}")
            st.write(f"🏠 **Location:** {item['Location_EN']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🌐 Info / 详情", item['Link'])
            with col2:
                # Direct Google Maps Link with Coordinates
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Google Maps / 导航", maps_url)
else:
    st.info("No major events found for this selection. / 所选时段暂无主要活动。")

st.divider()
st.caption("Cool Season Guide 2025/2026. Data verified against local event schedules.")
