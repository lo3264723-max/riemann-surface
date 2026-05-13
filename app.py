import streamlit as st
import plotly.graph_objects as go
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="عرض المسابقة - خلود", layout="wide")

st.title("النمذجة البصرية لأسطح ريمان")
st.write("قسم الرياضيات - جامعة مصراتة")

# --- الرسمة الأولى: دالة الجذر ---
st.header("1. سطح ريمان لدالة الجذر التربيعي")
r1 = np.linspace(0, 2, 50)
theta1 = np.linspace(0, 4 * np.pi, 100)
r1, theta1 = np.meshgrid(r1, theta1)
x1 = r1 * np.cos(theta1)
y1 = r1 * np.sin(theta1)
z1 = np.sqrt(r1) * np.sin(theta1/2)

fig1 = go.Figure(data=[go.Surface(x=x1, y=y1, z=z1, colorscale='Portland')])
st.plotly_chart(fig1, use_container_width=True)

st.write("---") # خط فاصل بين الرسمتين

# --- الرسمة الثانية: دالة جديدة (مثلاً اللوغاريتم) ---
st.header("2. سطح ريمان لدالة اللوغاريتم الطبيعي")
r2 = np.linspace(0.1, 2, 50) # نبدأ من 0.1 لأن لوغاريتم الصفر غير معرف
theta2 = np.linspace(0, 4 * np.pi, 100)
r2, theta2 = np.meshgrid(r2, theta2)
x2 = r2 * np.cos(theta2)
y2 = r2 * np.sin(theta2)
z2 = theta2 # تمثيل الجزء التخيلي للوغاريتم اللي يعطي شكل الحلزون

fig2 = go.Figure(data=[go.Surface(x=x2, y=y2, z=z2, colorscale='Viridis')])
st.plotly_chart(fig2, use_container_width=True)
