%%writefile app.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# إعدادات صفحة مشروع التخرج
st.set_page_config(page_title="مشروع التخرج - خلود", layout="wide")
st.title("النمذجة البصرية لأسطح ريمان")
st.write("قسم الرياضيات - جامعة مصراتة")

# حسابات سطح ريمان (دالة الجذر كمثال مبهر)
r = np.linspace(0, 2, 50)
theta = np.linspace(0, 4*np.pi, 100)
r, theta = np.meshgrid(r, theta)

x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.sqrt(r) * np.sin(theta/2)

# إنشاء السطح التفاعلي
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Portland', opacity=0.9)])

fig.update_layout(
    title='تمثيل سطح ريمان للدالة الجذرية 3D',
    scene=dict(
        xaxis_title='Re(z)',
        yaxis_title='Im(z)',
        zaxis_title='Im(f(z))'
    )
)

st.plotly_chart(fig, use_container_width=True)
