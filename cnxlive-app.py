import streamlit as st
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Chiang Mai Explorer", page_icon="🐘", layout="wide")

# --- 1. DATA: SPECIAL & SEASONAL EVENTS ---
festivals = [
    {
        "Name_CN": "清迈唐人街春节庆典", "Name_EN": "Chiang Mai Chinatown Chinese New Year",
        "Start": datetime(2026, 2, 16), "End": datetime(2026, 2, 19),
        "Brief_CN": "清迈瓦洛洛市场（唐人街）最热闹的时候。有舞龙舞狮、选美游行和绵延整条街的中华美食摊位，年味十足。",
        "Brief_EN": "Grand celebration at Warorot Market featuring dragon dances, cultural parades, and a massive street food market.",
        "lat": 18.7903, "lon": 99.0003, "Link": "https://www.google.com/search?q=Chiang+Mai+Chinese+New+Year+Warorot"
    },
    {
        "Name_CN": "春节红灯笼展 (布帕兰寺)", "Name_EN": "CNY Lantern Display at Wat Buppharam",
        "Start": datetime(2026, 2, 14), "End": datetime(2026, 2, 22),
        "Brief_CN": "为了庆祝春节，寺庙会挂起数以千计的红灯笼。这里曾是电影《泰囧》取景地，是春节期间清迈最热门的点灯打卡地。",
        "Brief_EN": "Famous 'Lost in Thailand' temple decorated with thousands of red lanterns for the Lunar New Year.",
        "lat": 18.7882, "lon": 99.0016, "Link": "https://www.google.com/search?q=Wat+Buppharam+Chiang+Mai+CNY"
    },
    {
        "Name_CN": "博桑纸伞手工艺节", "Name_EN": "Bo Sang Umbrella & Sankampaeng Craft Festival",
        "Start": datetime(2026, 1, 16), "End": datetime(2026, 1, 18),
        "Brief_CN": "清迈最亮丽的传统节日之一。整个博桑村会挂满五彩斑斓的纸伞，还有盛大的纸伞选美游行、手工艺市集和夜间灯光秀。",
        "Brief_EN": "One of the most colorful festivals in Chiang Mai. The village is decorated with umbrellas, featuring grand parades, craft markets, and cultural shows.",
        "lat": 18.7651, "lon": 99.0815, "Link": "https://www.facebook.com/BoSangUmbrellaFestival"
    },
    {
        "Name_CN": "坤昌阡樱花谷 (离市区最近)", "Name_EN": "Khun Chang Kian Cherry Blossom",
        "Start": datetime(2025, 12, 25), "End": datetime(2026, 2, 10),
        "Brief_CN": "清迈最具烟火气的赏樱地。粉色樱花散落在山村和咖啡馆间，仿佛世外桃源。建议在双龙寺换乘双条车。",
        "Brief_EN": "The closest cherry blossom spot to the city. Sakura trees bloom around Hmong village and coffee shops.",
        "lat": 18.8398, "lon": 98.8970, "Link": "https://www.google.com/search?q=Khun+Chang+Kian+Sakura"
    },
    {
        "Name_CN": "坤旺皇家农业中心 (最美樱花隧道)", "Name_EN": "Khun Wang Royal Agricultural Center",
        "Start": datetime(2025, 12, 25), "End": datetime(2026, 2, 15),
        "Brief_CN": "泰北最壮观的樱花胜地，拥有著名的樱花长廊。位于因他农山，花开满树时极为震撼。",
        "Brief_EN": "The most famous sakura tunnel in Northern Thailand located in Doi Inthanon National Park.",
        "lat": 18.6288, "lon": 98.5065, "Link": "https://maps.app.goo.gl/Tq3hM1D18a3SokLR7"
    },
    {
        "Name_CN": "皇家花园金莲花盛宴", "Name_EN": "Golden Shower Bloom at Royal Park Rajapruek",
        "Start": datetime(2026, 2, 1), "End": datetime(2026, 4, 30),
        "Brief_CN": "这里拥有清迈最集中、最壮观的金莲花林。作为泰国国花，金黄色的花瓣与园区内的泰式佛阁建筑相映生辉。",
        "Brief_EN": "The best place to see Thailand's national flower (Ratchaphruek) blooming in golden clusters alongside stunning Thai architecture.",
        "lat": 18.7480, "lon": 98.9249, "Link": "https://www.royalparkrajapruek.org/"
    },
    {
        "Name_CN": "古城护城河金黄走廊", "Name_EN": "Old City Moat Golden Shower Path",
        "Start": datetime(2026, 2, 15), "End": datetime(2026, 5, 10),
        "Brief_CN": "古城南门（松旁门）附近的护城河两岸。金色的花朵垂向水面，衬托着古老的城墙，是市区内最有氛围的赏花步行道。",
        "Brief_EN": "Beautiful golden shower trees lining the ancient city moat, especially near the South Gate (Suan Pung Gate).",
        "lat": 18.7816, "lon": 98.9815, "Link": "https://www.google.com/search?q=Chiang+Mai+Old+City+Moat+Flowers"
    },
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
        "Name_CN": "椰林集市", "Name_EN": "Coconut Market", "Day": [5, 6], "lat": 18.8378, "lon": 99.0335, 
        "Brief_CN": "位于翠绿椰林中的网红集市，非常适合周末拍照和品尝泰式小吃。", "Brief_EN": "Trendy market set in a coconut plantation, very photogenic.",
        "Link": "https://www.google.com/search?q=Coconut+Market+Chiang+Mai"
    }
]

# --- 3. UI & DATE LOGIC ---
st.sidebar.title("🗓️ Plan Your Trip")
selected_date = st.sidebar.date_input("Select Date", datetime.now())
view_mode = st.sidebar.radio("View Range", ["Single Day", "Full Week"])

d_start = datetime.combine(selected_date, datetime.min.time())
num_days = 1 if "Single" in view_mode else 7
date_range = [d_start + timedelta(days=i) for i in range(num_days)]

# --- 4. TOP: WEATHER FORECAST (大小调整为正文一致) ---
st.title("Elephant Chiang Mai Explorer 🐘")
st.subheader("🌤️ 3-Day Weather Forecast / 天气预报")
w_col1, w_col2, w_col3 = st.columns(3)
with w_col1:
    st.write("**Today / 今天**")
    st.write("28°C / 16°C | ☀️ 晴朗")
with w_col2:
    st.write("**Tomorrow / 明天**")
    st.write("29°C / 17°C | ☀️ 晴朗")
with w_col3:
    st.write("**Monday / 周一**")
    st.write("27°C / 15°C | 🌤️ 多云转晴")
st.markdown("---")

# --- 5. MAIN DISPLAY ---
final_list = []
for ev in festivals:
    if any(ev["Start"] <= d <= ev["End"] for d in date_range):
        final_list.append(ev)
for m in regular_markets:
    if m["Day"] == "Daily" or any(d.weekday() in (m["Day"] if isinstance(m["Day"], list) else [m["Day"]]) for d in date_range):
        final_list.append(m)

st.subheader(f"📅 活动预览: {d_start.strftime('%Y-%m-%d')}")

if final_list:
    for item in final_list:
        with st.expander(f"📍 {item['Name_EN']} | {item['Name_CN']}"):
            st.write(f"**{item.get('Brief_EN', '')}**")
            st.write(item.get('Brief_CN', ''))
            st.write("---")
            c1, c2 = st.columns(2)
            with c1: 
                st.link_button("🌐 Info", item['Link'])
            with c2:
                maps_url = f"https://www.google.com/maps/search/?api=1&query={item['lat']},{item['lon']}"
                st.link_button("📍 Navigation", maps_url)
else:
    st.info("该日期范围内暂无大型活动建议。")

# --- 6. TRAVEL TIPS (底部) ---
st.markdown("---")
with st.expander("🚀 Essential Travel Tips / 出行贴士", expanded=True):
    is_countdown = any(d.month == 12 and d.day == 31 for d in date_range)
    is_weekend = any(d.weekday() in [5, 6] for d in date_range)
    
    t1, t2 = st.columns(2)
    with t1:
        if is_countdown: st.error("🎆 **NYE Alert:** Road closures near Nawarat Bridge.")
        elif is_weekend: st.info("🛍️ **Weekend Market:** Visit JJ Market or Chamcha before 9 AM.")
        else: st.success("🛵 **Weekday:** Great time for Royal Park Rajapruek.")
    with t2:
        if is_countdown: st.markdown("**跨年提醒:** 纳瓦拉桥周边封路，建议步行。")
        elif is_weekend: st.markdown("**周末贴士:** JJ集市 或 雨林集市（Chamcha）周末氛围极好，建议早点去避开人流。")
        else: st.markdown("**平日贴士:** 皇家花园平日游览更清静。")
