index_KHTN = [4,5,6]
index_KHXH = [7,8,9]

data_fix = []

with open("data_new.csv", "r", encoding="utf8") as file:
    data = file.readline()
    while(data != ""):
        if (data[0] == "0"):
            data = data.split(",")
            index = []
            check_KHTN = False
            check_KHXH = False
            cnt = 0
            cnt1 = 0
            for i in range(4,10):
                if (data[i] != '-1'):
                    cnt += 1
                    if (i in index_KHTN):
                        check_KHTN = True
                        break
                    if (i in index_KHXH):
                        check_KHXH = True
            for i in range(1,4):
                if (data[i] != '-1'):
                    cnt1 += 1

            s = data[0] + ","

            if (check_KHTN):
                s += "KHTN,"
            if (check_KHXH):
                s += "KHXH,"

            if (cnt + cnt1 == 9):
                s += "All,"
            
            for i in range(1,len(data)):
                s += data[i] + ","
            tmp = s.index("\n") 
            s = s[:tmp]  
            data_fix.append(s)
        data = file.readline()


with open("data_new_fix.csv", "a", encoding="utf8") as file:
    file.write("Số báo danh,Khối thi,Toán,Ngữ Văn,Ngoại Ngữ,Vật Lý,Hóa Học,Sinh Học,Lịch Sử,Địa Lý,GDCD\n")
    for i in data_fix:
        file.write(i + "\n")
