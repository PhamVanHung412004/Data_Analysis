import streamlit as st
import pandas as pd
import plotly.express as px

csv_file_path = 'D:/Data_Analysis/data_new.csv'

st.title("Điểm thi tốt nghiệp năm 2022 trên địa bàn thành phố Hà Nội")

df = pd.read_csv(csv_file_path)

df['Số báo danh'] = df['Số báo danh'].astype(str)
df.insert(0, 'STT', range(1, len(df) + 1))

st.write("Dữ liệu từ tệp CSV:")
st.dataframe(df)

st.write("Thống kê tóm tắt:")
st.write(df.describe())

st.write("5 hàng đầu tiên:")
st.write(df.head())

path_calc_data = "D:/Data_Analysis/data1.csv"

data = pd.read_csv(path_calc_data)

st.title("Biểu đồ cột")
fig = px.bar(data, x='Môn thi', y='Số lượng thí sinh')
st.plotly_chart(fig)

path_data2 = "D:/Data_Analysis/data2.csv"
data1 = pd.read_csv(path_data2)

# Tiêu đề của ứng dụng
st.title('Biểu đồ hình tròn')

# Biểu đồ hình tròn
fig = px.pie(data1 , values='Số lượng thí sinh', names='Môn thi')
st.plotly_chart(fig)
