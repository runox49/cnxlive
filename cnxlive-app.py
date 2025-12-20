import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
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
        "Name_CN": "皇家花园花卉节", "Name_EN": "Flora Festival (Royal Park Rajapruek)",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "年度盛大花展，包含兰花园、空中步道和数百万株冬季花卉。",
        "Brief_EN": "Grand annual botanical garden festival featuring spectacular winter flower displays.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "Ping Fai 烤火节 (圣诞村)", "Name_EN": "Ping Fai Festival (Santa Village)",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区最火圣诞活动：围炉烤棉花糖、文创摊位、巨型圣诞树。",
        "Brief_EN": "The ultimate Christmas vibe in Nimman with marshmallow roasting and crafts.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name_CN": "CAD 跨年烟火秀", "Name_EN": "Chiang Mai CAD Countdown 2026",
        "Start": datetime(2025, 12, 30), "End": datetime(2025, 12, 31),
        "Brief_CN": "泰北最震撼的跨年烟火表演，结合兰纳文化表演。",
        "Brief_EN": "Breathtaking fireworks and Lanna cultural shows in Mae On.",
        "Location_CN": "CAD 文化中心", "Location_EN": "CAD Cultural Center Lanna",
        "lat": 18.7663, "lon": 99.2421, "Link": "https://faceticket.net/"
    }
]

# --- 2. DATA: REGULAR & DAILY MARKETS ---
regular_markets = [
    {
        "Name_CN": "清迈观光夜市 (每日)", "Name_EN": "Night Bazaar & Anusarn Market (Daily)",
        "Day": "Daily", "lat": 18.7850, "lon": 99.0001, "Link": "https://maps.app.goo.gl/LQc9jvvNSbGNGE7X90",
        "Brief_CN": "长康路上的每日夜市，包含阿努善市场，适合晚餐、按摩和海鲜。", "Brief_EN": "Iconic daily market on Chang Klan Road. Great for food, massage, and souvenirs."
    },
    {
        "Name_CN": "椰林市集", "Name_EN": "Coconut Market (Kad Bapao)",
        "Day": [5, 6], "lat": 18.8254, "lon": 99.0133, "Link": "https://www.facebook.com/kadmaprao/",
        "Brief_CN": "椰林中的绝美市集，适合拍照和地道小吃。", "Brief_EN": "Picturesque market in a coconut grove. Very photogenic."
    },
    {
        "Name_CN": "雨树市集", "Name_EN": "Chamcha Market (ฉำฉา)",
        "Day": [5, 6], "lat": 18.7758, "lon": 99.0712, "Link": "https://www.facebook.com/ChamchaMarket/",
        "Brief_CN": "桑甘烹区艺术地标，主打精致手作和蓝染。", "Brief_EN": "Artisan community market under giant rain trees."
    },
    {
        "Name_CN": "竹林亲子市集", "Name_EN": "Bamboo Family Market",
        "Day": [5, 6], "lat": 18.7885, "lon": 99.0825, "Link": "https://www.facebook.com/BambooFamilyMarket/",
        "Brief_CN": "温馨的竹林社区市集，亲子活动丰富。", "Brief_EN": "Eco-friendly community market in a bamboo forest."
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/",
        "Brief_CN": "清迈最有格调的市集，有机咖啡和高质感手作。", "Brief_EN": "Upscale weekend market for organic food and coffee."
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "http://maps.google.com/?q=Sunday+Walking+Street+Chiang+Mai",
        "Brief_CN": "全清迈最大的夜市，贯穿老城中心。", "Brief_EN": "Chiang Mai's largest and most famous night market."
    },
    {
        "Name_CN": "周六步行街", "Name_EN": "Saturday Walking Street",
        "Day": 5, "lat": 18.7812, "lon": 98.9863, "Link": "http://maps.google.com/?q=Saturday+Walking+Street+Chiang+Mai",
        "Brief_CN": "南门瓦莱路银器街市集，小吃极其丰富。", "Brief_EN": "Famous for silver crafts on Wualai Road south of the city."
    }
]

# --- 3. UI LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip / 行程计划")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime.now())
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

final_list = []

# NAP Week Logic (Dec 5 - 11)
is_nap_week = any(d.month == 12 and 5 <= d.day <= 11 for d in date_range)
if is_nap_week:
    final_list.append({
        "Name_CN": "⭐ NAP 宁曼艺术设计周", "Name_EN": "⭐ NAP Art & Design Promenade",
        "Brief_CN": "年度艺术盛会！宁曼路1巷封路，汇聚最顶尖的手作与设计。",
        "Brief_EN": "Iconic annual festival at Nimman Soi 1. The best of Chiang Mai art & design.",
        "Location_EN": "Nimman Soi 1", "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/nimmansoi1/"
    })

# Filter Festivals
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)

# Filter Regular & Daily Markets
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
            with c1: st.link_button("🌐 Info / 详情", item['Link'])
            with c2: 
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Navigation / 导航", maps_url)
else:
    st.info("No major events found for this selection.")

# --- 5. TRAVEL TIPS (Moved to Bottom) ---
st.markdown("---")
with st.expander("🚀 Essential Travel Tips / 出行必备贴士"):
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("**English:**\n* 🚕 **Grab/Maxim** apps are recommended for fair pricing.\n* 🌡️ **Weather:** 16°C mornings / 30°C afternoons. Dress in layers.\n* 💰 **Cash:** Markets still prefer cash; cafes take QR.")
    with t2:
        st.markdown("**中文:**\n* 🚕 推荐使用 **Grab** 或 **Maxim** 叫车。\n* 🌡️ **天气:** 早晚凉（16°C），中午热（30°C），建议洋葱式穿法。\n* 💰 **支付:** 市集主要使用现金，咖啡店支持扫码。")
