import random
import pickle
import mysql.connector
from unidecode import unidecode

# Nhập thông tin đăng nhập MySQL của bạn
print("Nhập thông tin đăng nhập MySQL của bạn")
_host = input("Host: ")
_user = input("User: ")
_password = input("Password: ")

# Tạo kết nối tới cơ sở dữ liệu MySQL
cnx1 = mysql.connector.connect(
    host=_host,
    user=_user,
    password=_password,
    database="TRUONGHOC1"
)
cursor1 = cnx1.cursor()

cnx2 = mysql.connector.connect(
    host=_host,
    user=_user,
    password=_password,
    database="TRUONGHOC2"
)
cursor2 = cnx2.cursor()

# Mở file từ điển Dictionaries.pkl để load vào Dictionaries và sử dụng
with open("Dictionaries.pkl", "rb") as file:
    Dictionaries = pickle.load(file)

#  ho_dict là từ điển chứa các họ
ho_dict = Dictionaries["ho_dict"]

# ten_dict là từ điển chứa các tên
ten_dict = Dictionaries["ho_dict"]

# street_dict là từ điển chứa các tên đường
street_dict = Dictionaries["street_dict"]

# truong_dict là từ điển chứa các tên trường
truong_dict = Dictionaries["truong_dict"]

# Hàm tạo dữ liệu Trường


def generate_truong_data(num_truong):
    truong_data = []
    for i in range(num_truong):
        matr = "MT" + str(i + 1).zfill(4)
        tentr = unidecode(truong_dict[i])
        dchitr = f"{random.randint(1, 999)}, {unidecode(random.choice(street_dict))}, Quan {random.randint(1, 12)}, TP HCM"
        truong = (matr, tentr, dchitr)
        truong_data.append(truong)
    return truong_data

# Hàm tạo dữ liệu Học sinh


def generate_hs_data(num_hs):
    hs_data = []
    cccd_set = set()  # Tập hợp để lưu trữ các số cccd đã được sử dụng
    for i in range(num_hs):
        mahs = "2252" + str(i + 1).zfill(7)
        ho = unidecode(random.choice(ho_dict))
        ten = unidecode(random.choice(ten_dict))
        # Random số cccd không trùng
        cccd = str(random.randint(100000000, 999999999))
        while cccd in cccd_set:
            cccd = str(random.randint(100000000, 999999999))
        cccd_set.add(cccd)
        ntns = f"2004-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        dchi_hs = f"{random.randint(1, 999)}, {unidecode(random.choice(street_dict))}, Quan {random.randint(1, 12)}, TP HCM"
        hs = (mahs, ho, ten, cccd, ntns, dchi_hs)
        hs_data.append(hs)
    return hs_data

# Hàm tạo dữ liệu Hoc


def generate_hoc_data(hs_data, truong_data):
    hoc_data = []
    for hs in hs_data:
        mahs = hs[0]
        matr = random.choice(truong_data)
        for namhoc in [2020, 2021, 2022]:
            diemtb = round(random.uniform(0, 10), 2)
            if diemtb >= 9:
                xeploai = "Xuat sac"
                kqua = "Hoan thanh"
            elif diemtb >= 8:
                xeploai = "Gioi"
                kqua = "Hoan thanh"
            elif diemtb >= 6.5:
                xeploai = "Kha"
                kqua = "Hoan thanh"
            elif diemtb >= 5:
                xeploai = "Trung binh"
                kqua = "Chua hoan thanh"
            else:
                xeploai = "Yeu"
                kqua = "Chua hoan thanh"
            hoc = (matr[0], mahs, namhoc, diemtb, xeploai, kqua)
            hoc_data.append(hoc)
    return hoc_data


# Tạo dữ liệu cho bảng TRUONG
truong_data = generate_truong_data(100)
for truong in truong_data:
    query = f"INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES ('{truong[0]}', '{truong[1]}', '{truong[2]}')"
    cursor1.execute(query)
    cursor2.execute(query)

# # Tạo dữ liệu cho bảng HS
hs_data = generate_hs_data(1000000)
for hs in hs_data:
    query = f"INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES ('{hs[0]}', '{hs[1]}', '{hs[2]}', '{hs[3]}', '{hs[4]}', '{hs[5]}')"
    cursor1.execute(query)
    cursor2.execute(query)

# Tạo dữ liệu cho bảng HOC
hoc_data = generate_hoc_data(hs_data, truong_data)
for hoc in hoc_data:
    query = f"INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES ('{hoc[0]}', '{hoc[1]}', '{hoc[2]}', '{hoc[3]}', '{hoc[4]}', '{hoc[5]}')"
    cursor1.execute(query)
    cursor2.execute(query)

# Lưu thay đổi vào cơ sở dữ liệu
cnx1.commit()
cnx2.commit()

# Đóng kết nối
cursor1.close()
cnx1.close()
cursor2.close()
cnx2.close()
