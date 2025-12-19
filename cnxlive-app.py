import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config / 页面配置
st.set_page_config(page_title="Chiang Mai Live 2025-26", page_icon="🐘", layout="wide")

# --- DATA ENGINE / 数据引擎 ---
events_master = [
    {
        "Name_CN": "魅力清迈花卉节",
        "Name_EN": "Charming Chiang Mai Flower Fest",
        "Category": "Festival",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief_CN": "大规模灯光雕塑、音乐喷泉秀（19:00 - 22:00）。免费入场。",
        "Brief_EN": "Massive light sculptures and musical fountain shows (7 PM - 10 PM). Free entry.",
        "Location_CN": "清迈省政府公园",
        "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772,
        "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "Jing Jai 'ม่วนม่วน' 年度市集",
        "Name_EN": "Jing Jai Muan Muan Market",
        "Category": "Market",
        "Start": datetime(2025, 12, 18), "End": datetime(2025, 12, 21),
        "Brief_CN": "年度开放日，600+ 摊位。集合兰纳手工艺品、有机咖啡和环保艺术。",
        "Brief_EN": "Annual Open House with 600+ vendors. Best for high-quality Lanna crafts and organic coffee.",
        "Location_CN": "Jing Jai 创意区",
        "Location_EN": "Jing Jai Central",
        "lat": 18.8073, "lon": 98.9955,
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name_CN": "CAD 跨年烟火秀 (Light of Faith)",
        "Name_EN": "Chiang Mai CAD Countdown 2026",
        "Category": "Festival",
        "Start": datetime(2025, 12, 30), "End": datetime(2025, 12, 31),
        "Brief_CN": "泰北最盛大的烟火表演，结合兰纳文化演出与传统美食市集。",
        "Brief_EN": "The grandest fireworks in Northern Thailand with cultural performances and a Lanna food market.",
        "Location_CN": "CAD 文化中心 (Mae On)",
        "Location_EN": "CAD Cultural Center",
        "lat": 18.7663, "lon": 99.2421,
        "Link": "https://faceticket.net/en/product/30-december-2025-ticket-chiang-mai-cad-festival/"
    },
    {
        "Name_CN": "数字游民大会 2026",
        "Name_EN": "Nomad Summit 2026",
        "Category": "Conference",
        "Start": datetime(2026, 1, 16), "End": datetime(2026, 1, 18),
        "Brief_CN": "全球数字游民聚集地，包含行业讲座、社交工作坊及泳池派对。",
        "Brief_EN": "World-class gathering for digital nomads featuring talks, networking, and a pool party.",
        "Location_CN": "宁曼区多处地点",
        "Location_EN": "Nimman Area / Various Venues",
        "lat": 18.7999, "lon": 98.9678,
        "Link": "https://www.nomadsummit.com/"
    },
    {
        "Name_CN": "博桑伞节 & 手工艺节",
        "Name_EN": "Bo Sang Umbrella Festival",
        "Category": "Culture",
        "Start": datetime(2026, 1, 16), "End": datetime(2026, 1, 18),
        "Brief_CN": "著名的传统纸伞庆典，有选美比赛、手工艺游行和精美现场彩绘。",
        "Brief_EN": "Iconic festival celebrating traditional paper umbrellas with parades, beauty pageants, and live painting.",
        "Location_CN": "博桑手工艺村",
        "Location_EN": "Bo Sang Handicraft Village",
        "lat": 18.7650, "lon": 99.0811,
        "Link": "https://www.tourismthailand.org/"
    }
]

# --- SIDEBAR / 侧边栏 ---
st.sidebar.title("🗓️ Plan Your Trip / 行程计划")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime(2025, 12, 19))
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

# Date Logic / 日期逻辑
d_start = datetime.combine(selected_date, datetime.min.time())
d_end = d_start if "Single" in view_mode else d_start + timedelta(days=6)
filtered_events = [e for e in events_master if (e["Start"] <= d_end and e["End"] >= d_start)]

# --- MAIN UI / 主页面 ---
st.title("Elephant Chiang Mai Explorer 🐘 清迈探索者")

date_label_en = d_start.strftime('%B %d, %Y') if "Single" in view_mode else f"{d_start.strftime('%b %d')} - {d_end.strftime('%B %d, %Y')}"
date_label_cn = d_start.strftime('%Y年%m月%d日') if "Single" in view_mode else f"{d_start.strftime('%m月%d日')} - {d_end.strftime('%Y年%m月%d日')}"

st.subheader(f"📅 {date_label_en} | {date_label_cn}")

# --- EVENT LIST / 活动列表 ---
st.markdown("---")
if filtered_events:
    for ev in filtered_events:
        # Title without "English/Chinese" labels
        with st.expander(f"📌 {ev['Name_EN']} | {ev['Name_CN']}"):
            st.write(ev['Brief_EN'])
            st.write(ev['Brief_CN'])
            st.write(f"**Location / 地点:** {ev['Location_EN']} ({ev['Location_CN']})")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("🌐 More Info / 更多信息", ev['Link'])
            with c2:
                gmaps = f"https://www.google.com/maps/search/?api=1&query={ev['lat']},{ev['lon']}"
                st.link_button("📍 Navigation / 导航", gmaps)
else:
    st.info("No major events for this range. / 该时段暂无大型活动。")

st.divider()
st.caption("Tip: Most local markets are most active on weekends (Sat-Sun). / 提示：当地市集在周末（周六日）最为活跃。")