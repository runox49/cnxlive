import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "清迈官方跨年庆典 (纳瓦拉桥/塔佩门)", "Name_EN": "Chiang Mai Countdown 2026 (Official)",
        "Start": datetime(2025, 12, 28), "End": datetime(2026, 1, 1),
        "Brief_CN": "市政府主办。28日起塔佩门有音乐会；31日跨年夜以纳瓦拉桥为中心，有大型烟火秀和倒数仪式。",
        "Brief_EN": "Official city countdown. Concerts at Tha Phae Gate from 28th. Grand fireworks & countdown at Nawarat Bridge on 31st.",
        "Location_CN": "纳瓦拉桥 & 塔佩门广场", "Location_EN": "Nawarat Bridge & Tha Phae Gate",
        "lat": 18.7879, "lon": 99.0045, "Link": "https://www.facebook.com/cmmayor"
    },
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
        "Brief_EN": "Grand annual botanical garden festival featuring winter flower displays.",
        "Location_CN": "拉查帕皇家花园", "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    }
]

# --- 2. DATA: REGULAR & DAILY MARKETS ---
regular_markets = [
    {
        "Name_CN": "清迈观光夜市 (每日)", "Name_EN": "Night Bazaar & Anusarn (Daily)",
        "Day": "Daily", "lat": 18.7850, "lon": 99.0001, "Link": "http://google.com/maps?q=18.7850,99.0001",
        "Brief_CN": "长康路上的每日夜市，包含阿努善市场，适合晚餐、按摩和海鲜。", 
        "Brief_EN": "Iconic daily market on Chang Klan Road. Best for food and souvenirs."
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Weekend Market",
        "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, "Link": "https://www.facebook.com/jjmarketchiangmai/",
        "Brief_CN": "清迈最有格调的市集，有机咖啡和高质感手作。", "Brief_EN": "Upscale weekend market for organic food and coffee."
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street",
        "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "http://google.com/maps?q=18.7877,98.9933",
        "Brief_CN": "全清迈最大的夜市，贯穿老城中心。", "Brief_EN": "Chiang Mai's largest and most famous night market."
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
            c1, c2 = st.columns(2)
            with c1: st.link_button("🌐 Info", item['Link'])
            with c2: 
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Navigation", maps_url)
else:
    st.info("No major events found for this selection.")

# --- 5. FIXED DYNAMIC TRAVEL TIPS ---
st.markdown("---")
with st.expander("🚀 Essential Travel Tips / 出行贴士", expanded=True):
    # Logic based on selected_date
    is_countdown = (selected_date.month == 12 and selected_date.day == 31)
    is_weekend = (selected_date.weekday() in [5, 6])
    
    t1, t2 = st.columns(2)
    
    with t1:
        if is_countdown:
            st.markdown("""
**Countdown Special:**
* 🎆 **Nawarat Bridge:** Best for midnight fireworks.
* 🚶 **Closures:** Roads close around 6 PM. Walking is recommended!
            """)
        elif is_weekend:
            st.markdown("""
**Weekend Tip:**
* 🛍️ **Markets:** Sunday Walking Street starts at 5 PM. 
* ☕ **Jing Jai:** Go before 9 AM to avoid the biggest crowds.
            """)
        else:
            st.markdown("""
**Weekday Tip:**
* 🛵 **Traffic:** Lighter traffic! Perfect for visiting Doi Suthep.
* ☕ **Cafes:** Enjoy Nimman cafes without the weekend wait times.
            """)

    with t2:
        if is_countdown:
            st.markdown("""
**跨年特别提醒:**
* 🎆 **纳瓦拉桥:** 观赏跨年烟火的最佳地点。
* 🚶 **封路状况:** 12月31日晚建议步行，用车极其困难。
            """)
        elif is_weekend:
            st.markdown("""
**周末贴士:**
* 🛍️ **市集:** 周日夜市下午5点开始，越晚人越多。
* ☕ **Jing Jai:** 建议上午9点前到达，体验感最佳。
            """)
        else:
            st.markdown("""
**平日贴士:**
* 🛵 **交通:** 拥堵较少，适合去远郊或者素贴山。
* ☕ **宁曼路:** 工作日去网红咖啡店基本不需要排队。
            """)
