import pickle

ho_dict = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô",
    "Dương", "Lý", "Lương", "Đinh", "Trương", "Võ", "Đoàn", "Đào", "Hàn", "Cao", "Tạ", "Lưu", "Kim",
    "Hà", "Vương", "Trịnh", "Châu", "Đường", "Bạch", "Mạc", "Tô", "Triệu", "Phùng", "Giang", "Đông",
    "Đàm", "Phí", "Tăng", "Đổ", "Lục", "Vi", "Du", "Hứa", "Sơn", "Mai", "Lê", "Dư", "Tiêu", "Hồng",
    "Thái", "Cung", "Diệp", "Lỗ", "Mạnh", "Bành", "Tống", "Dương", "Bửu", "Ngụy", "Quách", "Phan",
    "Mai", "Khiết", "Cung", "Diệp", "Lạc", "Dương", "Bửu", "Đàm", "Trần", "Mạc", "Hồ", "Bình", "Chử",
    "Trọng", "Quách", "Lý", "Ninh", "Cầm", "Quyền", "Âu", "Hồ", "Chử", "Tào", "Đường", "Tưởng", "Nhạc",
    "Tạ", "Viên", "Đoàn", "Công", "Từ", "Phú", "Quyên", "Nghiêm", "Lương", "Vương"
]

ten_dict = [
    "An", "Anh", "Ban", "Bình", "Bích", "Băng", "Bạch", "Bảo", "Bằng", "Bội", "Ca", "Cam", "Chi", "Chinh",
    "Chiêu", "Chung", "Châu", "Cát", "Cúc", "Cương", "Cầm", "Cẩm", "Dao", "Di", "Diên", "Diễm", "Diệp",
    "Diệu", "Du", "Dung", "Duy", "Duyên", "Dân", "Dã", "Dương", "Dạ", "Gia", "Giang", "Giao", "Giáng",
    "Hiếu", "Hiền", "Hiểu", "Hiệp", "Hoa", "Hoan", "Hoài", "Hoàn", "Hoàng", "Hoạ", "Huyền", "Huệ", "Huỳnh",
    "Hà", "Hàm", "Hân", "Hòa", "Hương", "Hướng", "Hường", "Hưởng", "Hạ", "Hạc", "Hạnh", "Hải", "Hảo", "Hậu",
    "Hằng", "Họa", "Hồ", "Hồng", "Hợp", "Khai", "Khanh", "Khiết", "Khuyên", "Khuê", "Khánh", "Khê", "Khôi",
    "Khúc", "Khả", "Khải", "Kim", "Kiết", "Kiều", "Kê", "Kỳ", "Lam", "Lan", "Linh", "Liên", "Liễu", "Loan",
    "Ly", "Lâm", "Lê", "Lý", "Lăng", "Lưu", "Lễ", "Lệ", "Lộc", "Lợi", "Lục", "Mai", "Mi", "Minh", "Miên",
    "My", "Mẫn", "Mậu", "Mộc", "Mộng", "Mỹ", "Nga", "Nghi", "Nguyên", "Nguyết", "Nguyệt", "Ngà", "Ngân",
    "Ngôn", "Ngọc", "Nhan", "Nhi", "Nhiên", "Nhung", "Nhàn", "Nhân", "Nhã", "Nhơn", "Như", "Nhạn", "Nhất",
    "Nhật", "Nương", "Nữ", "Oanh", "Phi", "Phong", "Phúc", "Phương", "Phước", "Phượng", "Phụng", "Quyên",
    "Quân", "Quế", "Quỳnh", "Sa", "San", "Sao", "Sinh", "Song", "Sông", "Sơn", "Sương", "Thanh", "Thi",
    "Thiên", "Thiếu", "Thiều", "Thiện", "Thoa", "Thoại", "Thu", "Thuần", "Thuận", "Thy", "Thái", "Thêu",
    "Thông", "Thùy", "Thúy", "Thơ", "Thư", "Thương", "Thường", "Thạch", "Thảo", "Thắm", "Thục", "Thụy",
    "Thủy", "Tinh", "Tiên", "Tiểu", "Trang", "Tranh", "Trinh", "Triều", "Triệu", "Trung", "Trà", "Trâm",
    "Trân", "Trúc", "Trầm", "Tuyến", "Tuyết", "Tuyền", "Tuệ", "Ty", "Tâm", "Tùng", "Tùy", "Tú", "Túy",
    "Tường", "Tịnh", "Tố", "Từ", "Uyên", "Uyển", "Vi", "Vinh", "Việt", "Vy", "Vàng", "Vành", "Vân", "Vũ",
    "Vọng", "Vỹ", "Xuyến", "Xuân", "Yên", "Yến", "xanh", "Ái", "Ánh", "Ân", "Ðan", "Ðinh", "Ðiệp", "Ðoan",
    "Ðài", "Ðàn", "Ðào", "Ðình", "Ðông", "Ðường", "Ðồng", "Ý", "Đơn", "Đức", "Ấu"
]

street_dict = [
    "Nguyễn Huệ", "Lê Lợi", "Võ Văn Tần", "Trần Hưng Đạo", "Phạm Ngũ Lão", "Cao Thắng", "Tôn Thất Tùng",
    "Hoàng Sa", "Bùi Viện", "Điện Biên Phủ", "Nam Kỳ Khởi Nghĩa", "Lý Tự Trọng", "Lê Lai", "Hàm Nghi",
    "Trương Định", "Hai Bà Trưng", "Lê Thánh Tôn", "Đinh Tiên Hoàng", "Mạc Thị Bưởi", "Phan Văn Trị",
    "Lê Văn Sỹ", "Nguyễn Thị Minh Khai", "Đặng Văn Ngu", "Võ Thị Sáu", "Lý Thái Tổ", "Phan Chu Trinh",
    "Trần Quốc Toản", "Nguyễn Bỉnh Khiêm", "Nguyễn Trãi", "Lý Chính Thắng", "Nguyễn Đình Chiểu",
    "Nguyễn Văn Trỗi", "Lê Văn Thiêm", "Phố Đức Chính", "Hoàng Diệu", "Nguyễn Văn Cừ", "Trần Cao Vân",
    "Điện Biên Phủ", "Nguyễn Công Trứ", "Phạm Hồng Thái", "Cách Mạng Tháng Tám", "Đinh Tiên Hoàng",
    "Lê Hồng Phong", "Trần Phú", "Nam Quốc Cang", "Dương Bá Trạc", "Trần Hưng Đạo", "Phạm Ngọc Thạch",
    "Lý Thường Kiệt", "Trần Quý Khoách", "Cao Văn Lau", "Điện Biên Phủ", "Nguyễn Thái Bình",
    "Lê Thanh Tôn", "Ba Huyện Thanh Quan", "Võ Thị Sáu", "Lê Đại Hành", "Trần Nhân Tông", "Lý Tự Trọng",
    "Võ Văn Kiệt", "Trần Đình Xu", "Hồ Hảo Hớn", "Nguyễn Cư Trinh", "Bùi Thị Xuân", "Nguyễn Thị Diệu",
    "Trường Sa", "Võ Văn Tần", "Lê Văn Sỹ", "Bình Tây", "Võ Thị Sáu", "Nguyễn Biểu", "Lê Thị Hồng Gấm",
    "Kính Dương Vương", "Trần Bình Trọng", "Lê Hồng Phong", "Trần Hưng Đạo", "Phan Xích Long",
    "Nguyễn Thái Học", "Phạm Văn Đồng", "Hoàng Hoa Thám", "Nguyễn Văn Trỗi", "Lý Thái Tổ", "Phan Đình Phùng",
    "Nguyễn Thiện Thuật", "Trần Cao Vân", "Võ Thị Sáu", "Nam Kỳ Khởi Nghĩa", "Lê Văn Sỹ", "Hoàng Sa",
    "Nguyễn Công Trứ", "Phạm Hồng Thái", "Đặng Tất", "Bùi Thị Xuân", "Trường Sa", "Trần Quốc Thảo",
    "Lý Chính Thắng", "Nguyễn Thị Diệu", "Nguyễn Đình Chiểu", "Trần Quang Diệu", "Điện Biên Phủ",
    "Nguyễn Thái Bình", "Lý Tự Trọng", "Phố Đức Chính", "Nguyễn Biểu", "Nguyễn Công Trứ", "Bạch Đằng",
    "Trần Đình Xu", "Cao Văn Lau"
]

truong_dict = [
    "THPT Bùi Thị Xuân", "THPT Trưng Vương", "THPT Giồng Ông Tố", "THPT Nguyễn Thị Minh Khai", "THPT Lê Quý Đôn",
    "THPT Nguyễn Trãi", "Phổ thông Năng khiếu thể thao Olympic", "THPT Hùng Vương", "THPT Mạc Đĩnh Chi",
    "THPT Bình Phú", "THPT Lê Thánh Tôn", "THPT Lương Văn Can", "THPT Ngô Gia Tự", "THPT Tạ Quang Bửu",
    "THPT Nguyễn Huệ", "THPT Nguyễn Khuyến", "THPT Nguyễn Du", "THPT Nguyễn Hiền", "THPT Võ Trường Toản",
    "THPT Thanh Đa", "THPT Võ Thị Sáu", "THPT Gia Định", "THPT Phan Đăng Lưu", "THPT Gò Vấp",
    "THPT Nguyễn Công Trứ", "THPT Phú Nhuận", "THPT Tân Bình", "THPT Nguyễn Chí Thanh", "THPT Trần Phú",
    "THPT Nguyễn Thượng Hiền", "THPT Thủ Đức", "THPT Nguyễn Hữu Huân", "THPT Tam Phú", "THPT Củ Chi",
    "THPT Quang Trung", "THPT An Nhơn Tây", "THPT Trung Phú", "THPT Trung Lập", "THPT Nguyễn Hữu Cầu",
    "THPT Lý Thường Kiệt", "THPT Bình Chánh", "THPT Ten Lơ Man", "THPT Marie Curie", "THPT Trần Khai Nguyên",
    "THPT Nguyễn An Ninh", "THPT Nam Kỳ Khởi Nghĩa", "THPT Nguyễn Thái Bình", "THPT Nguyễn Trung Trực",
    "THPT Hàn Thuyên", "THPT Hoàng Hoa Thám", "THPT Thăng Long", "THPT Phước Long", "THPT Bà Điểm",
    "THPT Tân Phong", "THPT Trường Chinh", "THPT Phú Hòa", "THPT Tân Thông Hội", "THPT Tây Thạnh",
    "THPT Long Trường", "THPT Nguyễn Văn Cừ", "THPT Nguyễn Hữu Tiến", "THPT Bình Khánh", "THPT Cần Thạnh",
    "THPT Trần Hưng Đạo", "THPT Hiệp Bình", "Tiểu học THCS và THPT Quốc Văn Sài Gòn", "THPT Trần Quang Khải",
    "THPT Vĩnh Lộc", "THPT Việt Âu", "THPT Việt Nhật", "THPT Hưng Đạo", "TH - THCS - THPT Chu Văn An",
    "Trung học Thực hành Đại học Sư phạm", "Phổ thông Năng Khiếu - ĐHQG Tp. HCM", "THPT Lý Thái Tổ",
    "THPT Trần Quốc Tuấn", "THPT An Dương Vương", "THPT Trần Nhân Tông", "THPT Đông Dương", "THPT Phước Kiển",
    "THPT Nhân Việt", "THPT An Nghĩa", "THPT Phú Lâm", "Trung học cơ sở và trung học phổ thông Phùng Hưng",
    "THPT Nguyễn Hữu Cảnh", "THPT Nguyễn Văn Linh", "Phân hiệu THPT Lê Thị Hồng Gấm", "THPT Nguyễn Thị Diệu",
    "THPT Quốc Trí", "THPT Vĩnh Viễn", "THCS - THPT Trần Cao Vân", "THPT Bách Việt", "THPT Việt Mỹ Anh",
    "THCS và THPT Nam Việt", "THPT Văn Lang", "THPT Bình Hưng Hòa", "THPT Bình Tân", "THPT Nguyễn Tất Thành",
    "THPT Nguyễn Văn Tăng",  "THPT Năng khiếu TDTT Huyện Bình Chánh", "THPT Lê Trọng Tấn", "THPT Linh Trung",
    "THPT Dương Văn Thì", "THPT Bình Chiểu", "THPT Hồ Thị Bi", "THPT Phong Phú", "THPT Thủ Thiêm", "THPT Ngô Quyền",
    "THPT Thạnh Lộc", "THPT An Lạc", "THPT Lê Minh Xuân", "THPT Đa Phước",  "THPT Nam Sài Gòn", "THPT Đông Đô",
    "TH THCS THPT Tuệ Đức (2)", "THPT chuyên Lê Hồng Phong", "THPT chuyên Trần Đại Nghĩa", "TH - THCS - THPT VẠN HẠNH",
    "THPT Chuyên Năng khiếu TDTT Nguyễn Thị Định"
]

Dictionaries = {
    "ho_dict": ho_dict,
    "ten_dict": ten_dict,
    "street_dict": street_dict,
    "truong_dict": truong_dict
}

with open("Dictionaries.pkl", "wb") as file:
    pickle.dump(Dictionaries, file)
