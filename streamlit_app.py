import streamlit as st
import openai
from datetime import datetime

# 🔐 SETUP OpenAI KEY (ใส่ Key จริงของคุณ)
openai.organization = "org-GELun61bLnDGutYVF1OIe9Pc"
openai.api_key = "sk-Gm-7fUM-TkSdeJQAUNcYKLw7LE-_hT0Mrmq-4pAhjJT3BlbkFJ7dupKD-NLCbp2qV5m359wUCnHr3o9yUWI475eGQEwA"

# --- UI
st.title("🔮 วิเคราะห์ดวงจีน BaZi (GPT Edition)")

birth_date = st.date_input("📅 วันเกิด")
birth_time = st.time_input("⏰ เวลาเกิด")
gender = st.selectbox("เพศ", ["ชาย", "หญิง"])

# --- เสา 4 หลัก (จำลองเฉพาะตอนนี้)
pillars = {
    "ปี": ("戊", "午"),
    "เดือน": ("辛", "酉"),
    "วัน": ("乙", "亥"),
    "เวลา": ("乙", "酉")
}
day_master = pillars["วัน"][0]  # '乙'

# --- GPT: คำถามวิเคราะห์
def ask_gpt(day_master, gender):
    prompt = f"""
คุณคือซินแสผู้เชี่ยวชาญดวงจีน โปรดวิเคราะห์ดวงตามธาตุดิถี {day_master} สำหรับเพศ {gender}
โดยอิงจากปี 2025 (乙巳年) สรุปผลให้ 3 หัวข้อ:

1. ความรัก
2. การเงิน
3. สุขภาพ

พร้อมคำแนะนำเสริมดวงเบื้องต้นด้วย
ตอบเป็นภาษาที่เข้าใจง่ายแบบสรุป
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "คุณคือซินแสผู้เชี่ยวชาญดวงจีน"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- ปุ่มขอคำทำนาย
if st.button("🔍 วิเคราะห์ดวงด้วย GPT"):
    with st.spinner("กำลังเรียก GPT วิเคราะห์..."):
        result = ask_gpt(day_master, gender)
        st.subheader("🧠 คำทำนายโดย GPT:")
        st.markdown(result)
