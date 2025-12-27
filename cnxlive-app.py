import streamlit as st
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "皇家花园花卉节", "Name_EN": "Flora Festival at Royal Park Rajapruek",
        "Start": datetime(2025, 11, 1), "End": datetime(2026, 2, 28),
        "Brief_CN": "清迈最负盛名的皇家花园年度盛典，有壮观的兰花园、各国园林及百万株花卉。",
        "Brief_EN": "Annual grand flower festival at Royal Park Rajapruek featuring orchid gardens and international flora.",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "2026 魅力清迈花卉节", "Name_EN": "Charming Chiang Mai Flower Festival",
        "Start": datetime(2025, 11, 28), "End": datetime(2026, 1, 4),
        "Brief_CN": "大型冬季花展，有绝美灯光秀、音乐喷泉和各色温带花卉，晚上非常漂亮。",
        "Brief_EN": "Grand flower festival with light shows, musical fountains, and winter blooms.",
        "lat": 18.8258, "lon": 98.9665, "Link": "https://www.facebook.com/CharmingChiangMaiFlowerFestival"
    },
    {
        "Name_CN": "Sawasdee Craft 手作艺术节", "Name_EN": "Sawasdee Craft at Baan Kang Wat",
        "Start": datetime(2025, 12, 27), "End": datetime(2026, 1, 3),
        "Brief_CN": "在森林艺术村 Baan Kang Wat 举办的年度手作盛会，汇集顶级匠人与工作坊。",
        "Brief_EN": "Annual craft festival at the artist village featuring local artisans and workshops.",
        "lat": 18.7766, "lon": 98.9485, "Link": "https://www.facebook.com/sawasdeecraft.chiangmai"
    },
    {
        "Name_CN": "清迈官方跨年庆典", "Name_EN": "Chiang Mai Countdown 2026",
        "Start": datetime(2025, 12, 28), "End": datetime(2026, 1, 1),
        "Brief_CN": "跨年夜以纳瓦拉桥为中心，有大型烟火秀和倒数仪式，感受万人齐聚的热闹。",
        "Brief_EN": "Official city countdown with grand fireworks at Nawarat Bridge.",
        "lat": 18.7879, "lon": 99.0045, "Link": "https://www.facebook.com/cmmayor"
    },
    {
        "Name_CN": "NAP 文创艺术周", "Name_EN": "Nimman Art & Design Promenade (NAP)",
        "Start": datetime(2025, 12, 5), "End": datetime(2025, 12, 11),
        "Brief_CN": "宁曼路5巷最著名的文创艺术街头市集，汇集清迈顶尖设计师作品。",
        "Brief_EN": "Famous art & design street fair at Nimman Soi 5.",
        "lat": 18.7995, "lon": 98.9680, "Link": "https://www.facebook.com/nimmansoi5"
    }
]

# --- 2. DATA: REGULAR MARKETS ---
regular_markets = [
    {
        "Name_CN": "雨树集市", "Name_EN": "Chamcha Market", "Day": [5, 6], "lat": 18.7778, "lon": 99.0435, 
        "Brief_CN": "位于手工艺术村，艺术气息浓厚，有现场音乐和极具设计感的手工艺品。", "Brief_EN": "Artsy market in a craft village with live music and unique handmade crafts.",
        "Link": "https://www.facebook.com/chamchamarket/"
    },
    {
        "Name_CN": "长康路观光夜市 (每日)", "Name_EN": "Night Bazaar (Daily)", "Day": "Daily", "lat": 18.7850, "lon": 99.0001, 
        "Brief_CN": "清迈最著名的每日夜市，适合晚餐、购买特产和足疗放松。", "Brief_EN": "Iconic daily night market on Chang Klan Road. Great for dinner and shopping.",
        "Link": "https://www.google.com/search?q=Chiang+Mai+Night+Bazaar"
    },
    {
        "Name_CN": "周日步行街", "Name_EN": "Sunday Walking Street", "Day": 6, "lat": 18.7877, "lon": 98.9933, 
        "Brief_CN": "清迈规模最大的夜市，贯穿古城中心，每周日晚开放。", "Brief_EN": "Chiang Mai's largest night market in the Old City, open Sunday evenings.",
        "Link": "https://www.google.com/search?q=Sunday+Walking+Street+Chiang+Mai"
    },
    {
        "Name_CN": "Jing Jai 周末市集", "Name_EN": "Jing Jai Market", "Day": [5, 6], "lat": 18.8073, "lon": 98.9955, 
        "Brief_CN": "清迈最有格调的早市：有机农产品、高质感手作和清迈最好的咖啡氛围。", "Brief_EN": "Organic food, quality crafts, and the best coffee vibes.",
        "Link": "https://www.facebook.com/jjmarketchiangmai/"
    },
    {
        "Name_CN": "椰林集市", "Name_EN": "Coconut Market", "Day": [5, 6], "lat": 18.8378, "lon":
