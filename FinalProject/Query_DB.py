import os
import time
import mysql.connector
import xml.etree.ElementTree as ET
import xml.dom.minidom

# Nhập thông tin đăng nhập MySQL của bạn
print("Nhập thông tin đăng nhập MySQL của bạn")
_host = input("Host: ")
_user = input("User: ")
_password = input("Password: ")

# Tạo Thư mục nếu chưa tồn tại
folder_path = input("Nhập đường dẫn đến Folder chứa các file XML: ")
os.makedirs(folder_path, exist_ok=True)


def query_HocSinh(database_name, tentruong, namhoc, xeploai):
    # Kết nối tới database
    cnx = mysql.connector.connect(
        host=_host,
        user=_user,
        password=_password,
        database=database_name
    )
    cursor = cnx.cursor()

    # Đo thời gian truy vấn
    start_time = time.time()

    # Truy vấn dữ liệu
    query = f"""
        SELECT  CONCAT_WS(' ',B.HO, B.TEN) AS HOTEN, B.NTNS, C.DIEMTB, C.XEPLOAI, C.KQUA
        FROM    TRUONG A, HS B, HOC C
        WHERE   A.TENTR = "{tentruong}" AND C.NAMHOC = {namhoc} AND C.XEPLOAI = "{xeploai}" AND A.MATR = C.MATR AND B.MAHS = C.MAHS;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Tính thời gian truy vấn
    query_time = time.time() - start_time

    # In danh sách học sinh
    for row in results:
        HOTEN, NTNS, DIEMTB, XEPLOAI, KQUA = row
        print("Họ tên học sinh:", HOTEN)
        print("Ngày tháng năm sinh:", NTNS)
        print("Điểm trung bình:", DIEMTB)
        print("Xếp loại học tập:", XEPLOAI)
        print("Kết quả:", KQUA)
        print("----------------------------")

    # Tạo tên file XML theo quy ước
    file_name = f"{database_name}-{tentruong}-{namhoc}-{xeploai}.xml"

    # Tạo root của XML
    root = ET.Element("DanhSachHocSinh")
    for row in results:
        hs = ET.SubElement(root, "HocSinh")
        HOTEN, NTNS, DIEMTB, XEPLOAI, KQUA = row
        ET.SubElement(hs, "HoTen").text = HOTEN
        ET.SubElement(hs, "NgaySinh").text = str(NTNS)
        ET.SubElement(hs, "DiemTB").text = str(DIEMTB)
        ET.SubElement(hs, "XepLoai").text = XEPLOAI
        ET.SubElement(hs, "KetQua").text = KQUA

    tree = ET.ElementTree(root)

    # Tạo một chuỗi để giữ XML được định dạng
    xml_string = ET.tostring(root, encoding="utf-8")

    # Tạo một đối tượng XML được phân tích cú pháp
    parsed_xml = xml.dom.minidom.parseString(xml_string)

    # Lấy chuỗi XML đã định dạng
    formatted_xml = parsed_xml.toprettyxml(indent="    ")

    # Ghi XML đã định dạng vào tệp
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(formatted_xml)

    # Đóng kết nối database
    # conn.close()
    cursor.close()
    cnx.close()

    # Trả về thời gian truy vấn
    return query_time


# Sử dụng chức năng
database1_name = "TRUONGHOC1"
database2_name = "TRUONGHOC2"
tentruong = input("Nhập tên trường: ")
namhoc = input("Nhập năm học: ")
xeploai = input("Nhập xếp loại: ")

# Xuất kết quả
print("-------------------------------")
print("| Kết quả truy vấn TRUONGHOC1 |")
print("-------------------------------")
query_time1 = query_HocSinh(database1_name, tentruong, int(namhoc), xeploai)
print()
print()
print("-------------------------------")
print("| Kết quả truy vấn TRUONGHOC2 |")
print("-------------------------------")
query_time2 = query_HocSinh(database2_name, tentruong, int(namhoc), xeploai)
print("Thời gian truy vấn TRUONGHOC1:", query_time1, "giây")
print("Thời gian truy vấn TRUONGHOC2:", query_time2, "giây")
