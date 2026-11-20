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
