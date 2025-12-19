import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 页面配置 / Page Config
st.set_page_config(page_title="Chiang Mai Live 2025", page_icon="🐘", layout="wide")

# --- 数据引擎 / DATA ENGINE ---
events_master = [
    {
        "Name_CN": "魅力清迈花卉节",
        "Name_EN": "Charming Chiang Mai Flower Fest",
        "Category": "Festival",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 5),
        "Brief_CN": "主题：‘兰纳之金’。大规模灯光雕塑、音乐喷泉秀（19:00, 20:00, 21:00, 22:00）。免费入场。",
        "Brief_EN": "Theme: 'Gold of Lanna'. Massive light sculptures, musical fountain shows (7, 8, 9, 10 PM). Free entry.",
        "Location_CN": "清迈省政府公园",
        "Location_EN": "Chiang Mai PAO Park",
        "lat": 18.8288, "lon": 98.9772,
        "Link": "https://www.facebook.com/charmingchiangmaiflowerfestival"
    },
    {
        "Name_CN": "Ping Fai 烤火节 (圣诞村)",
        "Name_EN": "Ping Fai Festival (Santa Village)",
        "Category": "Market",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "在宁曼区（Nimman）围炉烤棉花糖、逛 50+ 文创摊位、打卡巨型圣诞树。氛围感极佳。",
        "Brief_EN": "Toast marshmallows over open fires, shop at 50+ craft vendors in Nimman, and see the giant Christmas tree.",
        "Location_CN": "One Nimman 广场",
        "Location_EN": "One Nimman",
        "lat": 18.7999, "lon": 98.9678,
        "Link": "https://www.facebook.com/pro.onenimman/"
    },
    {
        "Name_CN": "Jing Jai 'ม่วนม่วน' 年度市集",
        "Name_EN": "Jing Jai Muan Muan Market",
        "Category": "Market",
        "Start": datetime(2025, 12, 18), "End": datetime(2025, 12, 21),
        "Brief_CN": "年度开放日，600+ 摊位。集合兰纳手工艺品、有机咖啡和环保艺术，清迈必逛。",
        "Brief_EN": "Annual Open House with 600+ vendors. Best for high-quality Lanna crafts, organic coffee, and eco-friendly art.",
        "Location_CN": "Jing Jai 创意区",
        "Location_EN": "Jing Jai Central",
        "lat": 18.8073, "lon": 98.9955,
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name_CN": "2025 皇家花园花卉节",
        "Name_EN": "Flora Festival 2025",
        "Category": "Festival",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "主题：‘为未来绽放’。亮点包括兰花园、360度空中步道及数百万株冬季花卉。",
        "Brief_EN": "Theme: 'Bloom for the Future'. Highlights include the Orchid House, 360-degree Sky Walk, and millions of blooms.",
        "Location_CN": "拉查帕皇家花园",
        "Location_EN": "Royal Park Rajapruek",
        "lat": 18.7516, "lon": 98.9247,
        "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "清迈马拉松博览会",
        "Name_EN": "Chiang Mai Marathon Expo",
        "Category": "Sports",
        "Start": datetime(2025, 12, 19), "End": datetime(2025, 12, 20),
        "Brief_CN": "马拉松领物展。塔佩门附近非常热闹，有很多运动装备摊位和当地美食。",
        "Brief_EN": "Race pack collection for the marathon. Lively area with sports gear booths and local food near the gate.",
        "Location_CN": "塔佩门",
        "Location_EN": "Tha Phae Gate",
        "lat": 18.7877, "lon": 98.9933,
        "Link": "https://www.chiangmaimarathon.com/"
    }
]

# --- 侧边栏 / SIDEBAR ---
st.sidebar.title("🗓️ Plan Your Trip / 行程计划")
selected_date = st.sidebar.date_input("Select Date / 选择日期", datetime(2025, 12, 19))
view_mode = st.sidebar.radio("View Range / 查看范围", ["Single Day / 单日", "Full Week / 整周"])

# 日期过滤逻辑 / Date Logic
d_start = datetime.combine(selected_date, datetime.min.time())
d_end = d_start if "Single" in view_mode else d_start + timedelta(days=6)
filtered_events = [e for e in events_master if (e["Start"] <= d_end and e["End"] >= d_start)]

# --- 主页面 UI / MAIN UI ---
st.title("🐘 Chiang Mai Event Explorer")
st.title("清迈动态活动探索器")

date_label_en = d_start.strftime('%B %d, %Y') if "Single" in view_mode else f"{d_start.strftime('%b %d')} - {d_end.strftime('%B %d, %Y')}"
date_label_cn = d_start.strftime('%Y年%m月%d日') if "Single" in view_mode else f"{d_start.strftime('%m月%d日')} - {d_end.strftime('%Y年%m月%d日')}"

st.subheader(f"📅 {date_label_en} | {date_label_cn}")

# --- 活动详情列表 / EVENT DETAILS ---
st.markdown("### 📍 Highlights / 重点活动")

if filtered_events:
    for ev in filtered_events:
        with st.expander(f"📌 {ev['Name_EN']} | {ev['Name_CN']}"):
            # 中英描述
            st.write(f"**** {ev['Brief_EN']}")
            st.write(f"**** {ev['Brief_CN']}")
            st.write(f"**Location / 地点:** {ev['Location_EN']} ({ev['Location_CN']})")
            st.write(f"**Dates / 日期:** {ev['Start'].strftime('%b %d')} - {ev['End'].strftime('%b %d, %Y')}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("🌐 Official Link / 官方链接", ev['Link'])
            with c2:
                # 谷歌地图导航
                gmaps = f"https://www.google.com/maps/search/?api=1&query={ev['lat']},{ev['lon']}"
                st.link_button("📍 Google Maps / 导航", gmaps)
else:
    st.info("No major events for this range. / 该时段暂无大型活动。")

st.divider()

# 温馨提示 / Tips
t1, t2 = st.columns(2)
with t1:
    st.info("""
    **💡 Travel Tip:**
    Nights in December drop to **16°C**. Wear a light jacket for outdoor night markets!
    """)
with t2:
    st.info("""
    **💡 出行贴士:**
    12月清迈夜晚气温会降至 **16°C** 左右。逛夜市记得带件轻便外套，防风保暖。
    """)