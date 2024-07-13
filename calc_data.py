import pandas as pd

data = pd.read_csv('D:/Data_Analysis/data_new.csv')

with open("data1.csv", "w", encoding="utf8") as file:
    file.write("Môn thi,Số lượng thí sinh\n")

with open("data2.csv", "w", encoding="utf8") as file_:
    file_.write("Môn thi,Số lượng thí sinh\n")

subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa Lý","GDCD"]
ans = []
no_test = []

for i in subject:
    tmp = list(data[i])
    total_zero = tmp.count(1.0)    

    with open("data1.csv", "a", encoding="utf8") as file1:
        tmp = str(i) + "," + str(len(tmp) - total_zero) + "\n"
        file1.write(tmp)

    with open("data2.csv", "a", encoding="utf8") as file1_:
        tmp1 = str(i) + "," + str(total_zero) + "\n"
        file1_.write(tmp1)