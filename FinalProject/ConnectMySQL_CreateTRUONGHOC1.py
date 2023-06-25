import mysql.connector

# Nhập thông tin đăng nhập MySQL của bạn
print("Nhập thông tin đăng nhập MySQL của bạn")
_host = input("Host: ")
_user = input("User: ")
_password = input("Password: ")

# Kết nối với cơ sở dữ liệu MySQL
conn = mysql.connector.connect(
    host=_host,
    user=_user,
    password=_password
)
cursor = conn.cursor()

file_path_CreateSchema1 = input("Nhập đường dẫn đến tệp CreateSchema1.sql: ")

# Đọc và thực thi các câu lệnh MySQL từ tệp CreateSchema1.sql
with open(file_path_CreateSchema1, 'r') as file:
    sql_statement = file.read().split(';')
    for statement in sql_statement:
        cursor.execute(statement)

# Commit các thay đổi vào cơ sở dữ liệu
conn.commit()

# Đóng kết nối cơ sở dữ liệu
cursor.close()
conn.close()
