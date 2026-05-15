import streamlit as st
import plotly.graph_objects as go
import numpy as np

# 1. إعدادات الصفحة والاتجاه من اليمين (RTL)
st.set_page_config(page_title="عرض المسابقة - خلود", layout="wide")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], .main {
        direction: rtl !important;
        text-align: right !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. العنوان الرئيسي
st.markdown("<h1 style='text-align: center;'>النمذجة البصرية لأسطح ريمان</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>قسم الرياضيات - جامعة مصراتة</p>", unsafe_allow_html=True)

# 3. الرسمة الأولى
st.markdown("<h2 style='text-align: right; color: #000080;'>1. سطح ريمان لدالة الجذر التربيعي</h2>", unsafe_allow_html=True)

# --- كود رسمة الجذر هنا (الذي كان عندك سابقاً) ---
r1 = np.linspace(0, 2, 50)
theta1 = np.linspace(0, 4 * np.pi, 100)
r1, theta1 = np.meshgrid(r1, theta1)
x1 = r1 * np.cos(theta1)
y1 = r1 * np.sin(theta1)
z1 = np.sqrt(r1) * np.sin(theta1/2)
fig1 = go.Figure(data=[go.Surface(x=x1, y=y1, z=z1, colorscale='Portland')])
st.plotly_chart(fig1, use_container_width=True)

# 4. الفاصل بين الدالتين
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# 5. الرسمة الثانية
st.markdown("<h2 style='text-align: right; color: #000080;'>2. سطح ريمان لدالة اللوغاريتم</h2>", unsafe_allow_html=True)

# --- كود رسمة اللوغاريتم هنا ---
r2 = np.linspace(0.1, 2, 50)
theta2 = np.linspace(0, 4 * np.pi, 100)
r2, theta2 = np.meshgrid(r2, theta2)
x2 = r2 * np.cos(theta2)
y2 = r2 * np.sin(theta2)
z2 = theta2 
fig2 = go.Figure(data=[go.Surface(x=x2, y=y2, z=z2, colorscale='Viridis')])
st.plotly_chart(fig2, use_container_width=True)

# 6. التذييل (الاسم)
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 14px;'>إعداد الطالبة: خلود</p>", unsafe_allow_html=True)
