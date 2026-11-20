# Bài tập thực hành Python - Dictionary: Giỏ hàng Amazon và Sổ tiết kiệm TechBank

Tổng hợp 2 bài tập thực hành (BTTH) về **List of Dictionary** trong Python. Cả 2 bài là chương trình dòng lệnh (CLI) có menu lặp liên tục, dùng dictionary để lưu từng bản ghi (sản phẩm, sổ tiết kiệm), thực hiện thêm, sửa, xóa, tìm kiếm theo mã, tính toán tổng tiền / tiền lãi, và xử lý các bẫy dữ liệu để chương trình không bị dừng khi người dùng nhập sai.

## Thứ tự bài tập

| STT | Bài tập | Kỹ thuật trọng tâm |
|---|---|---|
| 1 | [Hệ thống quản lý giỏ hàng Amazon](bai-1-he-thong-quan-ly-gio-hang-amazon/) | List of dict, tìm theo key `id`, cộng dồn `item["number"]`, `append` / `remove`, tính tổng tiền |
| 2 | [Hệ thống quản lý tài khoản tiết kiệm TechBank](bai-2-he-thong-quan-ly-tai-khoan-tiet-kiem/) | Chuẩn hóa mã, kiểm tra số nguyên / số thực không cần try-except, trạng thái `active` / `closed`, công thức tính lãi, rút trước hạn |

Mỗi thư mục bài có `README.md` riêng (đề bài, phân tích Input/Output, giải pháp, pseudocode, mã nguồn, kết quả chạy thử, bảng kiểm thử) và mã nguồn Python.

## Báo cáo

- [Báo cáo dạng Word (DOCX)](bao-cao-btth-dict-amazon-techbank.docx)

## Cách chạy

Yêu cầu Python 3.x. Vào thư mục bài cần chạy, ví dụ:

```bash
cd bai-1-he-thong-quan-ly-gio-hang-amazon
python amazon_cart.py
```
