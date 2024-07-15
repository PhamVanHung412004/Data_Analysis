import streamlit as st
import pandas as pd
import plotly.express as px

# Tạo một DataFrame ví dụ
data = {
    'Môn học': ['Toán', 'Vật lý', 'Hóa học', 'Sinh học', 'Lịch sử'],
    'Điểm trung bình': [7.8, 8.5, 7.2, 8.0, 6.9]
}
df = pd.DataFrame(data)

# Vẽ biểu đồ cột với Plotly Express
fig = px.bar(df, x='Môn học', y='Điểm trung bình', text='Điểm trung bình', color='Môn học',
             labels={'Điểm trung bình': 'Điểm trung bình', 'Môn học': 'Môn học'},
             title='Điểm trung bình mỗi môn học')

# Điều chỉnh layout của biểu đồ
fig.update_layout(xaxis_title='Môn học', yaxis_title='Điểm trung bình')

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)

# Hiển thị DataFrame nếu cần
st.write(df)
