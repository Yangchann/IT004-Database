from lxml import etree


def get_students_within_threshold(xml_file_path, low_threshold, high_threshold):
    # Đọc file XML
    tree = etree.parse(xml_file_path)

    # Xây dựng XPath query để lấy danh sách học sinh trong ngưỡng điểm
    xpath_query = f"//HocSinh[DiemTB >= {low_threshold} and DiemTB <= {high_threshold}]"

    # Truy vấn danh sách học sinh
    students = tree.xpath(xpath_query)

    return students


def print_student_info(student):
    ho_ten = student.findtext("HoTen")
    ngay_sinh = student.findtext("NgaySinh")
    diem_tb = student.findtext("DiemTB")
    xep_loai = student.findtext("XepLoai")
    ket_qua = student.findtext("KetQua")

    print("---------------------")
    print("Ho ten:", ho_ten)
    print("Ngay sinh:", ngay_sinh)
    print("Diem TB:", diem_tb)
    print("Xep loai:", xep_loai)
    print("Ket qua:", ket_qua)


# Đường dẫn tới file XML cần đọc
xml_file_path = input("Nhập đường dẫn file xml: ")

# Ngưỡng điểm
low_threshold = input("Nhập ngưỡng điểm thấp: ")
high_threshold = input("Nhập ngưỡng điểm cao: ")

# Lấy danh sách học sinh trong ngưỡng điểm
students_within_threshold = get_students_within_threshold(
    xml_file_path, low_threshold, high_threshold)

# In danh sách học sinh
for student in students_within_threshold:
    print_student_info(student)
