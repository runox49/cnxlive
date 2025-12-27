import streamlit as st
from datetime import datetime
import math

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Chiang Mai Explorer",
    page_icon="🐘",
    layout="wide"
)

# ---------------- Basic Style ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Language ----------------
lang = st.radio("Language / 语言", ["中文", "English"], horizontal=True)

def t(cn, en):
    return cn if lang == "中文" else en

# ---------------- Title ----------------
st.title(t("🐘 清迈住客探索指南", "🐘 Chiang Mai Guest Explorer"))
st.caption(
    t(
        "为住客准备的清迈活动、市集与周边推荐",
        "A curated guide to events, markets & nearby spots for our guests"
    )
)

# =========================================================
# 1️⃣ 房源位置（Astra Sky River 附近）
# =========================================================
PROPERTY_LAT = 18.7816
PROPERTY_LON = 99.0030

def distance_km(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))

def distance_label(km):
    if km < 1:
        return t("🚶 步行可达", "🚶 Walkable")
    elif km < 3:
        return t("🛺 5–10 分钟车程", "🛺 5–10 min ride")
    else:
        return t("🚕 需要打车", "🚕 Taxi / Grab")

# =========================================================
# 2️⃣ 天气逻辑（符合清迈）
# =========================================================
month = datetime.now().month
is_rainy_season = month in [5,6,7,8,9,10]

if is_rainy_season:
    st.info(
        t(
            "🌧 雨季（5–10 月）：几乎每天会下雨，夜市 & 室内活动更舒适。",
            "🌧 Rainy season (May–Oct): daily rain expected. Markets & indoor spots recommended."
        )
    )
else:
    st.success(
        t(
            "☀️ 旱季：天气稳定，非常适合夜市和户外活动。",
            "☀️ Dry season: stable weather, great for outdoor activities."
        )
    )

# =========================================================
# 3️⃣ 节庆活动（含 Yi Peng / 跨年高亮）
# =========================================================
festivals = [
    {
        "key": "yipeng",
        "Name_CN": "义蓬 & 水灯节（Yi Peng / Loy Krathong）",
        "Name_EN": "Yi Peng & Loy Krathong Festival",
        "Start": datetime(2025, 11, 5),
        "End": datetime(2025, 11, 6),
        "Brief_CN": "清迈一年中最重要的节日之一，古城及河边非常拥挤，建议提前规划交通。",
        "Brief_EN": "Chiang Mai’s most important festival. Expect heavy crowds; plan transport early.",
        "Highlight": True,
        "lat": 18.7877,
        "lon": 98.9933,
    },
    {
        "key": "countdown",
        "Name_CN": "清迈官方跨年夜",
        "Name_EN": "Chiang Mai Countdown",
        "Start": datetime(2025, 12, 28),
        "End": datetime(2026, 1, 1),
        "Brief_CN": "纳瓦拉桥一带大型跨年倒数与烟火活动。",
        "Brief_EN": "Official New Year countdown with fireworks at Nawarat Bridge.",
        "Highlight": True,
        "lat": 18.7879,
        "lon": 99.0045,
    },
]

st.subheader(t("🎉 重要节庆提醒", "🎉 Major Festival Alerts"))

today = datetime.now().date()
festival_found = False

for f in festivals:
    if f["Start"].date() - timedelta(days=3) <= today <= f["End"].date():
        festival_found = True
        with st.container(border=True):
            st.markdown(f"### 🔔 {t(f['Name_CN'], f['Name_EN'])}")
            st.write(t(f["Brief_CN"], f["Brief_EN"]))
            st.warning(
                t(
                    "⚠️ 节日期间交通拥堵，建议尽量步行或提前出发。",
                    "⚠️ Heavy traffic expected. Walking or early departure recommended."
                )
            )
            st.link_button(
                t("📍 查看主要区域", "📍 View Main Area"),
                f"https://www.google.com/maps?q={f['lat']},{f['lon']}"
            )

if not festival_found:
    st.info(
        t(
            "近期无大型节庆，可安心安排夜市与日常行程。",
            "No major festivals soon. Perfect time for markets & daily exploring."
        )
    )

# =========================================================
# 4️⃣ 夜市 / 市集（按距离排序）
# =========================================================
markets = [
    {
        "Name_CN": "长康路夜市（每日）",
        "Name_EN": "Night Bazaar (Daily)",
        "Brief_CN": "离房源最近，适合每天晚上散步。",
        "Brief_EN": "Closest market. Perfect for an easy evening walk.",
        "lat": 18.7850,
        "lon": 99.0001,
    },
    {
        "Name_CN": "周日步行街",
        "Name_EN": "Sunday Walking Street",
        "Brief_CN": "清迈最大夜市，每周日开放。",
        "Brief_EN": "Largest night market. Sunday evenings only.",
        "lat": 18.7877,
        "lon": 98.9933,
    },
    {
        "Name_CN": "Jing Jai 周末市集",
        "Name_EN": "Jing Jai Market",
        "Brief_CN": "白天市集，咖啡和手作很棒。",
        "Brief_EN": "Daytime market with great coffee & crafts.",
        "lat": 18.8073,
        "lon": 98.9955,
    },
]

# 计算距离并排序
for m in markets:
    m["distance"] = distance_km(PROPERTY_LAT, PROPERTY_LON, m["lat"], m["lon"])

markets.sort(key=lambda x: x["distance"])

st.subheader(t("🛍 房源附近夜市 & 市集", "🛍 Nearby Markets"))

for m in markets:
    with st.container(border=True):
        st.markdown(f"### {t(m['Name_CN'], m['Name_EN'])}")
        st.write(t(m["Brief_CN"], m["Brief_EN"]))
        st.caption(distance_label(m["distance"]))

        st.link_button(
            t("📍 Google 地图导航", "📍 Open in Google Maps"),
            f"https://www.google.com/maps?q={m['lat']},{m['lon']}"
        )

# ---------------- Footer ----------------
st.divider()
st.caption(
    t(
        "本指南为住客准备，祝你在清迈住得开心 🌿",
        "This guide is prepared for our guests. Enjoy your stay in Chiang Mai 🌿"
    )
)
