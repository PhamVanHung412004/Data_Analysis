import streamlit as st
import pandas as pd

# Đường dẫn đến tệp CSV của bạn
csv_file_path = 'data_new.csv'

# Tiêu đề của ứng dụng
st.title("Điểm thi tốt nghiệp năm 2022 trên địa bàn thành phố Hà Nội")


# Đọc tệp CSV
df = pd.read_csv(csv_file_path)
df['Số báo danh'] = df['Số báo danh'].astype(str)
df.insert(0, 'STT', range(1, len(df) + 1))

# Hiển thị dataframe
st.write("Dữ liệu từ tệp CSV:")
st.dataframe(df)

# Hiển thị thông tin bổ sung (tùy chọn)
st.write("Thống kê tóm tắt:")
st.write(df.describe())

st.write("5 hàng đầu tiên:")
st.write(df.head())
