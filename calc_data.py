import pandas as pd


def binray_search(arr,x):
    l = 0
    r = len(arr) - 1
    while(l <= r):
        mid = int((l + r)/2)
        if (arr[mid] == x):
            return True
        elif (arr[mid] < x):
            l = mid + 1
        else:
            r = mid - 1
    return False

data1 = pd.read_csv('D:/Data_Analysis/data_new_fix.csv')
subject = ["Toán","Ngữ Văn","Ngoại Ngữ","Vật Lý","Hóa Học","Sinh Học","Lịch Sử","Địa Lý","GDCD"]
ans = []
count_subject = [0] * 9
dx = [_ for _ in range(2,11)]

with open("D:/Data_Analysis/data_new_fix.csv" , "r" ,encoding="utf8") as fi:
    data = fi.readline()
    while(data != ""):
        if (data[0] == "0"):
            counts = 0
            total_subject = 0
            data = data.split(",")
            for i in range(len(dx)):
                if (data[dx[i]] != "-1"):
                    counts += 1
                    # total_subject += float(data[dx[i]])
            count_subject[counts] += 1
        data = fi.readline()


# with open("dt3.csv" , "w", encoding="utf8") as file111:
#     file111.write("nhóm,tần suất\n")

# with open("dt3.csv", "a", encoding="utf8") as file1111:
#     for i in range(len(count_subject)):
#         file1111.write(str(i) + " môn," + str(count_subject[i]) + "\n")