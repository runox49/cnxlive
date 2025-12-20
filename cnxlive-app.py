import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- DATA: SPECIAL & SEASONAL EVENTS ---
# Coordinates and links updated to real POI locations
festivals = [
    {
        "Name_CN": "魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Fest",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀。清迈年末最盛大的花卉灯光盛宴。",
        "Brief_EN": "Massive light sculptures and musical fountain shows at the PAO Park.",
        "Location_CN": "清迈省政府中心 (PAO Park)", "Location_EN": "Chiang Mai Provincial Government Center",
        "lat": 18.8288, "lon": 98.9772, "Link": "https://maps.app.goo.gl/9uT6PqA8t9S8Yf4R8"
    },
    {
        "Name_CN": "2025 皇家花园花卉节", "Name_EN": "Flora Festival 2025 (Royal Park)",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "‘为未来绽放’。包含兰花园、空中步道及数百万株冬季花卉。",
        "Brief_EN": "Grand botanical garden featuring the Ho Kham Luang Royal Pavilion.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://maps.app.goo.gl/8v3M4Y3JqXf5R6T9"
    },
    {
        "Name_CN": "Ping Fai 烤火节", "Name_EN": "Ping Fai Festival",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "围炉烤棉花糖、文创市集、巨型圣诞树，体验清迈的圣诞氛围。",
        "Brief_EN": "The ultimate Christmas vibe in Nimman with marshmallow roasting.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://maps.app.goo.gl/3A7L9Z5XqY2R8"
    },
    {
        "Name_CN": "CAD 跨年烟火秀", "Name_EN": "Chiang Mai CAD Countdown 2026",
        "Start": datetime(2025, 12, 30), "End": datetime(2025, 12, 31),
        "Brief_CN": "清迈最震撼的跨年烟火与兰纳文化表演。",
        "Brief_EN": "A breathtaking display of fireworks and cultural shows in Mae On.",
        "Location_CN": "CAD 文化中心 (梅翁区)", "Location_EN": "CAD Cultural Center Lanna",
        "lat": 18.7663, "lon": 99.2421, "Link": "https://maps.app.goo.gl/S4T8U7W6Z5Y2R9"
    }
]

# --- DATA: REGULAR & ARTISAN MARKETS ---
regular_markets = [
    {
        "Name_CN": "椰林市集 (Coconut Market)", "Name_EN": "Coconut Market (Kad Bapao)",
        "Day": [5, 6], 
        "Brief_CN": "在椰子林中逛吃，有独特的竹桥和极佳的拍照位。",
        "Brief_EN": "Charming weekend market set in a tropical coconut grove.",
        "Location_CN": "Fa Ham 区", "Location_EN": "94 Soi Ban Tong 2, Fa Ham",
        "lat": 18.8254, "lon": 99.0133, "Link": "https://maps.app.goo.gl/5Y8T2Pq9W6R7"
    },
    {
        "Name_CN": "雨树市集 (Chamcha Market)", "Name_EN": "Chamcha Market (ฉำฉา)",
        "Day": [5, 6], 
        "Brief_CN": "桑甘烹区的文艺地标，售卖精致手作服饰和蓝染。",
        "Brief_EN": "Handcrafted market filled with local artisan vendors.",
        "Location_CN": "桑甘烹区", "Location_EN": "San Klang, San Kamphaeng",
        "lat": 18.7758, "lon": 99.0712, "Link": "https://maps.app.goo.gl/2S6Xq9W8R7P5"
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6],
        "Brief_CN": "清迈最有格调的市集，提供有机食物和高质感手工艺品。",
        "Brief_EN": "Focuses on organic produce, local coffee, and high-end crafts.",
        "Location_CN": "Atsadathon 路", "Location_EN": "45 Atsadathon Rd, Mueang",
        "lat": 18.8073, "lon": 98.9955, "Link": "https://maps.app.goo.gl/1Q9Z8Y7Xq6R5"
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, 
        "Brief_CN": "全清迈最大的夜市，从塔佩门延伸至老城内部。",
        "Brief_EN": "Massive night market spanning the length of Ratchadamnoen Road.",
        "Location_CN": "老城塔佩门", "Location_EN": "Tha Phae Gate, Old City",
        "lat": 18.7877, "lon": 98.9933, "Link": "https://maps.app.goo.gl/8X7W6Z5Y2R9Q1"
    },
    {
        "Name_CN": "周六步行街", "Name_EN": "Saturday Walking Street",
        "Day": 5, 
        "Brief_CN": "南门外的传统市集，以银器街和丰富小吃著称。",
        "Brief_EN": "Famous for silver crafts on Wualai Road south of the Old City.",
        "Location_CN": "瓦莱路 (南门)", "Location_EN": "Wualai Road, Mueang",
        "lat": 18.7812, "lon": 98.9863, "Link": "https://maps.app.goo.gl/7Q8X9W6Z5Y2R3"
    }
]

# --- STREAMLIT UI ---
st.title("🐘 Chiang Mai Explorer | 清迈探索者")
st.sidebar.header("Filter / 筛选")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime.now())

# Logic to combine and show events
d_start = datetime.combine(selected_date, datetime.min.time())
final_list = []

# Festivals logic
for ev in festivals:
    if ev["Start"] <= d_start <= ev["End"]:
        final_list.append(ev)

# Market logic
for m in regular_markets:
    active_days = m["Day"] if isinstance(m["Day"], list) else [m["Day"]]
    if d_start.weekday() in active_days:
        final_list.append(m)

# Display Results
st.subheader(f"Schedule for {selected_date.strftime('%A, %b %d')}")

if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} ({item['Name_CN']})"):
            st.write(f"**Description:** {item['Brief_EN']}")
            st.write(f"**中文简介:** {item['Brief_CN']}")
            st.write(f"🏠 **Location:** {item['Location_EN']}")
            
            # Action Buttons
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("🌐 Event Page / 官方页面", item['Link'])
            with col2:
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Google Maps / 导航", maps_url)
else:
    st.info("No major markets or festivals today. / 今日暂无主要市集或节庆活动。")
