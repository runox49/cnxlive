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
    },
    {
        "Name_CN": "Ping Fai 烤火节 (圣诞村)", "Name_EN": "Ping Fai Festival (Santa Village)",
        "Start": datetime(2025, 12, 13), "End": datetime(2025, 12, 25),
        "Brief_CN": "宁曼区圣诞活动：围炉烤棉花糖、文创摊位、巨型圣诞树。",
        "Brief_EN": "Christmas vibe in Nimman with marshmallow roasting and crafts.",
        "Location_CN": "One Nimman 广场", "Location_EN": "One Nimman",
        "lat": 18.8001, "lon": 98.9684, "Link": "https://www.facebook.com/pro.onenimman/"
    }
]

# --- 2. DATA: REGULAR & DAILY MARKETS ---
regular_markets = [
    {
        "Name_CN": "清迈观光夜市 (每日)", "Name_EN": "Night Bazaar & Anusarn (Daily)",
        "Day": "Daily", "lat": 18.7850, "lon": 99.0001, "Link": "https://maps.app.goo.gl/Yy6m6",
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
        "Day": 6, "lat": 18.7877, "lon": 98.9933, "Link": "https://maps.app.goo.gl/18",
        "Brief_CN": "全清
