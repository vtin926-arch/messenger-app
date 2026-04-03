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

1. Mở trình duyệt và truy cập [supabase.com](https://supabase.com).
2. Nếu chưa có tài khoản, nhấn "Sign up" để đăng ký. Nếu đã có, nhấn "Sign in" để đăng nhập.
3. Sau khi đăng nhập, bạn sẽ thấy trang dashboard chính. Ở góc trên bên phải, nhấn nút màu xanh dương có chữ "New project".
4. Trong form tạo dự án:
   - **Name:** Nhập tên dự án, ví dụ: "Messenger App"
   - **Database Password:** Nhập mật khẩu mạnh cho database (ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số).
   - **Region:** Chọn region gần nhất với vị trí của bạn từ dropdown (ví dụ: "US East (N. Virginia)" hoặc "EU West (Ireland)").
5. Nhấn nút "Create new project" ở cuối form.
6. Chờ Supabase khởi tạo dự án (thường mất 2-3 phút). Bạn sẽ thấy thanh tiến trình và thông báo khi hoàn thành.

### Bước 2: Thiết lập Database

1. Sau khi dự án được tạo, bạn sẽ được chuyển đến dashboard của dự án.
2. Ở sidebar bên trái (menu điều hướng), cuộn xuống và chọn tab "SQL Editor" (biểu tượng hình bảng tính hoặc chữ "SQL").
3. Trong trang SQL Editor, bạn sẽ thấy một ô text lớn để nhập SQL.
4. Mở file `schema.sql` trong thư mục dự án của bạn bằng một editor (như VS Code, Notepad++).
5. Sao chép toàn bộ nội dung file `schema.sql` (từ đầu đến cuối).
6. Dán nội dung vào ô SQL trong Supabase.
7. Ở cuối trang, nhấn nút màu xanh "Run" (hoặc "Execute") để thực thi SQL.
8. Nếu thành công, bạn sẽ thấy thông báo "Success" và các bảng sẽ được tạo.

### Bước 3: Tạo Storage Bucket

1. Trong dashboard dự án, ở sidebar bên trái, chọn tab "Storage" (biểu tượng hình đám mây hoặc chữ "Storage").
2. Ở trang Storage, nhấn nút "Create bucket" (thường ở góc trên bên phải hoặc giữa trang).
3. Trong popup hoặc form xuất hiện:
   - **Name:** Nhập `files` (chính xác như vậy, không có dấu cách).
   - **Public bucket:** Đánh dấu chọn checkbox này nếu bạn muốn file có thể truy cập công khai (khuyến nghị cho MVP).
4. Nhấn nút "Create bucket" để hoàn thành.

### Bước 4: Lấy API Keys

1. Trong dashboard dự án, ở sidebar bên trái, chọn tab "Settings" (biểu tượng hình bánh răng).
2. Trong trang Settings, chọn mục "API" từ menu con bên trái (hoặc danh sách các tab).
3. Trong phần "Project API keys":
   - Tìm trường "Project URL" và sao chép giá trị (ví dụ: `https://abcdefghijklmnop.supabase.co`).
   - Tìm trường "anon public" và sao chép giá trị (đây là một chuỗi dài ký tự).

### Bước 5: Cấu hình file .env

1. Mở terminal/command prompt và điều hướng đến thư mục dự án:
   ```bash
   cd /path/to/messenger-app
   ```
2. Sao chép file `.env.example` thành `.env`:
   ```bash
   cp .env.example .env
   ```
3. Mở file `.env` bằng editor (ví dụ: `nano .env`, `code .env`, hoặc Notepad).
4. Thay thế các giá trị placeholder:
   - Thay `your_supabase_project_url` bằng Project URL bạn vừa sao chép từ bước 4.
   - Thay `your_supabase_anon_key` bằng anon public key từ bước 4.
5. Lưu file và đóng editor.

**Lưu ý:** Đừng commit file `.env` lên GitHub vì nó chứa thông tin nhạy cảm. File này đã được thêm vào `.gitignore`.

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
