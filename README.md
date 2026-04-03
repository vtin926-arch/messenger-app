# Messenger Desktop App

Ứng dụng chat desktop đơn giản sử dụng Python, CustomTkinter và Supabase.

## Tính năng

- Đăng nhập và đăng ký người dùng với Supabase Auth
- Gửi và nhận tin nhắn thời gian thực
- Lịch sử chat được lưu trữ
- Chuyển tệp (upload/download)
- Giao diện người dùng đơn giản bằng CustomTkinter

## Yêu cầu hệ thống

- **Hệ điều hành:** Linux, macOS, hoặc Windows
- **Python:** Phiên bản 3.11 hoặc cao hơn
- **Tkinter:** Cần thiết cho CustomTkinter (thường có sẵn trên Linux/Mac, trên Windows cần cài đặt)
- **Tài khoản Supabase:** Để sử dụng dịch vụ backend
- **Kết nối internet:** Để đồng bộ dữ liệu với Supabase

## Hướng dẫn cài đặt chi tiết

### Bước 1: Cài đặt Python và các công cụ cần thiết

1. **Kiểm tra phiên bản Python:**
   ```bash
   python3 --version
   ```
   Nếu chưa có Python 3.11+, hãy cài đặt từ [python.org](https://python.org) hoặc sử dụng package manager của hệ điều hành.

2. **Cài đặt Tkinter (nếu cần):**
   - **Ubuntu/Debian:** `sudo apt install python3-tk`
   - **macOS:** Tkinter thường có sẵn với Python từ python.org
   - **Windows:** Tkinter có sẵn khi cài đặt Python từ python.org

3. **Cài đặt Git (để clone repository):**
   ```bash
   # Ubuntu/Debian
   sudo apt install git

   # macOS (với Homebrew)
   brew install git

   # Windows: Tải từ https://git-scm.com/
   ```

### Bước 2: Clone repository

```bash
git clone https://github.com/your-username/messenger-app.git
cd messenger-app
```

(Thay `your-username` và `messenger-app` bằng tên repository thực của bạn)

### Bước 3: Tạo môi trường ảo

```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
# Linux/Mac:
source venv/bin/activate

# Windows:
# venv\Scripts\activate
```

### Bước 4: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

## Cấu hình Supabase chi tiết

### Bước 1: Tạo dự án Supabase

1. Truy cập [supabase.com](https://supabase.com) và đăng nhập.
2. Nhấn "New project".
3. Điền thông tin:
   - **Name:** Tên dự án (ví dụ: "Messenger App")
   - **Database Password:** Đặt mật khẩu mạnh
   - **Region:** Chọn region gần nhất
4. Nhấn "Create new project" và chờ khởi tạo (có thể mất vài phút).

### Bước 2: Thiết lập Database

1. Trong dashboard Supabase, chọn tab "SQL Editor".
2. Sao chép nội dung file `schema.sql` và dán vào SQL Editor.
3. Nhấn "Run" để thực thi schema.

### Bước 3: Tạo Storage Bucket

1. Chọn tab "Storage" trong dashboard.
2. Nhấn "Create bucket".
3. Đặt tên: `files`
4. Chọn "Public bucket" nếu muốn file có thể truy cập công khai.
5. Nhấn "Create bucket".

### Bước 4: Lấy API Keys

1. Chọn tab "Settings" > "API".
2. Sao chép:
   - **Project URL**
   - **anon public** key

### Bước 5: Cấu hình file .env

1. Sao chép file `.env.example` thành `.env`:
   ```bash
   cp .env.example .env
   ```

2. Mở file `.env` và điền thông tin:
   ```
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_ANON_KEY=your-anon-key-here
   ```

## Chạy ứng dụng

1. Đảm bảo môi trường ảo đã kích hoạt:
   ```bash
   source venv/bin/activate  # Linux/Mac
   # hoặc venv\Scripts\activate  # Windows
   ```

2. Chạy ứng dụng:
   ```bash
   python main.py
   ```

## Sử dụng ứng dụng

1. **Đăng ký/Đăng nhập:**
   - Mở ứng dụng, nhập email và mật khẩu.
   - Nếu chưa có tài khoản, nhấn "Đăng ký".
   - Kiểm tra email để xác nhận tài khoản.

2. **Chat:**
   - Sau khi đăng nhập, cửa sổ chat sẽ mở.
   - Nhập tin nhắn và nhấn "Gửi".
   - Tin nhắn sẽ hiển thị thời gian thực.

3. **Chuyển tệp:**
   - Nhấn "Chọn tệp" để chọn file.
   - Nhấn "Gửi tệp" để upload.

## Troubleshooting

### Lỗi "ModuleNotFoundError"
- Đảm bảo đã kích hoạt môi trường ảo và cài đặt dependencies.

### Lỗi Supabase
- Kiểm tra file `.env` có đúng thông tin không.
- Đảm bảo dự án Supabase đang hoạt động.

### Lỗi Tkinter
- Cài đặt Tkinter như hướng dẫn ở trên.

### Ứng dụng không khởi động
- Kiểm tra Python version: `python3 --version`
- Đảm bảo tất cả dependencies đã cài đặt.

## Giới hạn

- MVP chỉ hỗ trợ chat 1-1
- Không có quản lý danh sách bạn bè
- Mã hóa tin nhắn chưa được triển khai đầy đủ

## Cải tiến tiếp theo

- Hỗ trợ chat nhóm
- Mã hóa end-to-end
- Thông báo push
- Tìm kiếm tin nhắn

## Đóng góp

Mời đóng góp! Tạo issue hoặc pull request trên GitHub.

## Giấy phép

MIT License
