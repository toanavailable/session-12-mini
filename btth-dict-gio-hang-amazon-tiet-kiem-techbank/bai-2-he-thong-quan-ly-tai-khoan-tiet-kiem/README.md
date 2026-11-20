# Bài 2 - Hệ thống quản lý tài khoản tiết kiệm TechBank

## Đề bài

Tại ngân hàng TechBank, tài khoản tiết kiệm là một trong những sản phẩm phổ biến dành cho khách hàng cá nhân. Mỗi sổ tiết kiệm lưu: Mã sổ tiết kiệm, Tên khách hàng, Số tiền gửi, Kỳ hạn gửi, Lãi suất năm, Trạng thái sổ. Dữ liệu là một danh sách các dictionary, mỗi dictionary đại diện cho một sổ.

Nhân viên giao dịch cần xem danh sách sổ, mở sổ mới, cập nhật thông tin, tất toán sổ, tính lãi dự kiến khi đến hạn và kiểm tra điều kiện rút trước hạn. Sai lãi suất, sai trạng thái hay xử lý sai nghiệp vụ rút trước hạn có thể gây sai lệch số liệu, khiếu nại và ảnh hưởng uy tín, nên cần xây dựng module "Savings Account Management CLI". Dữ liệu mẫu: STK001 - Nguyễn Văn An - 50,000,000 - 6 tháng - 6.5%; STK002 - Trần Thị Bình - 120,000,000 - 12 tháng - 7.2%; cả hai đều "active".

### Yêu cầu nghiệp vụ

Menu chương trình:

```
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
Mời bạn chọn chức năng (1-7): 
```

- **Chức năng 1 - Xem danh sách sổ tiết kiệm:** In toàn bộ sổ theo dạng "1. Mã số: ... | Khách hàng: ... | Số tiền gửi: ... | Kỳ hạn: ... tháng | Lãi suất: ...%/năm | Trạng thái: ..."; danh sách rỗng thì in "Danh sách sổ tiết kiệm hiện đang trống".
- **Chức năng 2 - Mở sổ tiết kiệm mới:** Nhập mã, tên, số tiền gửi, kỳ hạn, lãi suất. Chuẩn hóa mã (xóa khoảng trắng, viết hoa), mã không trùng, tên không rỗng, tiền gửi và kỳ hạn là số nguyên dương, lãi suất là số thực > 0. Hợp lệ thì thêm sổ với trạng thái mặc định "active".
- **Chức năng 3 - Cập nhật thông tin sổ:** Nhập mã cần cập nhật và thông tin mới; chỉ cập nhật sổ "active", kiểm tra dữ liệu như khi mở sổ. Không thấy mã: "Không tìm thấy mã số tiết kiệm!"; sổ đã tất toán: "Không thể cập nhật số tiết kiệm đã tất toán!".
- **Chức năng 4 - Tất toán sổ:** Nhập mã; nếu tồn tại thì đổi trạng thái thành "closed". Sổ không bị xóa khỏi danh sách để phục vụ đối soát lịch sử.
- **Chức năng 5 - Tính lãi dự kiến khi đến hạn:** Chỉ tính cho sổ "active". Tiền lãi = Số tiền gửi × Lãi suất năm / 100 × Kỳ hạn / 12; Tổng tiền nhận = Số tiền gửi + Tiền lãi.
- **Chức năng 6 - Kiểm tra điều kiện rút trước hạn:** Nhập mã và số tháng thực gửi (số nguyên dương). Gửi chưa đủ kỳ hạn → rút trước hạn, lãi suất 0.5%/năm; đủ kỳ hạn → lãi suất ban đầu. Tiền lãi thực nhận = Số tiền gửi × Lãi suất áp dụng / 100 × Số tháng thực gửi / 12.
- **Chức năng 7 - Thoát chương trình:** Dừng chương trình.

### Edge cases (bẫy dữ liệu)

| Bẫy | Mô tả |
|---|---|
| Bẫy 1 | Mở sổ với mã đã tồn tại → "Mã số tiết kiệm đã tồn tại!" |
| Bẫy 2 | Tên khách hàng rỗng hoặc chỉ khoảng trắng → "Tên khách hàng không được để trống" |
| Bẫy 3 | Số tiền gửi hoặc kỳ hạn là chữ, số âm hoặc 0 → "Số tiền gửi hoặc kỳ hạn không hợp lệ" |
| Bẫy 4 | Lãi suất là chữ, số âm hoặc 0 → "Lãi suất không hợp lệ!" |
| Bẫy 5 | Cập nhật, tất toán, tính lãi, kiểm tra rút trước hạn với mã không tồn tại → "Không tìm thấy mã số tiết kiệm" |
| Bẫy 6 | Thao tác trên sổ "closed" → "Không thể thao tác với sổ tiết kiệm đã tất toán" |
| Bẫy 7 | Số tháng thực gửi là chữ, số âm hoặc 0 → "Số tháng thực gửi không hợp lệ!" |
| Bẫy 8 | Menu ngoài 1-7 hoặc nhập chữ → "Lựa chọn không hợp lệ, vui lòng nhập lại", hiện lại menu |

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Xử lý |
|---|---|---|---|
| Danh sách sổ | `saving_accounts` | `list[dict]` | Key: account_id, customer_name, balance, term_months, interest_rate, status |
| Lựa chọn menu | `choice` | `str` | So sánh "1"…"7" |
| Mã sổ | `account_id` | `str` | "".join(split()).upper() |
| Tên khách hàng | `customer_name` | `str` | " ".join(split()), không rỗng |
| Số tiền gửi / kỳ hạn | `balance_text, term_text` | `str → int` | isdigit() và > 0 |
| Lãi suất năm | `rate_text` | `str → float` | replace(".", "", 1).isdigit() và > 0 |
| Số tháng thực gửi | `months_text → actual_months` | `str → int` | isdigit() và > 0 |
| Sổ tìm thấy | `found_account` | `dict / None` | None nếu không có mã |
| Tiền lãi / tổng tiền | `interest` | `float` | Hiển thị {:,.0f} VNĐ |

### Đề xuất giải pháp

- Danh sách sổ là list các dictionary; truy cập và sửa thông tin qua key (account["status"] = "closed"...).
- Chức năng 2 - 6 đều bắt đầu bằng nhập mã, nên dùng chung một bước: chuẩn hóa mã bằng "".join(input().split()).upper() (xóa mọi khoảng trắng, kể cả ở giữa), rồi duyệt list tìm dictionary có account_id trùng, lưu vào found_account.
- Kiểm tra số nguyên dương bằng isdigit() trước khi int(); lãi suất là số thực nên bỏ một dấu chấm rồi mới isdigit() ("6.5" → "65"), sau đó float() > 0. Cách này chặn được chữ, số âm, ô trống mà không cần try-except.
- Mỗi lỗi in đúng thông báo của đề rồi continue để quay lại menu; dữ liệu chỉ được ghi vào list khi tất cả các trường đều hợp lệ.
- Tất toán chỉ đổi status thành "closed", không xóa khỏi list. Chức năng 3, 4, 5, 6 đều kiểm tra status trước khi xử lý.
- Lãi suất rút trước hạn là hằng EARLY_RATE = 0.5. Kiểm tra rút trước hạn: số tháng thực gửi < kỳ hạn → dùng EARLY_RATE, ngược lại dùng lãi suất của sổ; tiền lãi tính theo số tháng thực gửi.

### Thiết kế thuật toán (Pseudocode)

```
saving_accounts ← dữ liệu mẫu; EARLY_RATE ← 0.5
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU "1": rỗng → "Danh sách ... đang trống"; ngược lại IN từng sổ
    NẾU choice ∈ {"2".."6"}:
        NHẬP mã → xóa khoảng trắng, upper(); rỗng → báo lỗi
        found_account ← sổ có mã trùng (None nếu không có)
        NẾU "2" hoặc "3":
            "2" và đã có → "Mã số tiết kiệm đã tồn tại!"
            "3" và không có → "Không tìm thấy mã số tiết kiệm!"
            "3" và status ≠ active → "Không thể cập nhật số tiết kiệm đã tất toán!"
            NHẬP tên (không rỗng), tiền gửi + kỳ hạn (số nguyên > 0), lãi suất (số thực > 0)
            "2" → append({..., status: "active"});  "3" → ghi đè 4 trường
        NGƯỢC LẠI ("4","5","6"):
            không có → "Không tìm thấy mã số tiết kiệm!"
            status ≠ active → "Không thể thao tác với sổ tiết kiệm đã tất toán"
            "4": status ← "closed"
            "5": lãi ← tiền × lãi_suất / 100 × kỳ_hạn / 12; IN lãi và tổng
            "6": NHẬP số tháng (> 0)
                 tháng < kỳ_hạn → suất ← 0.5 ; ngược lại suất ← lãi suất sổ
                 lãi ← tiền × suất / 100 × tháng / 12; IN lãi và tổng
    NẾU "7": THOÁT
    NGƯỢC LẠI: "Lựa chọn không hợp lệ, vui lòng nhập lại"
```

## (2) Triển khai code

File: [`savings_account.py`](savings_account.py)

```python
"""Savings Account Management CLI - Hệ thống quản lý tài khoản tiết kiệm TechBank."""

# =====================================================================
# KHỞI TẠO: danh sách sổ tiết kiệm, mỗi sổ là một dictionary
# =====================================================================
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]
EARLY_RATE = 0.5          # Lãi suất rút trước hạn cố định (%/năm)

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    choice = input("Mời bạn chọn chức năng (1-7): ").strip()

    # =================================================================
    # Chức năng 1: Xem danh sách sổ tiết kiệm
    # =================================================================
    if choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
            continue
        print("Danh sách sổ tiết kiệm:")
        for stt, account in enumerate(saving_accounts, start=1):
            print(f"{stt}. Mã số: {account['account_id']} | Khách hàng: {account['customer_name']} | "
                  f"Số tiền gửi: {account['balance']} | Kỳ hạn: {account['term_months']} tháng | "
                  f"Lãi suất: {account['interest_rate']:g}%/năm | Trạng thái: {account['status']}")

    # =================================================================
    # Chức năng 2 - 6: đều bắt đầu bằng việc nhập mã sổ
    # =================================================================
    elif choice in ["2", "3", "4", "5", "6"]:
        if choice == "2":
            prompt = "Nhập mã số tiết kiệm: "
        elif choice == "3":
            prompt = "Nhập mã số tiết kiệm cần cập nhật: "
        elif choice == "4":
            prompt = "Nhập mã số tiết kiệm cần tất toán/xóa: "
        elif choice == "5":
            prompt = "Nhập mã số tiết kiệm cần tính lãi: "
        else:
            prompt = "Nhập mã số tiết kiệm cần kiểm tra: "

        # Chuẩn hóa mã: xóa mọi khoảng trắng và viết hoa toàn bộ
        account_id = "".join(input(prompt).split()).upper()
        if account_id == "":
            print("Mã số tiết kiệm không được để trống!")
            continue

        # Tìm dictionary sổ có "account_id" trùng mã (None nếu không có)
        found_account = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                found_account = account
                break

        # ---------- Chức năng 2 và 3: nhập + kiểm tra thông tin sổ ----------
        if choice == "2" or choice == "3":
            if choice == "2" and found_account is not None:
                print("Mã số tiết kiệm đã tồn tại!")                          # Bẫy 1
                continue
            if choice == "3":
                if found_account is None:
                    print("Không tìm thấy mã số tiết kiệm!")                  # Bẫy 5
                    continue
                if found_account["status"] != "active":
                    print("Không thể cập nhật số tiết kiệm đã tất toán!")     # Bẫy 6
                    continue
                suffix = " mới"
            else:
                suffix = ""

            # Tên khách hàng: bỏ khoảng trắng thừa, không được rỗng
            customer_name = " ".join(input(f"Nhập tên khách hàng{suffix}: ").split())
            if customer_name == "":
                print("Tên khách hàng không được để trống")                   # Bẫy 2
                continue

            # Số tiền gửi và kỳ hạn: số nguyên dương
            balance_text = input(f"Nhập số tiền gửi{suffix}: ").strip()
            term_text = input(f"Nhập kỳ hạn{suffix} theo tháng: ").strip()
            if (not balance_text.isdigit() or int(balance_text) <= 0
                    or not term_text.isdigit() or int(term_text) <= 0):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")                 # Bẫy 3
                continue

            # Lãi suất: số thực > 0 (cho phép tối đa 1 dấu chấm thập phân)
            rate_text = input(f"Nhập lãi suất năm{suffix}: ").strip()
            if not rate_text.replace(".", "", 1).isdigit() or float(rate_text) <= 0:
                print("Lãi suất không hợp lệ!")                               # Bẫy 4
                continue

            if choice == "2":
                new_account = {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": int(balance_text),
                    "term_months": int(term_text),
                    "interest_rate": float(rate_text),
                    "status": "active"
                }
                saving_accounts.append(new_account)
                print(f"Mở sổ tiết kiệm {account_id} thành công!")
            else:
                found_account["customer_name"] = customer_name
                found_account["balance"] = int(balance_text)
                found_account["term_months"] = int(term_text)
                found_account["interest_rate"] = float(rate_text)
                print(f"Cập nhật sổ tiết kiệm {account_id} thành công!")
            continue

        # ---------- Chức năng 4, 5, 6: sổ phải tồn tại và còn active ----------
        if found_account is None:
            print("Không tìm thấy mã số tiết kiệm!")                          # Bẫy 5
            continue
        if found_account["status"] != "active":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")          # Bẫy 6
            continue

        balance = found_account["balance"]
        if choice == "4":
            # Không xóa khỏi list, chỉ đổi trạng thái để giữ lịch sử đối soát
            found_account["status"] = "closed"
            print(f"Tất toán sổ tiết kiệm {account_id} thành công! Trạng thái: closed")

        elif choice == "5":
            interest = balance * found_account["interest_rate"] / 100 * found_account["term_months"] / 12
            print(f"Sổ {account_id} - Kỳ hạn {found_account['term_months']} tháng, "
                  f"lãi suất {found_account['interest_rate']:g}%/năm")
            print(f"Tiền lãi dự kiến: {interest:,.0f} VNĐ")
            print(f"Tổng tiền nhận khi đến hạn: {balance + interest:,.0f} VNĐ")

        else:
            months_text = input("Nhập số tháng thực gửi: ").strip()
            if not months_text.isdigit() or int(months_text) <= 0:
                print("Số tháng thực gửi không hợp lệ!")                      # Bẫy 7
                continue
            actual_months = int(months_text)

            if actual_months < found_account["term_months"]:
                applied_rate = EARLY_RATE
                print(f"Rút trước hạn ({actual_months}/{found_account['term_months']} tháng) "
                      f"- áp dụng lãi suất {applied_rate:g}%/năm")
            else:
                applied_rate = found_account["interest_rate"]
                print(f"Đủ kỳ hạn ({actual_months}/{found_account['term_months']} tháng) "
                      f"- hưởng lãi suất {applied_rate:g}%/năm")
            interest = balance * applied_rate / 100 * actual_months / 12
            print(f"Tiền lãi thực nhận: {interest:,.0f} VNĐ")
            print(f"Tổng tiền thực nhận: {balance + interest:,.0f} VNĐ")

    # =================================================================
    # Chức năng 7: Thoát
    # =================================================================
    elif choice == "7":
        print("Thoát chương trình. Cảm ơn bạn đã sử dụng hệ thống TechBank!")
        break

    # Bẫy 8: ngoài phạm vi 1-7 hoặc nhập chữ
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
```

## Kết quả

Chạy thử toàn bộ chức năng và bẫy dữ liệu *(ẩn menu lặp lại cho gọn)*:

```
Mời bạn chọn chức năng (1-7): 1
Danh sách sổ tiết kiệm:
1. Mã số: STK001 | Khách hàng: Nguyễn Văn An | Số tiền gửi: 50000000 | Kỳ hạn: 6 tháng | Lãi suất: 6.5%/năm | Trạng thái: active
2. Mã số: STK002 | Khách hàng: Trần Thị Bình | Số tiền gửi: 120000000 | Kỳ hạn: 12 tháng | Lãi suất: 7.2%/năm | Trạng thái: active

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm:  stk 001
Mã số tiết kiệm đã tồn tại!

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm: stk003
Nhập tên khách hàng:    
Tên khách hàng không được để trống

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm: STK003
Nhập tên khách hàng: Lê Văn Cường
Nhập số tiền gửi: -100
Nhập kỳ hạn theo tháng: 12
Số tiền gửi hoặc kỳ hạn không hợp lệ

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm: STK003
Nhập tên khách hàng: Lê Văn Cường
Nhập số tiền gửi: abc
Nhập kỳ hạn theo tháng: 0
Số tiền gửi hoặc kỳ hạn không hợp lệ

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm: STK003
Nhập tên khách hàng: Lê Văn Cường
Nhập số tiền gửi: 30000000
Nhập kỳ hạn theo tháng: 9
Nhập lãi suất năm: abc
Lãi suất không hợp lệ!

Mời bạn chọn chức năng (1-7): 2
Nhập mã số tiết kiệm: stk003
Nhập tên khách hàng:   Lê Văn   Cường 
Nhập số tiền gửi: 30000000
Nhập kỳ hạn theo tháng: 9
Nhập lãi suất năm: 5.8
Mở sổ tiết kiệm STK003 thành công!

Mời bạn chọn chức năng (1-7): 1
Danh sách sổ tiết kiệm:
1. Mã số: STK001 | Khách hàng: Nguyễn Văn An | Số tiền gửi: 50000000 | Kỳ hạn: 6 tháng | Lãi suất: 6.5%/năm | Trạng thái: active
2. Mã số: STK002 | Khách hàng: Trần Thị Bình | Số tiền gửi: 120000000 | Kỳ hạn: 12 tháng | Lãi suất: 7.2%/năm | Trạng thái: active
3. Mã số: STK003 | Khách hàng: Lê Văn Cường | Số tiền gửi: 30000000 | Kỳ hạn: 9 tháng | Lãi suất: 5.8%/năm | Trạng thái: active

Mời bạn chọn chức năng (1-7): 3
Nhập mã số tiết kiệm cần cập nhật: STK999
Không tìm thấy mã số tiết kiệm!

Mời bạn chọn chức năng (1-7): 3
Nhập mã số tiết kiệm cần cập nhật: stk002
Nhập tên khách hàng mới: Trần Thị Bình
Nhập số tiền gửi mới: 150000000
Nhập kỳ hạn mới theo tháng: 12
Nhập lãi suất năm mới: 7.5
Cập nhật sổ tiết kiệm STK002 thành công!

Mời bạn chọn chức năng (1-7): 5
Nhập mã số tiết kiệm cần tính lãi: STK001
Sổ STK001 - Kỳ hạn 6 tháng, lãi suất 6.5%/năm
Tiền lãi dự kiến: 1,625,000 VNĐ
Tổng tiền nhận khi đến hạn: 51,625,000 VNĐ

Mời bạn chọn chức năng (1-7): 5
Nhập mã số tiết kiệm cần tính lãi: STK002
Sổ STK002 - Kỳ hạn 12 tháng, lãi suất 7.5%/năm
Tiền lãi dự kiến: 11,250,000 VNĐ
Tổng tiền nhận khi đến hạn: 161,250,000 VNĐ

Mời bạn chọn chức năng (1-7): 6
Nhập mã số tiết kiệm cần kiểm tra: STK001
Nhập số tháng thực gửi: 3
Rút trước hạn (3/6 tháng) - áp dụng lãi suất 0.5%/năm
Tiền lãi thực nhận: 62,500 VNĐ
Tổng tiền thực nhận: 50,062,500 VNĐ

Mời bạn chọn chức năng (1-7): 6
Nhập mã số tiết kiệm cần kiểm tra: STK001
Nhập số tháng thực gửi: 6
Đủ kỳ hạn (6/6 tháng) - hưởng lãi suất 6.5%/năm
Tiền lãi thực nhận: 1,625,000 VNĐ
Tổng tiền thực nhận: 51,625,000 VNĐ

Mời bạn chọn chức năng (1-7): 6
Nhập mã số tiết kiệm cần kiểm tra: STK001
Nhập số tháng thực gửi: 0
Số tháng thực gửi không hợp lệ!

Mời bạn chọn chức năng (1-7): 6
Nhập mã số tiết kiệm cần kiểm tra: STK001
Nhập số tháng thực gửi: abc
Số tháng thực gửi không hợp lệ!

Mời bạn chọn chức năng (1-7): 4
Nhập mã số tiết kiệm cần tất toán/xóa: STK003
Tất toán sổ tiết kiệm STK003 thành công! Trạng thái: closed

Mời bạn chọn chức năng (1-7): 1
Danh sách sổ tiết kiệm:
1. Mã số: STK001 | Khách hàng: Nguyễn Văn An | Số tiền gửi: 50000000 | Kỳ hạn: 6 tháng | Lãi suất: 6.5%/năm | Trạng thái: active
2. Mã số: STK002 | Khách hàng: Trần Thị Bình | Số tiền gửi: 150000000 | Kỳ hạn: 12 tháng | Lãi suất: 7.5%/năm | Trạng thái: active
3. Mã số: STK003 | Khách hàng: Lê Văn Cường | Số tiền gửi: 30000000 | Kỳ hạn: 9 tháng | Lãi suất: 5.8%/năm | Trạng thái: closed

Mời bạn chọn chức năng (1-7): 3
Nhập mã số tiết kiệm cần cập nhật: STK003
Không thể cập nhật số tiết kiệm đã tất toán!

Mời bạn chọn chức năng (1-7): 5
Nhập mã số tiết kiệm cần tính lãi: STK003
Không thể thao tác với sổ tiết kiệm đã tất toán

Mời bạn chọn chức năng (1-7): 6
Nhập mã số tiết kiệm cần kiểm tra: STK003
Không thể thao tác với sổ tiết kiệm đã tất toán

Mời bạn chọn chức năng (1-7): 4
Nhập mã số tiết kiệm cần tất toán/xóa: STK003
Không thể thao tác với sổ tiết kiệm đã tất toán

Mời bạn chọn chức năng (1-7): 4
Nhập mã số tiết kiệm cần tất toán/xóa: X01
Không tìm thấy mã số tiết kiệm!

Mời bạn chọn chức năng (1-7): 8
Lựa chọn không hợp lệ, vui lòng nhập lại

Mời bạn chọn chức năng (1-7): abc
Lựa chọn không hợp lệ, vui lòng nhập lại

Mời bạn chọn chức năng (1-7): 7
Thoát chương trình. Cảm ơn bạn đã sử dụng hệ thống TechBank!
```

### Bảng kiểm thử

| Kịch bản | Dữ liệu | Kết quả |
|---|---|---|
| Xem danh sách mẫu | Chọn 1 | In 2 sổ đúng định dạng đề |
| Bẫy 1 - mã trùng (có khoảng trắng, chữ thường) | " stk 001" | Mã số tiết kiệm đã tồn tại! |
| Bẫy 2 - tên rỗng | "   " | Tên khách hàng không được để trống |
| Bẫy 3 - tiền âm / chữ, kỳ hạn 0 | -100; abc, 0 | Số tiền gửi hoặc kỳ hạn không hợp lệ |
| Bẫy 4 - lãi suất chữ | abc | Lãi suất không hợp lệ! |
| Mở sổ hợp lệ | stk003, 30,000,000, 9 tháng, 5.8 | Thêm STK003, trạng thái active |
| Bẫy 5 - cập nhật mã không có | STK999 | Không tìm thấy mã số tiết kiệm! |
| Cập nhật sổ | stk002 → 150,000,000, 12, 7.5 | Cập nhật thành công |
| Tính lãi đến hạn | STK001; STK002 | 1,625,000 → 51,625,000; 11,250,000 → 161,250,000 |
| Rút trước hạn | STK001, 3 tháng | Lãi 0.5% → 62,500; tổng 50,062,500 |
| Đủ kỳ hạn | STK001, 6 tháng | Lãi 6.5% → 1,625,000 |
| Bẫy 7 - số tháng 0 / chữ | 0, abc | Số tháng thực gửi không hợp lệ! |
| Tất toán | STK003 | Trạng thái closed, vẫn còn trong danh sách |
| Bẫy 6 - thao tác sổ đã tất toán | STK003 với chức năng 3, 5, 6, 4 | Báo không thể thao tác / cập nhật |
| Bẫy 8 - menu sai | 8, abc | Lựa chọn không hợp lệ, vui lòng nhập lại |
| Thoát | 7 | Kết thúc chương trình |

## Ghi chú

Chương trình giữ nguyên câu thông báo của đề, kể cả chữ "số tiết kiệm" trong "Không thể cập nhật số tiết kiệm đã tất toán!". Tiền lãi được hiển thị làm tròn đến đồng ({:,.0f}).

## Cách chạy

```bash
python savings_account.py
```
