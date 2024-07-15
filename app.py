import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa Lý","GDCD"]

csv_file_path = 'data_new_fix.csv'
st.title("Điểm thi tốt nghiệp năm 2022 trên địa bàn thành phố Hà Nội")
st.write("Lưu ý là số báo danh bắt đầu bằng 0 ví dụ số báo danh trong file csv hiển thi là 1000001 thì số báo danh thật thêm số 0 đằng trước thành 01000001.")
df = pd.read_csv(csv_file_path)

df['Số báo danh'] = df['Số báo danh'].astype(str)
df.insert(0, 'STT', range(1, len(df) + 1))

st.write("Dữ liệu từ tệp CSV:")
st.dataframe(df)

st.write("Thống kê tóm tắt:")
st.write(df.describe())

st.write("5 hàng đầu tiên:")
st.write(df.head())

st.title("Biểu đồ cột")

file_path = "D:/Data_Analysis/dt1.csv"
file_path1 = "D:/Data_Analysis/dt2.csv"

dt1 = pd.read_csv(file_path)
dt2 = pd.read_csv(file_path1)
# # Extract the relevant columns
subjects = dt1['Môn thi']
attendees = dt1['Số lượng thí sinh']

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(subjects, attendees, color='skyblue')
ax.set_xlabel('Môn thi')
ax.set_ylabel('Số lượng thí sinh')
plt.title('Số Lượng Thí Sinh Theo Môn Thi')
ax.set_xticklabels(subjects, rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Display the plot in Streamlit
st.pyplot(fig)

# Observations
max_students = dt1['Số lượng thí sinh'].max()
min_students = dt1['Số lượng thí sinh'].min()
most_popular_subject = dt1[dt1['Số lượng thí sinh'] == max_students]['Môn thi'].values[0]
least_popular_subject = dt1[dt1['Số lượng thí sinh'] == min_students]['Môn thi'].values[0]

st.write(f"Số lượng thí sinh nhiều nhất: {max_students} (Môn {most_popular_subject})")
st.write(f"Số lượng thí sinh ít nhất: {min_students} (Môn {least_popular_subject})")

st.write("""
Phân tích:
- Môn học có số lượng thí sinh nhiều nhất là Toán với 95332 thí sinh, cho thấy đây là môn học phổ biến và quan trọng.
- Môn học có số lượng thí sinh ít nhất là Vật Lý với 26022 thí sinh, cho thấy sự quan tâm đối với môn học này ít hơn so với các môn khác.
""")

subjects = dt2['Môn thi']
attendees = dt2['Số lượng thí sinh không đi thi']

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(subjects, attendees, color='skyblue')
ax.set_xlabel('Môn thi')
ax.set_ylabel('Số lượng thí sinh không đi thi')
plt.title('Số Lượng Thí Sinh Không Đi Thi Theo Môn')
ax.set_xticklabels(subjects, rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Display the plot in Streamlit
st.pyplot(fig)

# Observations
max_students = dt2['Số lượng thí sinh không đi thi'].max()
min_students = dt2['Số lượng thí sinh không đi thi'].min()
most_popular_subject = dt2[dt2['Số lượng thí sinh không đi thi'] == max_students]['Môn thi'].values[0]
least_popular_subject = dt2[dt2['Số lượng thí sinh không đi thi'] == min_students]['Môn thi'].values[0]

st.write(f"Số lượng thí sinh không đi thi nhiều nhất: {max_students} (Môn {most_popular_subject})")
st.write(f"Số lượng thí sinh không đi thi ít nhất: {min_students} (Môn {least_popular_subject})")


file_ = "dt1.csv"

data_ = pd.read_csv(file_)

not_exam = list(data_["Số lượng thí sinh"])
dtb = list(data_["Số lượng thí sinh"])
total = sum(dtb)

for i in range(len(dtb)):
    dtb[i] = round((dtb[i]/total) * 100,2)

fig, ax = plt.subplots()

y_pos = np.arange(len(subject))
x_pos = np.arange(len(subject))

# performance = [10,8,6,4,2,1]

plt.bar(y_pos, dtb, align='center', alpha=0.5)
plt.xticks(y_pos, subject)
plt.plot(x_pos, dtb, color='red', marker='o')

ax.set_ylim(0,70)
plt.ylabel('Phần trăm')
plt.title('Thống kê điểm trung bình mỗi môn') 

# make value
rects = ax.patches
for rect, label in zip(rects, not_exam):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )

st.pyplot(fig)
# # plt.show()

for i in range(len(subject)):
    # tmp = list(data11[])
    st.title("Phổ điểm môn " + subject[i])
    file_path1 = 'phodiemmon' + str(subject[i]) + '.csv'
    data11 = pd.read_csv(file_path1)

    fig, ax = plt.subplots()
    bars = sns.barplot(x='Điểm', y='Tần suất', data=data11, ax=ax, color='skyblue')
    ax.set_title('Biểu đồ hình cột')
    ax.set_xlabel('Điểm')
    ax.set_ylabel('Số lần xuất hiện')
    plt.xticks(rotation=90)
    st.pyplot(fig)
