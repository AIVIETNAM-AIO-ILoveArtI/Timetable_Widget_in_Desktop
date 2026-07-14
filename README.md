# Timetable-Widget-in-Desktop
Đây là sản phẩm Vibe coding đầu tay của tôi. Sản phẩm này là một chatbot thu nhỏ dựa trên việc gọi API để đọc lịch và đưa cho bạn lịch trình hôm nay của bạn.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](#)
[![Wayland](https://img.shields.io/badge/Wayland-Native-1793d1?logo=arch-linux&logoColor=white)](#)
[![Vibe Coding](https://img.shields.io/badge/Coding_Vibe-Chill_%26_AI-ff69b4)](#)

---

## ✨ Tính năng nổi bật

- ⚡ **Hỏi lịch siêu tốc:** Chatbot kết nối API qua WebSocket để đọc file thời khóa biểu và báo lịch chính xác.
- 🐧 **Tối ưu Wayland:** Hỗ trợ giao diện native qua `Quickshell` cho các môi trường như Hyprland.
- 🪟 **Chạy đa nền tảng:** Có sẵn bản giao diện `Window` tiêu chuẩn để chạy trên Windows, macOS hoặc các Distro Linux X11.

---

## 📁 Cấu trúc thư mục

```text
Timetable-Widget-in-Desktop/
├── Backend/
│   ├── Logic.py
│   └── source.txt
├── Frontend/
│   ├── UI_wayland.qml
│   ├── UI_Window.qml
│   ├── connect_Window
│   └── cat_cropped.png
├── README.md
└── requirements.txt
```

---

## ⚙️ Hướng dẫn cài đặt

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Cấu hình
API Key được lấy ở web: https://console.groq.com/home. 
Tạo file `.env` ở thư mục `Backend/` và thêm API Key:
```env
GROQ_API_KEY="your_api_key_here"
```

---

## 🚀 Cách khởi chạy

### Bước 1: Khởi động Backend (Bắt buộc)
```bash
cd Backend
python Logic.py
```

### Bước 2: Hiển thị giao diện (Chọn 1 trong 2)

**> Dành cho Wayland (Arch Linux / Hyprland)**
```bash
cd Frontend
quickshell UI_wayland.qml
```

**> Dành cho Windows / macOS / X11**
```bash
cd Frontend
python connect_Window
```
