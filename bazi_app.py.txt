import streamlit as st
from datetime import datetime

st.title("🔮 วิเคราะห์ดวงจีน BaZi (ต้นแบบ)")

# --- Input
birth_date = st.date_input("📅 วันเกิด")
birth_time = st.time_input("⏰ เวลาเกิด")
gender = st.selectbox("เพศ", ["ชาย", "หญิง"])

# --- Process (Mock BaZi Conversion)
def mock_4pillars():
    return {
        "ปี": ("戊", "午"),
        "เดือน": ("辛", "酉"),
        "วัน": ("乙", "亥"),
        "เวลา": ("乙", "酉")
    }

pillars = mock_4pillars()
day_master = pillars["วัน"][0]  # '乙'

# --- Analysis
favorable = ["น้ำ", "ไม้"] if day_master == "乙" else ["ไฟ"]
unfavorable = ["ทอง"] if day_master == "乙" else ["น้ำ"]

# --- Output
st.subheader("🔎 ผลการวิเคราะห์เบื้องต้น:")
st.markdown(f"""
- **ธาตุดิถี**: `{day_master}`
- **ธาตุเกื้อหนุน**: `{', '.join(favorable)}`
- **ธาตุควรหลีกเลี่ยง**: `{', '.join(unfavorable)}`
""")
