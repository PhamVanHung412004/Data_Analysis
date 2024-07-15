dx = [2,3,4,5,6,7,8,9,10]
coutns = [0] * len(dx)
coutns_ = [0] * len(dx)
subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa Lý","GDCD"]
with open("data_new_fix.csv", "r", encoding="utf8") as file:
    data = file.readline()
    while (data != ""):
        if (data[0] == "0"):
            data = data.split(",")
            
            for i in range(0,3):
                if (data[dx[i]] != '-1'):
                    coutns[i] += 1
                else:
                    coutns_[i] += 1  

            if (data[1] == "KHTN"):
                for i in range(3,6):
                    if (data[dx[i]] != '-1'):
                        coutns[i] += 1
                    else:
                        coutns_[i] += 1             
            else:
                for i in range(6,9):
                    if (data[dx[i]] != '-1'):
                        coutns[i] += 1
                    else:
                        coutns_[i] += 1                 
        data = file.readline()

with open("dt1.csv", "a", encoding="utf8") as file1:
    file1.write("Môn thi,Số lượng thí sinh\n")
    for i in range(len(subject)):
        file1.write(subject[i] + "," + str(coutns[i]) + "\n")

with open("dt2.csv", "a", encoding="utf8") as file2:
    file2.write("Môn thi,Số lượng thí sinh\n")
    for i in range(len(subject)):
        file2.write(subject[i] + "," + str(coutns_[i]) + "\n")

# print(coutns)
# print(coutns_)