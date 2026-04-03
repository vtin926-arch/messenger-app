# Messenger Desktop App

Ứng dụng chat desktop đơn giản sử dụng Python, CustomTkinter và Supabase.

## Tính năng

- Đăng nhập và đăng ký người dùng với Supabase Auth
- Gửi và nhận tin nhắn thời gian thực
- Lịch sử chat được lưu trữ
- Chuyển tệp (upload/download)
- Giao diện người dùng đơn giản bằng CustomTkinter

## Yêu cầu hệ thống

- Python 3.11+
- Tài khoản Supabase

## Cài đặt

1. Clone repository này.
2. Tạo môi trường ảo: `python -m venv venv`
3. Kích hoạt môi trường: `source venv/bin/activate` (Linux/Mac) hoặc `venv\Scripts\activate` (Windows)
4. Cài đặt dependencies: `pip install -r requirements.txt`

## Cấu hình

1. Tạo dự án Supabase tại [supabase.com](https://supabase.com)
2. Sao chép `.env.example` thành `.env`
3. Điền `SUPABASE_URL` và `SUPABASE_ANON_KEY` từ dự án Supabase

## Thiết lập Supabase

1. Chạy file `schema.sql` trong SQL Editor của Supabase
2. Tạo bucket storage tên 'files' (có thể public)

## Chạy ứng dụng

`python main.py`

## Giới hạn

- MVP chỉ hỗ trợ chat 1-1
- Không có quản lý danh sách bạn bè
- Mã hóa tin nhắn chưa được triển khai đầy đủ

## Cải tiến tiếp theo

- Hỗ trợ chat nhóm
- Mã hóa end-to-end
- Thông báo push
- Tìm kiếm tin nhắn